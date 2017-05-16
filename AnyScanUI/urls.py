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

from AnyScanUI import views
from AnyScanUI.view import cmsview, portview, epocview, autopocview

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
    url(r'^portattack/$', portview.portattack, name ='portattack'),
    url(r'^portattacklog/$', portview.portattacklog, name ='portattacklog'),
    url(r'^portattack_list/$', portview.portattack_list, name ='portattack_list'),
    url(r'^portattackpause/$', portview.portattackpause, name ='portattackpause'),
    url(r'^portattackdel/$', portview.portattackdel, name ='portattackdel'),
    url(r'^portattackchild_list/$', portview.portattackchild_list, name ='portattackchild_list'),
    url(r'^cms_scan/$', cmsview.cms_scan, name ='cms_scan'),
    url(r'^cms_scan_log/$', cmsview.cms_scan_log, name ='cms_scan_log'),
    url(r'^cms_scan_stop/$', cmsview.cms_scan_stop, name ='cms_scan_stop'),
    url(r'^cms_scan_list/$', cmsview.cms_scan_list, name ='cms_scan_list'),
    url(r'^cms_scan_del/$', cmsview.cms_scan_del, name ='cms_scan_del'),
    url(r'^exe_poc/$', epocview.exe_poc, name ='exe_poc'),
    url(r'^baidu_url/$', epocview.baidu_url, name ='baidu_url'),
    url(r'^url_log/$', epocview.url_log, name ='url_log'),
    url(r'^exec_poc_log/$', epocview.exec_poc_log, name ='exec_poc_log'),
    url(r'^poc_main_list/$', epocview.poc_main_list, name ='poc_main_list'),
    url(r'^poc_chil_list/$', epocview.poc_chil_list, name ='poc_chil_list'),
    url(r'^epoc_upload/$', epocview.epoc_upload, name ='epoc_upload'),
    url(r'^auto_poc_start/$', autopocview.auto_poc_start, name ='auto_poc_start'),
    url(r'^auto_poc_stop/$', autopocview.auto_poc_stop, name ='auto_poc_stop'),
    url(r'^auto_poc_log/$', autopocview.auto_poc_log, name ='auto_poc_log'),
    url(r'^auto_poc_data/$', autopocview.auto_poc_data, name ='auto_poc_data'),
    url(r'^auto_poc_data_chil/$', autopocview.auto_poc_data_chil, name ='auto_poc_data_chil'),
    url(r'^auto_poc_del/$', autopocview.auto_poc_del, name ='auto_poc_del'),



]
