# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from api_site.settings import DBNAME

# Create your models here.
connect(DBNAME)

class Article(Document):
    title = StringField(required=True, max_length=50)
    author = StringField()
    publishtime = DateTimeField()
    lastchangetime = DateTimeField()
    content = StringField(required=True)
    tags = StringField(required=False)
