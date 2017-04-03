ckanext-odm_notifications
===================

CKAN plugin to notify admin users about certain events ocured on a ckan instance.


Tested with CKAN v2.5.2

# Installation

In order to install this CKAN Extension:

  * clone the ckanext-odm_notifications folder to the src/ folder in the target CKAN instance.

 ```
 git clone --recursive https://github.com/OpenDevelopmentMekong/ckanext-odm_notifications.git
 cd ckanext-odm_notifications
 ```

 * Install dependencies
 <code>pip install -r requirements.txt</code>

 * Setup plugin
 <code>python setup.py develop</code>

# Testing

Tests are found on ckanext/odm_notifications/tests and can be run with ```nosetest```

# Copyright and License

This material is copyright (c) 2014-2015 East-West Management Institute, Inc. (EWMI).

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

http://www.fsf.org/licensing/licenses/agpl-3.0.html

# Credits

Originally forked and adapted from https://github.com/aptivate/ckanext-userautoadd
