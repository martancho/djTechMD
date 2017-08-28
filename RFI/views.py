from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .models import Profile, Contact
from .forms import UserForm, ProfileForm, ContactForm

@login_required
def Home(request):
    return render(request, 'RFI/home.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'RFI/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
	title = 'Welcome'
	form = ContactForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("client_name")
		form_client_address = form.cleaned_data.get("client_address")
		form_client_address2 = form.cleaned_data.get("client_address2")
		form_message = form.cleaned_data.get("info_requested")
		form_project_name = form.cleaned_data.get("project_name")
		form_phone_number = form.cleaned_data.get("phone_number")
		form_client = form.cleaned_data.get("client")
		subject = "Tech MD inc contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "The client %s: asked about %s via %s from %s"%(form_full_name, 
			form_message,
			form_client_address, 
			from_email)
		context={
			"title":"Thank you"
		}
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)

		instance.save()	

	return render(request, "RFI/rfiForm.html", context)