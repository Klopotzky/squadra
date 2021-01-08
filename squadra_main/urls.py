"""squadra_main URL Configuration

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
from django.urls import path, include
from addProject import views as addProjectViews
from user import views as user_views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_view

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.create_user, name='register'),
    path('logout/', user_views.logout, name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('editor/', include('editor.urls')),
    path('workflow/', include('workflow.urls')),
    path('projects', addProjectViews.NewProjectView, name='NewProject'),
    path('projects', addProjectViews.ProjectListView, name='ProjectListView1'),
    path('addProject', addProjectViews.ProjectAdd, name='addProject'),
    # path('projects', addProjectViews.ProjectList, name='projects'),
    path('ProjectEdit/<str:id>/', addProjectViews.DynamicUrl),
    path('chat/', include('chat.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
+ aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)

