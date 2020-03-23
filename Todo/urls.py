from django.urls import path
from . import views
app_name='Todo'

urlpatterns = [
    path('TodoMgr',views.TodaytaskList.as_view(),name='todaytask'),
    path('mark/<id>',views.marktask,name='marktask'),
    path('add',views.addtask,name='addtask'),
]
