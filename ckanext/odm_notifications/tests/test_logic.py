from ckanext.odm_notifications.lib import notification
from ckan.logic.action.create import user_create as ckan_user_create
from ckan.plugins import toolkit
from ckan.tests import factories
import ckan.tests.helpers as helpers
from ckan import model
from ckan import logic
from ckan.logic import _actions
import pytest
import mock
import logging

log = logging.getLogger(__name__)


def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    log.debug('User %s has been created, sending notification to admin users', user['name'])

    notification.notify_user_created(context,user)
    notification.notify_fill_form(context,user)

    return user


@pytest.mark.usefixtures("clean_db", "with_request_context")
class TestOdmNotificationsLogic:

    def setup(self):
        """
        # create dataset
        # create resource
        # create user
        # create sysadmin
        :return:
        """
        self._user = factories.User(name='admin_user')
        self._sysadmin = factories.Sysadmin()
        self.admin_context = {
            'user': self._sysadmin['name'],
            'model': model,
            'ignore_auth': False,
            "session": model.Session
        }

    def test_notification_for_user(self, monkeypatch):
        """
        Test notification for user
        :return:
        """
        def send_email(contact_name,contact_email,email_msg,subject):

            assert contact_name == "test_name"
            assert "successfully created an account on the Open" in email_msg
            assert subject == 'Welcome to the Open Development Mekong Datahub'


        monkeypatch.setitem(_actions, 'user_create', user_create)
        monkeypatch.setattr(notification, 'send_email', send_email)

        res = helpers.call_action(
            "user_create",
            context=self.admin_context,
            name="test_name",
            email="test@gmail.com",
            password="TestPassword123",
            fullname="Test Name"
        )
