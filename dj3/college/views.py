
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import College
from django.shortcuts import render, render_to_response
from college.forms import noticeForm
from django.template.defaulttags import csrf_token
from django.template.context_processors import csrf

# Create your views here.
def hello(request):
    return HttpResponse("Hello")

class MyList(generic.ListView):
    template_name='index.html'
    context_object_name='nl'
    def get_queryset(self):
        return College.objects.order_by('cr_date')[:5]
   
class DetailView(generic.DetailView):
    model=College
    template_name='detail.html'
    context_object_name='nl'

def signup(request):
    return render(request,"signup.html")   

def create(request):
    if request.POST:
        form=noticeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/college/')
    else:
            form=noticeForm()
            args={}
            args.update(csrf(request))
            args['form']=form
            
            return render_to_response('create.html',args)
            