import logging
from ckan.logic.action.create import user_create as ckan_user_create

from ...lib import notification

log = logging.getLogger(__name__)

def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    log.debug('User %s has been created, sending notification to admin users', user['name'])

    try:
        notification.notify_user_created(context,user)
    except Exception as e:
        log.error("Exception notifying admins of new user: %s" % e)

    try:
        notification.notify_fill_form(context,user)
    except Exception as e:
        log.error("Exception welcoming new user: %s" %e)

    return user
