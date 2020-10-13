import logging
import boto3
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Event:
    """
    Data model class to hold event data
    Used to parse once so the  main handler can call as needed
    """
    def __init__(self,event):
        """
           :param event: event json sent to the lambda function
        """
        self.region = event['region']
        _detail = event['detail']
        logger.info('request detail: ' + str(_detail))
        self.eventname = _detail['eventName']
        self.arn = _detail['userIdentity']['arn']
        self.principal = _detail['userIdentity']['principalId']
        _userType = _detail['userIdentity']['type']
        self.responseElements = _detail['responseElements']
        if 'errorCode' in _detail.keys():
            self.errorCode = _detail['errorCode']
            self.errorMessage = _detail['errorMessage']
        if _userType == 'IAMUser':
            self.user = _detail['userIdentity']['userName']
        else:
            self.user = self.principal.split(':')[1]
        self.appName = None
        self.runInstance = False
        self.createValumes = False
        self.createImage = False
        self.createSnapshot = False
        
        if self.eventname == 'RunInstances':
            self.runInstance = True
            self.instanceIds = _detail['responseElements']['instancesSet']['items']
        elif self.eventname == 'CreateVolume':
            self.createVolumes = True
            self.volumeIds = _detail['responseElements']['volumeId']
        elif self.eventname == "CreateImage":
            self.createImage = True
            self.imageIds = _detail['responseElements']['imageId']
        elif self.eventname == "CreateSnapshot":
            self.createSnapshot = True
            self.snapShotIds = _detail['responseElements']['snapshotId']
        self.ids = []
        
    def getVolumeIds(self):
        if self.createVolumes:
           self.ids.append(self.volumeIds)
           logger.info(self.ids)
    
    def getInstsanceIds(self):
        ec2 = boto3.resource('ec2', region_name=self.region)
        items = self.instanceIds
        for item in items:
            self.ids.append(item['instanceId'])
            if "tagSet" in item.keys():
                for tag in item['tagSet']['items']:
                    if tag['key'] == "Name":
                        self.appName = tag['value']
                    
                
        logger.info(self.ids)
        logger.info('number of instances: ' + str(len(self.ids)))

        base = ec2.instances.filter(InstanceIds=self.ids)
        # loop through the instances
        for instance in base:
            for vol in instance.volumes.all():
                self.ids.append(vol.id)
            for eni in instance.network_interfaces:
                self.ids.append(eni.id)
    
    def getImageIds(self):
        self.ids.append(self.instanceIds)
        logger.info(self.ids)
        
    def getSnapShotIds(self):
        self.ids.append(self.snapShotIds)
        logger.info(self.ids)
    
    