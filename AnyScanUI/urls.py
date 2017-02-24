"""AnyScan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from AnyScanUI import views,portattack

from AnyScan import settings

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^alltasks/$',views.alltasks,name = 'alltasks'),
    url(r'^add_task/$',views.add_task,name = 'add_task'),
    url(r'^bash_task/$',views.bash_task,name = 'bash_task'),
    url(r'^web_log/$',views.web_log,name = 'web_log'),
    url(r'^task_stop/$',views.task_stop,name = 'task_stop'),
    url(r'^web_kill/$',views.web_kill,name = 'web_kill'),
    url(r'^web_delete/$',views.web_delete,name = 'web_delete'),
    url(r'^web_flush/$',views.web_flush,name = 'web_flush'),
    url(r'^port_scaner/$',views.port_scaner,name = 'port_scaner'),
    url(r'^read_file/$',views.read_file,name = 'read_file'),
    url(r'^portattack/$',portattack.portattack,name = 'portattack'),
    url(r'^portattacklog/$',portattack.portattacklog,name = 'portattacklog'),
    url(r'^portattack_list/$',portattack.portattack_list,name = 'portattack_list'),
    url(r'^portattackpause/$',portattack.portattackpause,name = 'portattackpause'),
]
