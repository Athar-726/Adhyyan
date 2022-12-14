from django.urls import path
from.import views

urlpatterns = [
    path('', views.index,name='hm'),
    path('course', views.course,name='cor'),
    path('course/<int:cid>', views.course1,name='cor1'),
    path('teacher', views.Teacher,name='tech'),
    path('price', views.Price,name='fee'),
    path('course/sgn/<int:brid>', views.sgbran,name='rev'),
    path('hh', views.review,name='rev'),
    path('feed', views.Feedback,name='fd'),
    path('feed', views.feed,name='feed'),
    path('contact', views.Contact,name='cont'),
    path('Register', views.Register,name='regis'),
    path('register1', views.Register1,name='register1'),
    path('prof', views.prof,name='pro'),
    path('Login', views.Log,name='log'),
    path('Tregister', views.Register,name='techregis'),
    path('updateprofile', views.uprof,name='uprofile'),
    path('car',views.Cart,name='car'),
    path('ser',views.Search,name='ser'),
    path('remove_ser',views.remove_ser,name='remove_ser'),
    path('videolect',views.videolect,name='videolect'),
    path('get_cart_data',views.get_cart_data,name='get_cart_data'),
    path("process_payment",views.process_payment,name="process_payment"),
    path("payment_done",views.payment_done,name="payment_done"),
    path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
    path("material",views.material,name="material"),
    path("tadd_record",views.add_recor,name="tadd_record"),
    path('cnc',views.Counseling,name='cnc'),
]