from ckan import plugins
from ckan.plugins import toolkit

import logging

from .logic.action import create

log = logging.getLogger(__name__)

class OdmNotificationsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    # IActions
    def get_actions(self):
        return {
            'user_create': create.user_create,
        }
