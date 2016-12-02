"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^page/(?P<n2>\d+)/(?P<n1>\d+)', views.page),
    url(r'^app01/', include("app01.urls")),
    url(r'^db/', views.db_handle),

    url(r'^login/$', views.acc_login),
    url(r'^logout/$', views.acc_logout),
    url(r'^homepage/$', views.homepage),
    url(r'^host/$', views.host,name='host'),
    url(r'^audit/$', views.audit, name='audit'),
    url(r'^asset/$', views.asset, name='asset'),
    url(r'^webqq/', include("webqq.urls")),
    url(r'^register/$', views.register),

    url(r'^test/$', views.testurl),
]
