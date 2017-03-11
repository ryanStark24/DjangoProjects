

from django.views import generic
from .models import College
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from .forms import UserForm
from django.views.generic.base import View

from django.http.response import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Hello")

class MyList(generic.ListView):
    template_name='index.html'
    context_object_name='nl'
    def get_queryset(self):
        return College.objects.order_by('cr_date')
   
class DetailView(generic.DetailView):
    model=College
    template_name='detail.html'
    context_object_name='nl'



def About(request):
    return render(request,"about.html")
def logged(request):
    return render(request,"loggedin.html")
   
class collegeCreate(generic.CreateView):
    model=College
    fields='__all__'
    
class UserFormView(View):
    form_class=UserForm
    template_name="signup.html"
    
    #Balnk Form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    
    
    #data processing
    def post(self,request):
        form=self.form_class(request.POST)
        
        if form.is_valid():
            
            user= form.save(commit=False)
            
            #Normalised Data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            
            user.save()
            
            #Login And authenticate
            
            user=authenticate(username=username,password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('college:index')
            
            
    
        return render(request,self.template_name,{'form':form})
