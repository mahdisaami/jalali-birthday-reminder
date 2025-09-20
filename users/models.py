from datetime import date

from django_jalali.db import models as jmodels
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(models.Model):
    M = 'Male'
    F = 'Female'

    CHOICES = (
        (M, _('Male')),
        (F, _('Female')),
    )

    username = models.CharField(_('username'), max_length=256)
    full_name = models.CharField(_('full name'), max_length=256)
    gender = models.CharField(_('gender'), choices=CHOICES)
    national_code = models.CharField(_('national code'), max_length=10)
    birthday_date = jmodels.jDateField(_('birthday date'))
    ceremony_datetime = jmodels.jDateTimeField(_('ceremony datetime'))
    country = models.CharField(default='Iran', max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_first_and_last_name(self):
        full_name = self.full_name.split()
        first_name = full_name[0]
        last_name = full_name[-1]
        return {'first_name': first_name, 'last_name': last_name}

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year
        if today.month < self.birthday_date.month:
            age -= 1
        return age

    def is_birthday(self):
        today = date.today()
        if self.birthday_date.month == today.month and self.birthday_date.day == today.day:
            return True
        return False




class Birthday(models.Model):
    pass