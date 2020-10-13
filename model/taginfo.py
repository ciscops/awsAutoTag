

class InstanceTag:
	
	def __init__(self,user,AppName):
		self.DataClassification = "Cisco Public"
		self.Environment = 'NonProd'
		self.ResourceOwner = user
		self.CiscMailAlias = user
		self.DataTaxonomy = 'Cisco '
		self.AppName = AppName

	def getTags(self):
		tags=[]
		tags.append({
					'Key'  : 'Data Classification',
					'Value': str(self.DataClassification)
				})
		tags.append({
					'Key'  : 'Environment',
					'Value': str(self.Environment)
				})
		tags.append({
					'Key'  : 'Resource Owner',
					'Value': str(self.ResourceOwner)
				})
		tags.append({
					'Key'  : 'Cisco Mail Alias',
					'Value': str(self.CiscMailAlias)
				})
		tags.append({
					'Key'  : 'Data Taxonomy',
					'Value': str(self.DataTaxonomy)
				})
		tags.append({
					'Key'  : 'Application Name',
					'Value': str(self.AppName)
				})
		
		return tags