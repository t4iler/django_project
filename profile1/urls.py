from django.urls import path
from django.conf.urls.static import static          #lib needs to open image
from django.conf import settings                    #lib needs to open image

from .views import ProfileViewSet

profile_list = ProfileViewSet.as_view({
        'get': 'list',
})

profile_detail = ProfileViewSet.as_view({
        'get': 'retrieve',
})


urlpatterns = [
    path('profile/', profile_list),
    path('profile/<int:pk>/', profile_detail),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)