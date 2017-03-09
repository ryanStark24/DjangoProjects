from django.conf.urls import url
from college import views

namespace='college'
urlpatterns=[
    
    url('^$',views.MyList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^create/$',views.create,name='create'),
    url(r'^about/$',views.About,name='about'),
]
