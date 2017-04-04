# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
import sys, os

version = '1.0.1'

setup(
    name='''ckanext-odm?notifications''',
    version=version,
    description='''CKAN plugin to notify admin users about certain events ocured on a ckan instance.''',
    url='https://github.com/OpenDevelopmentMekong/ckanext/odm_notifications',
    author='Alex Corbi',
    author_email='mail@lifeformapps.com',
    license='AGPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='''CKAN user notifications''',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    package_data={
    },
    data_files=[],
    entry_points='''
        [ckan.plugins]
        odm_notifications=ckanext.odm_notifications.plugin:OdmNotificationsPlugin
    '''
)
