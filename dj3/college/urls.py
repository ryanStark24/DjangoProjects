from django.conf.urls import url
from college import views


urlpatterns=[
    
    url('^$',views.MyList.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^signup/',views.UserFormView.as_view(),name='signup'),
    url(r'^create/$',views.collegeCreate.as_view(),name='create'),
     url(r'^loggedin/$',views.logged,name='loggedin'),
    url(r'^about/$',views.About,name='about'),
]