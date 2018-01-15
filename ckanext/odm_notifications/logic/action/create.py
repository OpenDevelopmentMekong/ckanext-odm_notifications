import ckan
import pylons
import logging

import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.plugins.toolkit as toolkit

from ckanext.odm_notifications.lib import notification

log = logging.getLogger(__name__)

def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    log.debug('User %s has been created, sending notification to admin users', user['name'])

    notification.notify_user_created(context,user)

    notification.notify_fill_form(context,user)

    return user
