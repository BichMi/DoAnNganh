from django.conf.urls import url
from AirlineTicketApp.views import index

urlpatterns = [
    url(r'^$', index, name='home')
    ]