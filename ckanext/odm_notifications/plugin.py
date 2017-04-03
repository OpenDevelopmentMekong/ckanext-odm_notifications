import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

import ckanext.odm_notifications.logic.action.create

log = logging.getLogger(__name__)

class OdmNotificationsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    def __init__(self, *args, **kwargs):
        log.debug('OdmNotificationsPlugin init')

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'odm_notifications')

    # IActions
    def get_actions(self):
        return {
            'user_create':
            ckanext.odm_notifications.logic.action.create.user_create,
        }
