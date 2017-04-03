#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True

import pylons
import json
import ckan
import logging
import urlparse
import genshi
import datetime
import re
import uuid
import os
import ckan.model as model
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
from ckan.plugins.toolkit import Invalid

import ckan.lib.navl.dictization_functions as df
missing = df.missing

log = logging.getLogger(__name__)

def helper_function_1(pkg_info):
	''' TBD'''
