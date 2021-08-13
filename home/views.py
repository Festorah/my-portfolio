from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):

	contact = Contact.objects.all()

	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		contact = contact.create(name=name, email=email, subject=subject, message=message)
		contact.save()


	return render(request, 'home/index.html')


def project(request):
	return render(request, 'home/inner-page.html')