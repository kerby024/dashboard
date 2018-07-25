# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def registration_validation(self, data):
        errors = {}
        if len(data['f_name']) < 2:
            errors['first_name'] = 'First name is incorrect'
        
        if not data['password'] == data['confirm']:
            errors['password'] = 'Passwords do not match'

        if len(errors) == 0:
            # print 'NO ERRRROOORRSSS'
            level = 'admin' #admin
            if len(self.all()) > 0:
                level = 'normal' #normal
            self.create(first_name=data['f_name'], last_name=data['l_name'], email_address=data['email'], password=data['password'], desc='', user_level=level)
        else:
            # print 'ERRRORS'
            return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    user_level = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return '<USER: {} {} {}>'.format(self.first_name, self.last_name, self.email_address)

