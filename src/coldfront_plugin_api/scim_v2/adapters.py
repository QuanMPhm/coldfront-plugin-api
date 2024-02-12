'''
Defines the SCIM adapter for coldfront users and groups
'''

from django_scim.adapters import SCIMUser, SCIMGroup
from django_scim import constants

from coldfront_plugin_api import auth, utils

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
                "created": self.obj.date_joined.isoformat(),
            },
        }

        return d

    def from_dict(self, d):

        '''
        Overide from SCIMUser, this function first check if user exists through one of 
        the configured search providers, and if yes, will fetch additional information from there.

        Otherwise, for setting the attributes manually from the request's payload
        '''
        username = d.get('userName')
        found = utils.find_user(username) # Fetch user

        # If the user is not found in the search provider,
        # allow the API client to specify the values that would have
        # otherwise been fetched.
        # This allows preregistering a user that doesn't have a corresponding
        # identity provider yet.
        if found:
            self.obj.username = username
            self.obj.first_name = found["first_name"]
            self.obj.last_name = found["last_name"]
            self.obj.email = found["email"]
        else:
            super().from_dict(d)