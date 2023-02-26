from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from littlelemon.urls import router
from . import views
from restaurant import views

router.register('users', views.UserViewSet)
router.register('tables', views.BookingViewSet)



urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]