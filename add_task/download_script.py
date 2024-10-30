import requests
from pprint import pprint

acces_token = "y0_AgAAAABN5P5UAAys-gAAAAEWGZpxAABSn7qRGehGmrJTcTMJZ_S7U9DNwA"
url = "https://disk.yandex.ru/i/1wH1wbV0ooi0jQ"

base_url2 = "https://cloud-api.yandex.net/v1/disk/resources/download?"

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

def download_file(file_url: str, filename: str):
	global base_url
	filepath = '/downloads/'
	final_url = f'{base_url}public_key={file_url}'

	response = requests.get(final_url)
	pprint(response.json())

	download_url = response.json()['href']
	response = requests.get(download_url)

	with open(f'{filepath}/{filename}', 'wb') as f:
	    f.write(response.content)



def download_file_token(file_url: str, filename: str, acces_token: str):
	global base_url
	filepath = '/downloads/'
	final_url = f'{base_url2}public_key={file_url}'

	headers = {
		"Authorization": acces_token
	}

	params = {
		"path": file_url
	}

	response = requests.get(final_url, headers=headers, params=params)
	pprint(response.json())

	# download_url = response.json()['href']
	# response = requests.get(download_url)

	# with open(f'{filepath}/{filename}', 'wb') as f:
	#     f.write(response.content)


download_file_token("files/Sirius/videopayback.mp4", "eqeqeq", acces_token)
