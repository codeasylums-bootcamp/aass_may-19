from django.conf.urls import url
from django.urls import include

from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'privacy/', core_views.privacy, name="privacy"),
    url(r'facebook/add_post/', core_views.add_post, name="facebook_add_post"),
    url(r'facebook/publish/', core_views.publish, name='facebook_publish'),
]
