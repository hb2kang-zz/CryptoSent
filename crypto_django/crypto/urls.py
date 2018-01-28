from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display$', views.display, name='display'),
    url(r'^bitcoin$', views.bitcoin, name='bitcoin'),
    url(r'^ethereum$', views.ethereum, name='ethereum'),
    url(r'^litecoin$', views.litecoin, name='litecoin'),
    url(r'^ripple$', views.ripple, name='ripple'),
    url(r'^bitcoincash$', views.bitcoincash, name='bitcoincash'),
    url(r'^stellar$', views.stellar, name='stellar'),
]
