"""squadra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from addProject import views as addProjectViews



# from squadra_app.views import
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_view

from uploadapp.views import upload_file
from squadra_app.views import app_page, ajax_html_text, ajax_storage_content, ajax_open_file


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', user_views.create_user, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('upload/', upload_file, name='upload'),
    path('squadra_app/', app_page, name='app_page'),
    path('squadra_app/ajax_html_text', ajax_html_text, name='ajax_html_text'),
    path('squadra_app/ajax_storage_content', ajax_storage_content, name='ajax_storage_content'),
    path('squadra_app/ajax_open_file', ajax_open_file, name='ajax_open_file'),
    path('NewProject', addProjectViews.NewProject, name='NewProject'),
    path('addProject', addProjectViews.ProjectAdd, name='addProject'),
    path('logout/', user_views.logout, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
