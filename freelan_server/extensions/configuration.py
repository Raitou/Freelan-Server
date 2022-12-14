"""
Configuration related information.
"""

import os

import M2Crypto as m2
from M2Crypto import BIO

def register_configuration_information(app):
    """
    Register configuration information.
    """

    authority_certificate_file = app.config['AUTHORITY_CERTIFICATE_FILE']
    authority_private_key_file = app.config['AUTHORITY_PRIVATE_KEY_FILE']

    if 'FREELAN_SERVER_CONFIGURATION_FILE' in os.environ:
        base_path = os.path.abspath(os.path.dirname(os.environ['FREELAN_SERVER_CONFIGURATION_FILE']))

        if not os.path.isfile(authority_certificate_file) and not os.path.isabs(authority_certificate_file):
            authority_certificate_file = os.path.join(base_path, authority_certificate_file)

        if not os.path.isfile(authority_private_key_file) and not os.path.isabs(authority_private_key_file):
            authority_private_key_file = os.path.join(base_path, authority_private_key_file)

    authority_private_key_passphrase = app.config['AUTHORITY_PRIVATE_KEY_PASSPHRASE'] or ''

    try:
        # Below is a hack that allow loading of trusted certificates
        # I don't like it but it seems M2Crypto doesn't provide a way for
        # loading those, so we don't really have a choice.
        
        membuf = BIO.MemoryBuffer(open(authority_certificate_file, 'r').read().replace(' TRUSTED', ''))
           
        authority_certificate = m2.X509.load_cert_bio(
            membuf,
            m2.X509.FORMAT_PEM
        )
        authority_certificate_error = None

    except (IOError, m2.X509.X509Error) as ex:
        authority_certificate = None
        authority_certificate_error = str(ex)

    try:
    
        membuf = BIO.MemoryBuffer(open(authority_private_key_file, 'r').read())
        authority_private_key = m2.RSA.load_key_bio(
            membuf,
            callback=(lambda v: authority_private_key_passphrase or '')
        )
        authority_private_key_error = None

    except (IOError, m2.RSA.RSAError) as ex:
        authority_private_key = None
        authority_private_key_error = str(ex)

    app.config['AUTHORITY_CERTIFICATE'] = authority_certificate
    app.config['AUTHORITY_CERTIFICATE_ERROR'] = authority_certificate_error
    app.config['AUTHORITY_PRIVATE_KEY'] = authority_private_key
    app.config['AUTHORITY_PRIVATE_KEY_ERROR'] = authority_private_key_error
