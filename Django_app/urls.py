"""Django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from .views import (
    home_page,
    about_page,
    contact_page
)
from post.views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view
)
urlpatterns = [
    path('', home_page),
    path('blog-new/', blog_post_create_view),
    path('blogs/', blog_post_list_view),
    path('blog/<str:slug>/edit/', blog_post_update_view),
    path('blog/<str:slug>/delete/', blog_post_delete_view),
    # path('blog/<int:post_id>/', blog_post_detail_page), # dynamic routing
    path('blog/<str:slug>/', blog_post_detail_view), # routing with slug
    path('about/', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
