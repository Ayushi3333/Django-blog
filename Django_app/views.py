from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
	  my_title = "Hello hey there......." 
	  return render(request, "base.html", {"title": my_title})

def about_page(request):
		return render(request, "about.html", {"title": "About"})

def contact_page(request):
		form = ContactForm(request.POST or None)
		if form.is_valid():
				print(form.cleaned_data)
				form = ContactForm()
		context = {
				"title": "Contact us", 
				"form": form
		}
		return render(request, "form.html", context)