import requests
from bs4 import BeautifulSoup
import json

def request_function(request_url,post_param):
	r = requests.post(request_url,post_param)
	return_data = json.loads(r.text)
	return return_data