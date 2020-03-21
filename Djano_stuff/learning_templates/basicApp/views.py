from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':20}
    return render(request,'basicApp/index.html',context=context_dict)

def other(request):
    return render(request,'basicApp/other.html')

def relative(request):
    return render(request,'basicApp/relative_url_templates.html')
