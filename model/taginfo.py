

class InstanceTag:
	
	def __init__(self,user,appname):
		self.dataclassification = "Cisco Public"
		self.environment = 'NonProd'
		self.resourceowner = user
		self.ciscomailalias = user
		self.datataxonomy = 'Cisco '
		self.appname = appname

	def get_tags(self):
		tags= [{
				'Key'  : 'Data Classification',
				'Value': str(self.dataclassification)
		}, {
				'Key'  : 'Environment',
				'Value': str(self.environment)
		}, {
				'Key'  : 'Resource Owner',
				'Value': str(self.resourceowner)
		}, {
				'Key'  : 'Cisco Mail Alias',
				'Value': str(self.ciscomailalias)
		}, {
				'Key'  : 'Data Taxonomy',
				'Value': str(self.datataxonomy)
		}, {
				'Key'  : 'Application Name',
				'Value': str(self.appname)
		}]
		
		return tags