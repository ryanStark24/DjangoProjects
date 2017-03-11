from django.conf.urls import url
from college import views
from django.contrib.auth import views as auth_views



urlpatterns = [
     url('^home/$', views.hello, name='home'),
    url('^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^signup/', views.UserFormView.as_view(), name='signup'),
    url(r'^create/$', views.collegeCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update$', views.collegeUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.collegeDelete.as_view(), name='delete'),
    url(r'^loggedin/$', views.logged, name='loggedin'),
    url(r'^about/$', views.About, name='about'),
    url(r'^login/$', views.login_user,name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'college:index'}, name='logout'),
   
]
