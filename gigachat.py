import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={
  'scope': 'GIGACHAT_API_PERS'
}

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Basic MDFiMGJiZjMtM2I5ZC00ZDNjLWJkYzEtY2EzNjU5ZTI4Y2Y2OjJiODZjOGI2LWMxMmQtNDZlMS04MGJkLWVjNDMwZmM2ZTI2ZA=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.ur)
print(response.text)
