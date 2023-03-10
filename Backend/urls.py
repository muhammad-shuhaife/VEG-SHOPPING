from django.urls import path
from Backend import views

urlpatterns = [
    path('loginpage/', views.loginpage, name="loginpage"),

    path('indexpage/',views.indexpage,name="indexpage"),

    path('adminpage/', views.adminpage, name="adminpage"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('viewadmin/', views.viewadmin, name="viewadmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),

    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),


    path('categorypage/', views.categorypage, name="categorypage"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('viewcategory/', views.viewcategory, name="viewcategory"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),


    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('viewproductB/', views.viewproductB, name="viewproductB"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('viewcomplaint/', views.viewcomplaint, name="viewcomplaint"),
    path('deletecomplaint/<int:dataid>/', views.deletecomplaint, name="deletecomplaint"),

]