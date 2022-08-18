from django.urls import path
from.import views

urlpatterns = [
    path('', views.register,name='reg'),
    path('login', views.login,name='lgt'),
    path('logout', views.logout,name='lgn'),
    path('profile', views.prof,name='pro'),
    path('uprofile', views.update_profile,name='upro'),
    path('teacherreg', views.teacherregister,name='teacherreg'),   
]