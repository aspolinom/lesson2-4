import requests
import time
import json

nameUrl = "https://playground.learnqa.ru/ajax/api/longtime_job"
# первый запрос на получение имени токена
reasponce = requests.get(nameUrl)
answer1 = reasponce.json()
#print(reasponce.text)
name_token = answer1['token']
time_delay = answer1['seconds']
token_ask = {"token":name_token}
# повторный запрос на считку окончания процесса и результата
time.sleep(time_delay)
reasponce = requests.get(nameUrl,params=token_ask)

answer2 = reasponce.json()
key_result = "result"

if key_result in answer2:
    if answer2['status'] == 'Job is ready':
        print('Ответ с результатом:')
        print(reasponce.text)
    else:
        print('Расчет не закончен')
else:
    print('Результат не получен')