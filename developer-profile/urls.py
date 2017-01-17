from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from authentication.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

    url(r'^api/v1/', include(router.urls)),
    # url('^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
]

# urlpatterns += router.urls
