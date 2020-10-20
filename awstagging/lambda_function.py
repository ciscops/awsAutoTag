from __future__ import print_function
import logging
from tagging import tag
from model.cloud_trail import Event
from model.taginfo import InstanceTag
from teams.create_card import template_card
from teams.send_message import replay_card
from os import getenv
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run_tagging(event):
    """
    Check Tagging Event function
    :param event: Obj
    :return:
    """
    try:
        if event.ids:
            for resourceid in event.ids:
                i = resourceid.split('-')
                if i[0] == "i":
                    tags = InstanceTag(user=event.user, appname=event.appname, itemid=resourceid)

                    print('Tagging resource %s', resourceid)
                    attachment = template_card("tagcard.json", tags)
                    replay_card(attachment=attachment, email=event.user)
                    tag(tags=tags, region=event.region)
        return True
    except Exception as e:
        logger.error('Something went wrong: %s', str(e))
        return False


def lambda_handler(request, context):
    try:
        event = Event(request)
        logger.info('principalId: %s', str(event.principal))
        logger.info('region: %s', str(event.region))
        logger.info('eventName: %s', str(event.eventname))

        if not event.response_elements:
            logger.warning('Not responseElements found')
            if event.errorcode:
                logger.error('errorCode: %s', str(event.errorcode))
            if event.errormessage:
                logger.error('errorMessage: %s', str(event.errormessage))
            return False

        if event.runinstance:
            event.get_instsance_ids()

        if getenv("DEV"):
            #Check Environment for DEV and if running in DEV will only run function for users in the DEV_USER enviromnet variable
            dev_users = [getenv('DEV_USERS')]
            for user in dev_users:
                if event.user.upper() == user.upper():
                    run_tagging(event)

        else:
            run_tagging(event)

        logger.info(' Remaining time (ms): %s', str(context.get_remaining_time_in_millis()) + '\n')
        return True
    except Exception as e:
        logger.error('Something went wrong: %s', str(e))
        return False
