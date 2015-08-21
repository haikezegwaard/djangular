from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from djangular.models import Apple
from djangular.serializers import AppleSerializer, UserSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
import djangular
from djangular.views import HomePageView
admin.autodiscover()

# Serializers define the API representation.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppleViewSet(viewsets.ModelViewSet):
    queryset = Apple.objects.all()
    serializer_class = AppleSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'apples', AppleViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^home', HomePageView.as_view(), name = 'home'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
