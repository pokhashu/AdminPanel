from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('getSchedule/', getSchedule),
    path('askForApproval/', askForApproval),
    path('isGroupApproved/', isGroupApproved),
    path('getChatId/', getChatId),
]
