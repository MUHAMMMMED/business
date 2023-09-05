from django.urls import path
from business.views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='business'

urlpatterns = [



  path('',home, name="home"),
  path('Team',Team, name="Team"),
  path('About',about, name="About"),
  path('CallUs',CallUs, name="CallUs"),
  path('blog',blog, name="blogAll"),
  path('<int:id>/',blogdetails, name="blogdetails"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
