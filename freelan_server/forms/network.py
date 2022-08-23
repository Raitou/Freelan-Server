"""
The network form.
"""
from wtforms import TextField, FormField, BooleanField, validators, FieldList
from flask_wtf import Form
from freelan_server.extensions.fields import ConstantField, IPTextField

class NetworkMemberForm(Form):
    """
    The network member form.
    """
    user_id = ConstantField('Identifier')
    username = ConstantField('Name')
    email = ConstantField('Email')
    is_member = BooleanField('Is member')
    ipv4_address = IPTextField('IPv4 address', ip_version=4, network_only=False)
    ipv6_address = IPTextField('IPv6 address', ip_version=6, network_only=False)

class NetworkForm(Form):
    """
    The network form.
    """
    name = TextField('Name', [validators.Required(), validators.Length(min=1, max=80)])
    ipv4_address = IPTextField('IPv4 network', ip_version=4, network_only=True)
    ipv6_address = IPTextField('IPv6 network', ip_version=6, network_only=True)
    members = FieldList(FormField(NetworkMemberForm))
