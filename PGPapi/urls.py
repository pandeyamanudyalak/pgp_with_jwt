from django.urls import path,include
from . import views

urlpatterns=[

    path('auth/',include('rest_framework.urls')),
    
    path('locationapi', views.userLocationAPI.as_view(), name="userLocationAPI"),
    path('locationapi/<int:id>', views.userLocationIDAPI.as_view(), name="userLocationID"),

    path('roleapi', views.userRoleAPI.as_view(),name="userRoleAPI"),
    path('roleapi/<int:id>', views.userRoleIDAPI.as_view(), name="userRoleIDAPI"),

    path('loginapi', views.userLoginAPI.as_view(), name="userLoginAPI"),
    path('loginapi/<int:id>', views.userLoginIDAPI.as_view(), name="userLoginIDAPI"),

    path('userdetailapi', views.userDetailAPI.as_view(), name="userDetailID"),
    path('userdetailapi/<int:id>', views.userDetailIDAPI.as_view(), name="userDetailIDAPI"),

    path('formdataApi', views.formDataAPI.as_view(), name="formDataAPI"),
    path('formdataApi/<int:id>', views.formDataIDAPI.as_view(), name="formDataIDAPI"),

    path('agencyapi', views.agencyNameAPI.as_view(), name="flagAPI"),

    path('filterapi/<str:name>', views.filter.as_view(),name="filterapi"),

    path('newflagapi', views.newFlag.as_view(), name="newFlagapi"),

    path('oldflagapi', views.oldFlag.as_view(), name="oldFlagapi"),

    path('closeflagapi', views.closeFlag.as_view(), name="closeFlagapi"),

    path('completedflagapi', views.completedFlag.as_view(), name="completedFlagapi"),

    path('notificationapi', views.notification.as_view(), name="notificationapi"),

    path('changectoloseflagapi', views.changeToCloseFlag.as_view(), name="change"),

    path('changeoldflagapi', views.changeOldFlag.as_view(), name="change"),

    path('changecompleteflag',views.changeCompleteFlag.as_view(),name="changecompleteflag"),

    path('completedbyloggeduser/<int:id>',views.completedByLoggedUser.as_view(),name='completedbyloggeduser'),

    path('completedflag',views.completedFlag.as_view(),name='completedflag'),

    path('verify/<int:id>',views.approvedByPersonForm.as_view(),name="verify"),

    path('close/<int:id>/<str:name>',views.closedByPersonForm.as_view(),name="close"),

    path('completedtask/<str:name>',views.completedTask.as_view(),name='completedtask'),

    path('extension/<int:id>',views.extensionView.as_view(),name='extension'),

    path('updateextension/<int:id>',views.updateExtension.as_view(),name='updateextension'),

    #path('user_login',views.userLogin.as_view(),name='userlogin'),
    path('user_login',views.loginApiView.as_view(),name='userlogin'),

    path('user',views.userAPIView.as_view(),name='user'),
    
    
    path('refresh',views.refreshAPIView.as_view(),name='refresh'),

    path('logout',views.logoutAPIView.as_view(),name='logout')


  
    
]