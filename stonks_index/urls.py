from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'set_stonks_data/$', views.set_stonks_data),
    url(r'get_stonks_data/$', views.get_stonks_data),
]
