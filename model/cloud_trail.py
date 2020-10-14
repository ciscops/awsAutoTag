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
        self.responseElements = _detail['responseElements']
        if 'errorCode' in _detail.keys():
            self.errorcode = _detail['errorCode']
            self.errormessage = _detail['errorMessage']
        if _detail['userIdentity']['type'] == 'IAMUser':
            self.user = _detail['userIdentity']['userName']
        else:
            self.user = self.principal.split(':')[1]
        self.appname = None
        self.runinstance = False
        self.createvolumes = False
        self.createimage = False
        self.createsnapshot = False
        
        if self.eventname == 'RunInstances':
            self.runinstance = True
            self.instanceids = _detail['responseElements']['instancesSet']['items']
        elif self.eventname == 'CreateVolume':
            self.createvolumes = True
            self.volumeids = _detail['responseElements']['volumeId']
        elif self.eventname == "CreateImage":
            self.createimage = True
            self.imagiids = _detail['responseElements']['imageId']
        elif self.eventname == "CreateSnapshot":
            self.createsnapshot = True
            self.snapshotids = _detail['responseElements']['snapshotId']
        self.ids = []
        
    def get_volume_ids(self):
        if self.createvolumes:
           self.ids.append(self.volumeids)
           logger.info(self.ids)
    
    def get_instsance_ids(self):
        ec2 = boto3.resource('ec2', region_name=self.region)
        items = self.instanceids
        for item in items:
            self.ids.append(item['instanceId'])
            if "tagSet" in item.keys():
                for tag in item['tagSet']['items']:
                    if tag['key'] == "Name":
                        self.appname = tag['value']
                    
                
        logger.info(self.ids)
        logger.info('number of instances: ' + str(len(self.ids)))

        base = ec2.instances.filter(InstanceIds=self.ids)
        # loop through the instances
        for instance in base:
            for vol in instance.volumes.all():
                self.ids.append(vol.id)
            for eni in instance.network_interfaces:
                self.ids.append(eni.id)
    
    def get_image_ids(self):
        self.ids.append(self.instanceids)
        logger.info(self.ids)
        
    def get_snap_shot_ids(self):
        self.ids.append(self.snapshotids)
        logger.info(self.ids)
    
    