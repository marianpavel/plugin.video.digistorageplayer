import requests

username = 'sorin.popescu@rdslink.ro'
password = 'marius'

print(username + " " + password)

api_base = 'https://storage.rcs-rds.ro'

s = requests.Session()

# get auth token

token = s.get(api_base + '/token', headers = {
    'X-Koofr-Email': username,
    'X-Koofr-Password': password
}).headers['X-Koofr-Token']

s.headers['Authorization'] = 'Token ' + token

# get mount (Digi Cloud, Dropbox...)

mounts = s.get(api_base + '/api/v2/mounts').json()['mounts']

mount = [x for x in mounts if x['name'] == 'Digi Cloud'][0]

print(mount['name'] + mount['id'])


files = s.get(api_base + '/api/v2/mounts/' + mount['id'] + '/files/list', params = {'path': '/'}).json()["files"]
for file in files:
    if str(file['type']) == str('dir'):
        print (file['name'])
