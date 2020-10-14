from __future__ import print_function
import logging
from model.cloud_trail import Event
from model.taginfo import InstanceTag
from teams.send_message import replay_card
from teams.createCard import static_new_instance
from tagging import tag
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(request, context):
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
		
		if event.runinstance:
			event.get_instsance_ids()
			
		if event.ids:
			inst = InstanceTag(user=event.user, AppName=event.appName)
			tags = inst.get_tags()
			for resourceid in event.ids:
				i = resourceid.split('-')
				if i[0] == "i":
					print('Tagging resource ' + resourceid)
					attachment = static_new_instance(tags=inst,instanceid=resourceid)
					replay_card(attachment=attachment,email=event.user,msg='Card Error')
					tag(resourceId=resourceid,region=event.region,tag=tags)
		
		logger.info(' Remaining time (ms): ' + str(
			context.get_remaining_time_in_millis()) + '\n')
		return True
	except Exception as e:
		logger.error('Something went wrong: ' + str(e))
		return False
	


