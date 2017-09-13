import traceback
import pylons
from pylons import config
from logging import getLogger
import ckan.model as model
import ckan.lib.helpers as h
from ckan.lib.base import render
from ckan import logic
from ckan.logic import action
from genshi.template.text import NewTextTemplate
from ckan.lib.mailer import mail_recipient
import threading

log = getLogger(__name__)

role_mapper ={'Admin':'admin','Editor':'reader'}

def notify_user_created(context,user):

    extra_vars = {
      'username': user['name'],
      'email': user['email']
    }

    # retrieve all users
    all_organizations = action.get.organization_list(context,data_dict={})
    for organization in all_organizations:

        organization_members = action.get.member_list(context,data_dict={'id':organization,'object_type':'user','capacity':'admin'})

        admins = dict()
        for admin_user in organization_members:

            admin_obj = model.User.get(admin_user[0])
            admin_name = admin_obj.name
            admin_email = admin_obj.email
            admins[admin_name] = admin_email

        for name, email in admins.iteritems():

            try:
                email_msg = render("email/user_created.txt",extra_vars=extra_vars,loader_class=NewTextTemplate)
                send_email(name,email,email_msg,"User created")

            except logic.NotFound:

                log.error("user %s not found",user['name'])

def notify_fill_form(context,user):

    extra_vars = {
      'username': user['name'],
      'email': user['email']
        }

    try:
        email_msg = render("email/fill_form.txt",extra_vars=extra_vars,loader_class=NewTextTemplate)
        send_email(user['name'],user['email'],email_msg,"Welcome to the Open Development Mekong Datahub")

    except logic.NotFound:

        log.error("user %s not found",user['name'])

def send_email(contact_name,contact_email,email_msg,subject):

  log.debug("send_email to %s %s",contact_name,contact_email)

  headers = {}
  # if cc_email:
  #     headers['CC'] = cc_email

  try:

    mail_recipient(contact_name, contact_email,subject,email_msg, headers=headers)

  except Exception:

    traceback.print_exc()
    log.error('Failed to send an email message for issue notification')
