import pylons.config as config

import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.plugins.toolkit as toolkit


def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    return user
