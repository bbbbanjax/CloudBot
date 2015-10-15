from cloudbot import hook
from datetime import datetime
import requests

api_url = "http://api.icndb.com/jokes/random"

@hook.command('bam', autohelp=False)
def bam(text, nick='', db=None, bot=None, notice=None):

	response = []
	
	name = nick
	
	if text:
		name = text
	
	params = {'firstName': name, 'lastName': "~"}
		
	request = requests.get(api_url, params)
	
	response = request.json()
	
	if response["type"] == "success":
		bam = response["value"]["joke"].replace("{} ~".format(name), "{}".format(name)).replace("'s", "")
		return bam
	else:
		return u"There was a problem, sorry {}".format(nick)