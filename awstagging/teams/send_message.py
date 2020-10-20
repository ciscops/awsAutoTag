import json
import logging
from os import environ
from webexteamssdk import webexteamssdkException
from teams.utils_teams import teams_api

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def replay(msg, email):

    try:
        teams_api.messages.create(toPersonEmail=email, text=msg)
        return True
    except webexteamssdkException as e:
        logger.info("Message Failed for going to teams:%s ", str(e))
        return False


def send_all(msg):
    try:
        for email in json.loads(environ['TEAMS_USERS']):
            teams_api.messages.create(toPersonEmail=email, text=msg)
        return True
    except webexteamssdkException as e:
        logger.info("Message Failed for going to teams: %s", str(e))
        return False


def replay_card(attachment, email):
    try:
        teams_api.messages.create(toPersonEmail=email, attachments=[attachment], text="Test")
        return True
    except webexteamssdkException as e:
        logger.info("Message Failed for going to teams: %s", str(e))
