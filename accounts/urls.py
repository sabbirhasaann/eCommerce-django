from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from . import session_view


from .api_views import CustomLoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', login_required(views.dashboard_view), name='dashboard'),
    path('set-session/', session_view.set_session, name='set-session'),
    path('get-session/', session_view.get_session, name='get-session'),
    path('delete-key/', session_view.delete_key, name='delete-key'),
    path('visit-counter/', session_view.visit_counter, name='visit-counter')
]

urlpatterns += [
    path('api/token/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
