import ckan.model as model
from ckan.plugins import toolkit

import logging
log = logging.getLogger(__name__)

def notify_user_created(context,user):
    extra_vars = {
      'username': user['name'],
      'email': user['email']
    }

    # retrieve all users
    admins = {}

    user_orgs = toolkit.get_action('organization_list_for_user')(context, {'id':user['id']})
    # add the admins of the user's groups.
    for organization in user_orgs:
        admin_members = toolkit.get_action('member_list')(context,
                                                                 data_dict={'id':organization,
                                                                            'object_type':'user',
                                                                            'capacity':'admin'})
        for admin_user in admin_members:
            admin_obj = model.User.get(admin_user[0])
            admin_name = admin_obj.name
            admin_email = admin_obj.email
            admins[admin_name] = admin_email

    # add all the sysadmins
    sysadmins = model.Session.query(model.User).filter_by(sysadmin=True, state='active')
    for admin in sysadmins:
        admins[admin.name] = admin.email

    for name, email in admins.items():
        email_msg = toolkit.render("email/user_created.txt",extra_vars=extra_vars)
        send_email(name, email, email_msg, "User created")

def notify_fill_form(context,user):
    extra_vars = {
      'username': user['name']
    }

    email_msg = toolkit.render("email/fill_form.txt",extra_vars=extra_vars)
    send_email(user['name'],
               user['email'],
               email_msg,
               "Welcome to the Open Development Mekong Datahub")


def send_email(contact_name,contact_email,email_msg,subject):
    log.debug("send_email to %s %s",contact_name,contact_email)

    headers = {}
    # if cc_email:
    #     headers['CC'] = cc_email

    try:
        toolkit.mail_recipient(contact_name, contact_email, subject, email_msg, headers=headers)
    except:
        log.exception('Failed to send an email message for issue notification') 
