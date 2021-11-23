# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    Branch,
    Bank
)

# Register your models here.
admin.site.register(Branch)
admin.site.register(Bank)

