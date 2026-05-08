# forms.py

from django import forms
from captcha.fields import CaptchaField

from .models import *


class ContactForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:

        model = Contact

        fields = [
            'name',
            'email',
            'phone_number',
            'subject',
            'message',
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter message',
                'rows': 5
            }),
        }


class ContactUpdateForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = [
            'name',
            'email',
            'phone_number',
            'subject',
            'message',
            'status',
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

class ServiceForm(forms.ModelForm):

    class Meta:

        model = Service

        fields = [
            'title',
            'short_description',
            'description',
            'image',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter service title'
            }),


            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Short description'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Full description'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class GalleryForm(forms.ModelForm):

    class Meta:

        model = Gallery

        fields = [
            'title',
            'image',
            'category',
            'description',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),


            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter description'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class OfferForm(forms.ModelForm):

    class Meta:

        model = Offer

        fields = [
            'title',
            'image',
            'discount',
            'description',
            'start_date',
            'end_date',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),


            'discount': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),

            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class LatestUpdateForm(forms.ModelForm):

    class Meta:

        model = LatestUpdate

        fields = [
            'title',
            'image',
            'short_description',
            'description',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }