class InstanceTag:
    def __init__(self, user,email, appname, itemid):
        self.dataclassification = "Cisco Restricted"
        self.environment = 'dev'
        self.resourceowner = user
        self.ciscomailalias = email
        self.datataxonomy = 'Cisco Operations Data'
        self.appname = appname
        self.itemid = itemid
        self.approved = "False"

    def get_tags(self):
        tags = [{
            'Key': 'Data Classification',
            'Value': str(self.dataclassification)
        }, {
            'Key': 'Environment',
            'Value': str(self.environment)
        }, {
            'Key': 'ResourceOwner',
            'Value': str(self.resourceowner)
        }, {
            'Key': 'Cisco Mail Alias',
            'Value': str(self.ciscomailalias)
        }, {
            'Key': 'Data Taxonomy',
            'Value': str(self.datataxonomy)
        }, {
            'Key': 'Application Name',
            'Value': str(self.appname)
        }, {
            'Key': 'Validated',
            'Value': self.approved
        }]

        return tags
