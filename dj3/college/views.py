

from django.views import generic
from .models import College
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout

from .forms import UserForm
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from college.forms import College_Form
from django.template import context,RequestContext
from django.contrib.auth import logout

def logout_view(request):
    logout(request,next_page='college:index')

@login_required(login_url='college/login/')
def hello(request):
    return render(request,'hello.html')

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'nl'
    def get_queryset(self):
        return College.objects.order_by('cr_date')
   
class DetailView(generic.DetailView):
    model = College
    template_name = 'detail.html'
    context_object_name = 'nl'



def About(request):
    return render(request, "about.html")
def logged(request):
    return render(request, "loggedin.html")
   
class collegeCreate(generic.CreateView):
    model = College
    form_class = College_Form

class collegeUpdate(generic.UpdateView):
    model = College
    fields = '__all__'
    template_name_suffix = '_update_form' 
    
class collegeDelete(generic.DeleteView):
    model = College
    success_url = reverse_lazy('college:index')     
    
class UserFormView(View):
    form_class = UserForm
    template_name = "signup.html"
    
    # Balnk Form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    
    # data processing
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
            # Normalised Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            
            user.save()
            
            # Login And authenticate
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('college:index')
            
            
    
        return render(request, self.template_name, {'form':form})
    
    
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/college/home/')
    return render_to_response('login.html',context=RequestContext(request))


