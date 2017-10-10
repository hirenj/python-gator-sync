import rumps
import keyring
import os
import requests

path = os.path.dirname(os.path.realpath(__file__))
path_to_img = '%s/pony.jpg' % path

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

endpoint = 'https://test.glycocode.com'

client_id = keyring.get_password('gatordata.client_id', endpoint)
client_secret = keyring.get_password('gatordata.client_secret', endpoint)

print '%s/api/config' % endpoint

config_info = requests.get('%s/api/login/config' % endpoint )

auth0_domain = config_info.json()['AUTH0_DOMAIN']
audience = config_info.json()['API_AUDIENCE']

client = BackendApplicationClient(client_id=client_id,audience=audience)

gator = OAuth2Session(client=client)

token_uri = ('https://%s.auth0.com/oauth/token' % auth0_domain)

token = gator.fetch_token(token_url=token_uri,client_id=client_id,client_secret=client_secret,audience=audience)

gator.headers.update({'x-api-key' : client_id })

url = '%s/api/metadata' % endpoint
r = gator.get(url)

user_metadata = r.json()

rumps.debug_mode(True)

@rumps.clicked('Icon', 'On')
def a(_):
    app.icon = path_to_img

@rumps.clicked('Icon', 'Off')
def b(_):
    app.icon = None

@rumps.clicked('Title', 'On')
def c(_):
    app.title = 'Buzz'

@rumps.clicked('Title', 'Off')
def d(_):
    app.title = None

app = rumps.App('', icon='pony.jpg', quit_button=rumps.MenuItem('Quit Buzz', key='q'))
app.menu = [
    ('Icon', ('On', 'Off')),
    ('Title', ('On', 'Off'))
]
app.run()