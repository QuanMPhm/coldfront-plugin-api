'''
Defines the SCIM adapter for coldfront users and groups
'''

from django_scim.adapters import SCIMUser, SCIMGroup

class SCIMColdfrontUser(SCIMUser):
    id_field = "id"
