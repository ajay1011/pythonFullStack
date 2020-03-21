from django.shortcuts import render
from .models import Contact
import requests
import json
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    # check post method and request type

    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'myapp/index.html', context)
    else:

        return render(request,'myapp/index.html')

def portfolio(request):
    return render(request,'myapp/portfolio.html')

def contact(request):
    if request.method  == "POST":
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email = email_r,subject = subject_r,message = message_r)
        c.save()
        print("message saved")
        print("sending mail")
        send_mail('NoRply','Thanks for response','ajayjedhe1011@gmail.com',[email_r,],fail_silently=False)
        print("mail sent")
        context={
                 "success_report":"Message Sent Successfully",
                 }
        return render(request,'myapp/thankyou.html',context=context)
    else:
        return render(request,'myapp/contact.html')
