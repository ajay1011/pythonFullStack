from django.shortcuts import render
from forms.forms import NewUserForm
from forms import forms

# Create your views here.

def index(request):
    return render(request,'forms/index.html')

def form_page_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print("Name: "+ form.cleaned_data['name'])
            print("Email: "+ form.cleaned_data['email'])
            print("Text "+ form.cleaned_data['text'])

    return render(request,'forms/form_page.html',{'form':form})

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return index(request)
        else:
            print("Form Invalid")
    return render(request,'forms/users.html',{'form':form})
