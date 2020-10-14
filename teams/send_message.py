#from utils_logging import apilogging
import json
from webexteamssdk import webexteamssdkException
from .utils_teams import teams_api
from os import environ
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def replay(msg,email):
    #apilogging.debug(msg)
    try:
        #apilogging.debug(
        #    f"Email Address: {email}\n"
        #    f"Message: {msg}")
        teams_api.messages.create(toPersonEmail=email,
                                  text=msg)
        return True
    except webexteamssdkException as e:
        #apilogging.debug(f"Message Failed for going to teams: {str(e)}")
        return False

def replaymd(msg,email):
    #apilogging.debug(msg)
    try:
        #apilogging.debug(
        #    f"Email Address: {email}\n"
        #    f"Message: {msg}")
        res=teams_api.messages.create(toPersonEmail=email,
                                  html=msg)
        return True
    except webexteamssdkException as e:
        #apilogging.debug(f"Message Failed for going to teams: {str(e)}")
        return False

def all(msg):
    #apilogging.debug(msg)
    try:
        for email in json.loads(environ['TEAMS_USERS']):
            #apilogging.debug(f"Email Address: {email}")
            teams_api.messages.create(toPersonEmail=email,text=msg)
        return True
    except webexteamssdkException as e:
        #apilogging.debug(f"Message Failed for going to teams: {str(e)}")
        return False


def replayCard(attachment,email,msg):
    try:
        teams_api.messages.create(toPersonEmail=email,text=msg, attachments=[attachment])
        return True
    except webexteamssdkException as e:
        logger.info(f"Message Failed for going to teams: {str(e)}")
        return False
