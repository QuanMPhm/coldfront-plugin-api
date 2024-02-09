'''
Defines the SCIM adapter for coldfront users and groups
'''

from django_scim.adapters import SCIMUser, SCIMGroup
from django_scim import constants

class SCIMColdfrontUser(SCIMUser):
    id_field = "id"

    def to_dict(self):

        d = {
            'schemas': [constants.SchemaURI.USER],
            "id": self.obj.username,
            "externalId": self.obj.username,
            "userName": self.obj.username,
            "name": {
                "givenName": self.obj.first_name,
                "familyName": self.obj.last_name,
            },
            "emails": [
                {
                    "value": self.obj.email,
                    "type": "work",
                    "primary": True,
                }
            ],
            "meta": {
                "resourceType": "User",
                "created": self.obj.date_joined,
            },
        }

        return d
