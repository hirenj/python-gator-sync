import rumps
import keyring
import os
path = os.path.dirname(os.path.realpath(__file__))
path_to_img = '%s/pony.jpg' % path

endpoint = 'https://test.glycocode.com'

client_id = keyring.get_password('gatordata.client_id', endpoint)
client_secret = keyring.get_password('gatordata.client_secret', endpoint)

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