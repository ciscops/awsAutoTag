#from utils_logging import apilogging
from webexteamssdk import webexteamssdkException
from os import environ
from .utils_teams import teams_api
import json



def newDeviceMessage(device):

    msg = (
        f"New {device['manufacturer']} device has been received from inventory\n"
        f"Model Number: {device['model_number']}\n"
        f"Serial Number: {device['serial']}\n"
        f"Location: {device['location']}\n"
        f"If you would to deply this device to DNAC please replay: /yes:{device['id']}")
    #apilogging.debug(msg)
    try:
        #apilogging.debug(
         #   f"Token: {environ['TEAMS_USERS']}")

        #teams_api.messages.create(roomId=os.environ['TEAMS_BOT_ROOM_ID'],
        #						  text=msg)
        for email in json.loads(environ['TEAMS_USERS']):
            teams_api.messages.create(toPersonEmail=str(email),text=msg)
        return True
    except webexteamssdkException as e:
        #apilogging.debug(f"Message Failed for going to teams: {str(e)}")
        return False

def newDeviceSendCard(attachment):
    for email in json.loads(environ['TEAMS_USERS']):
      try:
          status=teams_api.messages.create(toPersonEmail=str(email),text="Issue", attachments=[attachment])
      except Exception as e:
          print(str(e))
    return True