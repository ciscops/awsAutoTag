#from utils_logging import apilogging
import json
from webexteamssdk import webexteamssdkException
from .utils_teams import teams_api
from os import environ
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def replay(msg,email):
 
    try:
        teams_api.messages.create(toPersonEmail=email,
                                  text=msg)
        return True
    except webexteamssdkException as e:
        logger.info(f"Message Failed for going to teams: {str(e)}")
        return False

def send_all(msg):
    try:
        for email in json.loads(environ['TEAMS_USERS']):
            teams_api.messages.create(toPersonEmail=email,text=msg)
        return True
    except webexteamssdkException as e:
       logger.info(f"Message Failed for going to teams: {str(e)}")
       return False


def replay_card(attachment,email,msg):
    try:
        teams_api.messages.create(toPersonEmail=email,text=msg, attachments=[attachment])
        return True
    except webexteamssdkException as e:
        logger.info(f"Message Failed for going to teams: {str(e)}")
        return False
