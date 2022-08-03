import requests

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRS0QiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkxMDQxNzA4LCJpYXQiOjE2NTk1MDU3MDh9.NzxJB3FZxmWDyJx44pvUZOCkqME50heLRhYWD19z1go"
acturl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-02.json"
header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token)}

resp = requests.get(acturl, headers=header).json()
summ = resp["summary"]
print("You walked {} steps today.".format(summ["steps"]))
