from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from RFI.models import Profile, Contact
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['client_name', 'client_address','client_address2', 'email', 'info_requested', 'phone_number', 'client',
		'project_name', 'rfi', 'user', 'description', 'response', 'user_signature', 'client_signature']
	
	project_name = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': 'Project Name'
		}))
	client_name = forms.CharField(required = False, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Name]',
			'style' : 'width:100%'
		}))
	client_address = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Address 1]',
			'style' : 'width:100%',
			'required' : True,

		}))
	client_address2 = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Address 2]',
			'style' : 'width:100%',
		}))
	phone_number = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder' : '[Phone Number]',
			'style' : 'width:100%'
		}))
	email = forms.EmailField(widget=forms.TextInput(
		attrs={
			'placeholder' : '[Email]',
			'style' : 'width:100%'
		}))
	today_date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
	rfi = forms.CharField(widget=forms.TextInput(
		attrs={
			'style' : 'width:60%'
		}))
	user = forms.CharField(widget=forms.TextInput())
	client = forms.CharField(widget=forms.TextInput())
	info_requested = forms.CharField(widget=forms.Textarea(
		attrs={
			'class' : 'textInfo'
		}))
	description = forms.CharField(widget=forms.Textarea(
		attrs={
			'style':'width:100%'
		}))
	response = forms.CharField(widget=forms.Textarea(
		attrs={
			'style':'width:100%'
		}))
	user_signature = forms.CharField(widget=forms.TextInput())
	client_signature = forms.CharField(widget=forms.TextInput())
	user_date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
	client_date = forms.DateTimeField(widget=forms.DateTimeInput(
		attrs={
			'type' : 'date'
		}))