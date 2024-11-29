from django.contrib import admin
from django.urls import path
from Content import views
from Comments import views as comment_view
from accounts import views as LoginView
# from Content. import ContentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ContentView, name='Content'),
    path('comments/<int:data>/', comment_view.CommentView, name='comments'),
    path('register/', views.ContentView, name='register'),
    # path('login/', views.ContentView, name='login')
    path('login/', LoginView.user_login, name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


