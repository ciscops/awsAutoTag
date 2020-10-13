from __future__ import print_function
import json
import boto3
import logging
import time
import datetime
import teams.utils_teams
from model.cloud_trail import Event
from model.taginfo import InstanceTag
from teams.send_message import replayCard
from teams.createCard import staticNewInstance
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
			
		if event.ids:
			inst = InstanceTag(user=event.user, AppName=event.appName)
			tags = inst.getTags()
			for resourceid in event.ids:
				i = resourceid.split('-')
				if i[0] == "i":
					print('Tagging resource ' + resourceid)
					attachment = staticNewInstance(tags=inst,instanceid=resourceid)
					replayCard(attachment=attachment,email=event.user,msg='Card Error')
					tag(resourceId=resourceid,region=event.region,tag=tags)
		
		logger.info(' Remaining time (ms): ' + str(
			context.get_remaining_time_in_millis()) + '\n')
		return True
	except Exception as e:
		logger.error('Something went wrong: ' + str(e))
		return False
	


