import requests

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRS0QiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYwMDc0MjQ0LCJpYXQiOjE2NTk0Njk0NDR9.a0I8ag4s9xNTxSl4nCLiNjC7cYA88j5A9Fi6ruU9XcA"
acturl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-02.json"
header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token)}

resp = requests.get(acturl, headers=header).json()

print(resp)
