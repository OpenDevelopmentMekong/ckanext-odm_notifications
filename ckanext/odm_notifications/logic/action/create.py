import logging
from ckan.plugins import toolkit
from ckanext.odm_notifications.lib import notification

log = logging.getLogger(__name__)


@toolkit.chained_action
def user_create(ckan_user_create, context, data_dict):
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
