# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def index(request):

	# if request.method == 'POST':
	# 	message = request.POST['message']
	

	# 	send_mail('Contact Form',
	# 	 message, 
	# 	 settings.EMAIL_HOST_USER,
	# 	 ['chepsharonmaswai@gmail.com'], 
	# 	 fail_silently=False)
	
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			phone_number = form.cleaned_data['phone_number']
			from_email = form.cleaned_data['from_email']
			name = form.cleaned_data['name']
			# phone_number = form.cleaned_data['name']
			# current_home= form.cleaned_data['name']
			# new_home = form.cleaned_data['new_home']
			#bedrooms = form.cleaned_data['bedrooms']
			# moving_date = form.cleaned_data['moving_date']
			try:
				send_mail(phone_number, name, from_email, ['chepsharonmaswai@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('alert')

	return render(request, 'index.html', {'form': form})
def alert(request):

    return render(request, 'alert.html')    
 