from django.conf.urls import url, include
from myapp.views import show_user

urlpatterns = [
    url(r'show_user$', show_user, ),
]
