from __future__ import print_function
import json
import boto3
import logging
import time
import datetime
from model.cloud_trail import Event
from model.taginfo import InstanceTag
from tagging import tag
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(request, context):
	# logger.info('Event: ' + str(event))
	# print('Received event: ' + json.dumps(event, indent=2))
	
	ids = []
	
	try:
		event = Event(request)
		logger.info('principalId: ' + str(event.principal))
		logger.info('region: ' + str(event.region))
		logger.info('eventName: ' + str(event.eventname))
		
		if not event.responseElements:
			logger.warning('Not responseElements found')
			if event.errorCode:
				logger.error(f'errorCode: {str(event.errorCode)}')
			if event.errorMessage:
				logger.error(f'errorMessage: {str(event.errorMessage)}')
			return False
		
		if event.runInstance:
			event.getInstsanceIds()
			
		if ids:
			for resourceid in event.ids:
				print('Tagging resource ' + resourceid)
				inst = InstanceTag(user=event.user,AppName=event.appName)
				tags = inst.getTags()
				tag(resourceid=resourceid,region=event.region,tag=tags)
		
		logger.info(' Remaining time (ms): ' + str(
			context.get_remaining_time_in_millis()) + '\n')
		return True
	except Exception as e:
		logger.error('Something went wrong: ' + str(e))
		return False
	


