import re

from django import forms
from django.contrib import messages
from django.core.validators import RegexValidator
from django_jalali.admin.widgets import AdminjDateWidget, AdminSplitjDateTime
from django_jalali.forms import jDateField, jDateTimeField

from users.models import CustomUser


class CustomUserForm(forms.ModelForm):

    national_code = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="National code must be exactly 10 digits."
            )
        ]
    )

    birthday_date = jDateField(
        input_formats=['%Y/%m/%d'],  # match the JS datepicker format
        widget=forms.TextInput(attrs={'class': 'jalali_date'})
    )
    ceremony_datetime = jDateTimeField(
        input_formats=['%Y/%m/%d %H:%M'],  # match datetime format from JS
        widget=forms.TextInput(attrs={'class': 'jalali_datetime'})
    )


    class Meta:
        model = CustomUser
        fields = (
            'username',
            'full_name',
            'gender',
            'national_code',
            'birthday_date',
            'ceremony_datetime',
            'country',
        )

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']

        parts = full_name.strip().split(' ')
        if len(parts) != 2:
            raise forms.ValidationError("Full name must be exactly 2 digits.")

        for part in parts:
            if not re.match(r'^[A-Z][a-z]+$', part):
                raise forms.ValidationError("Each part of the name must start with a capital letter and the rest lowercase.")

        return full_name
