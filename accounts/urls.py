from django.conf.urls import url
from.import views
from django.conf.urls.i18n import urlpatterns
from django.contrib.auth.decorators import login_required

app_name='accounts'
 
urlpatterns=[
    url(r'profile',views.profile,name='profile')


    ]