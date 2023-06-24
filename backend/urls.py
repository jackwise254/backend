from django.urls import include, path
from rest_framework import routers
from api.views import ActionViewSet
from users.views import LoginView, SignupView
from properties.views import PropertyListView, ListingView, PropertyPost,ReactionsPost
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import BlogListView


router = routers.DefaultRouter()
router.register(r'reaction', ActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reaction/<int:pk>/heart-clicks/', ActionViewSet.as_view({'post': 'heart_clicks'}), name='heart_clicks'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('properties/', PropertyListView.as_view(), name='property_list'),
    path('listings/<int:pk>', ListingView.as_view(), name='listings_list'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('posts/', PropertyPost.as_view(), name='posts'),
    path('reactions/', ReactionsPost.as_view(), name="reactions"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
