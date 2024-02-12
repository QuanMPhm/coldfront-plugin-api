'''
Defines the SCIM filters for coldfront users and groups
'''

from django_scim.filters import UserFilterQuery, GroupFilterQuery
from django_scim import constants
from django_scim.utils import get_user_model

class ColdfrontUserFilterQuery(UserFilterQuery):
    model_getter = get_user_model
    attr_map = {
        # attr, sub attr, uri
        ('userName', None, None): 'username',
        ('name', 'familyName', None): 'last_name',
        ('familyName', None, None): 'last_name',
        ('name', 'givenName', None): 'first_name',
        ('givenName', None, None): 'first_name',
        ('emails', 'value', None): 'email'  # Current implementation means each user only have 1 email
    }