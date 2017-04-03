import traceback
import pylons
from pylons import config
from logging import getLogger
import ckan.model as model
import ckan.lib.helpers as h
from ckan.lib.base import render
from ckan.logic import action
from genshi.template.text import NewTextTemplate
from ckan.lib.mailer import mail_recipient
import threading

log = getLogger(__name__)

role_mapper ={'Admin':'admin','Editor':'reader'}

def notify_user_created(context,user):

  notify(context,user,"email/user_created.txt")

def notify(context,user,email_template):

  # retrieve all users
  all_organizations = action.get.organization_list(context,data_dict={})
  for organization in all_organizations:

      organization_details = action.get.organization_show(context,data_dict={'id':organization})

      if 'users' in organization_details:
          for potential_admin_user in organization_details['users']:

            if potential_admin_user['capacity'] == 'admin':

              admin_user = model.User.get(potential_admin_user['id'])
              admin_name = admin_user.name
              admin_email = admin_user.email

              email_msg = render(email_template,extra_vars=extra_vars,loader_class=NewTextTemplate)
              send_email(admin_name,admin_email,email_msg)

def send_email(contact_name,contact_email,email_msg):

  log.debug("send_email to %s %s",contact_name,contact_email)

  headers = {}
  # if cc_email:
  #     headers['CC'] = cc_email

  try:

    mail_recipient(contact_name, contact_email,"User created",email_msg, headers=headers)

  except Exception:

    traceback.print_exc()
    log.error('Failed to send an email message for issue notification')
