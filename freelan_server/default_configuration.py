"""
The default configuration.
"""

import os
import tempfile
from datetime import timedelta

# The host to listen on.
HOST = '193.247.144.254'

# Whether to enable debug mode.
DEBUG = False

# Enable or disable the register option.
#
# If you decide to enable it, you probably should setup a recaptcha to prevent
# spam.
REGISTER_ENABLED = True

# The authority certificate file.
#
# An absolute path to the authority certificate file.
AUTHORITY_CERTIFICATE_FILE = 'C:\Users\Administrator\Desktop\cert\crt\ca.crt'

# The authority private key file.
#
# An absolute path to the authority private key file.
AUTHORITY_PRIVATE_KEY_FILE = 'C:\Users\Administrator\Desktop\cert\key\ca.key'

# The authority private key passphrase.
#
# If no passphrase is required, specify None.
AUTHORITY_PRIVATE_KEY_PASSPHRASE = 'A9020andi0n2aAUU@*8uajsdija290djasofn0a9s'

# The issued certificate validity duration.
CERTIFICATE_VALIDITY_DURATION = timedelta(days=3)

# The network membership duration.
NETWORK_MEMBERSHIP_VALIDITY_DURATION = timedelta(days=3)

# The database URI.
#
# For real installations, you probably want to change the target directory to a
# more permanent location or to change the database provider to something more
# production-suited.
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(
    tempfile.gettempdir(),
    'freelan_server.db'
)

# The secret key used for session securing.
#
# This key *MUST* be changed and kept secret !
#
# Failing to do so would allow anyone to steal sessions and you don't want
# that, do you ?
SECRET_KEY =  '12094asjfkasn0#$&qusa0!@(#2aoi09299j0adsa'

# Recaptcha settings.
#
# You may set those to add a captcha to the login and registration forms.
#RECAPTCHA_USE_SSL = False
#RECAPTCHA_PUBLIC_KEY = '6LeiVJUhAAAAAD6-gEt4wzE9CKY7DUOGRHoDxge8'
#RECAPTCHA_PRIVATE_KEY = '6LeiVJUhAAAAAN_SUwJ1FCOg42M9i_7Yjg6wdpZI'
#RECAPTCHA_OPTIONS = {'theme': 'white'} 
# ABSOLUTELY dont use this - move to main.py


SQLALCHEMY_TRACK_MODIFICATIONS = False