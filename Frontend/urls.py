from django.urls import path
from Frontend import views
urlpatterns = [

path('loginfront/',views.loginfront,name="loginfront"),
path('logoutfront/',views.logoutfront,name="logoutfront"),

path('homehtmlpage/',views.homehtmlpage,name="homehtmlpage"),
path('aboutus/',views.aboutus,name="aboutus"),
path('contact/',views.contact,name="contact"),
path('savecontact/',views.savecontact,name="savecontact"),
path('registration/',views.registration,name="registration"),
path('saveregistration/',views.saveregistration,name="saveregistration"),
path('viewproducts/<itemcatg>',views.viewproducts,name="viewproducts"),
path('singleproduct/<int:dataid>',views.singleproduct,name="singleproduct"),

]