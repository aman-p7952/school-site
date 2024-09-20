from django.urls import path
from . import views

urlpatterns = [
    path('fee/', views.fee, name='fee'),
    path('fee_details',views.fetch_student_details,name='fee_details'),  
    path('fee_paid',views.fee_payment,name="fee_paid"),
    path('fee_structure',views.fee_structure,name="fee_structure"),
    path('fee_structure_by_class',views.fee_structure_by_class,name="fee_structure_by_class"),
    path('enter_fee_structure',views.enter_fee_structure,name="enter_fee_structure")
    
]