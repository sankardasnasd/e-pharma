"""
URL configuration for untitled project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from E_PHARMA import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('login_post/', views.login_post),

    path('admin_home/', views.admin_home),

    path('admin_verify_customers/', views.verify_customer),
    path('approve_customer/<id>', views.approve_customer),
    path('reject_customer/<id>', views.reject_customer),

    path('admin_view_approved_customers/', views.view_approved_customers),
    path('view_approvedcustomer_post/', views.view_approvedcustomer_post),

    path('admin_view_rejected_customers/', views.view_rejected_customers),
    path('view_rejectedcustomer_post/', views.view_rejectedcustomer_post),

    path('admin_add_stock/', views.add_stock),
    path('addstock_post/', views.addstock_post),

    path('admin_view_stocks/', views.view_stocks),
    path('viewstocks_post/', views.viewstocks_post),

    path('admin_edit_stock/<did>', views.edit_stock),
    path('editstock_post/', views.editstock_post),

    path('admin_delete_stocks/<id>/', views.admin_delete_stocks),

    path('admin_add_inventory/', views.add_inventory),
    path('addinventory_post/', views.addinventory_post),

    path('admin_view_inventory/', views.view_inventory),
    path('viewinventory_post/', views.viewinventory_post),

    path('admin_edit_inventory/<id>/', views.edit_inventory),
    path('editinventory_post/', views.editinventory_post),

    path('admin_delete_inventory/<id>/', views.admin_delete_inventory),

    path('admin_view_prescription/', views.view_prescription),
    path('viewprescription_post/', views.viewprescription_post),

    path('admin_update_availability_status/<id>', views.update_availability_status),
    path('updateavailability_post/', views.updateavailability_post),

    path('admin_view_orders/', views.view_orders),
    path('vieworder_post/', views.vieworder_post),

    path('view_suborders/<id>', views.view_suborders),
    path('delivered/<id>', views.delivered),
    # path('viewsuborders_post/', views.viewsuborder_post),


    path('admin_view_payment_status/', views.view_payment_status),
    path('view_pstatus_post/', views.view_pstatus_post),


    path('admin_view_more/<id>', views.view_more),

    path('admin_view_complaint/', views.view_complaint),
    path('viewcomplaint_post/', views.viewcomplaint_post),

    path('admin_send_reply/<id>/', views.send_reply),
    path('sendreply_post/<id>', views.sendreply_post),

    path('admin_view_feedback/', views.view_feedback),
    path('viewfeedback_post/', views.viewfeedback_post),

###########customer#############
    path('customer_home/', views.customer_home),

    path('customer_registeration/', views.customer_registeration),
    path('customerreg_post/', views.customerreg_post),

    path('view_profile/', views.view_profile),
    path('viewprofile_post/', views.viewprofile_post),

    path('customer_search_products/', views.search_products),
    path('csearchproduct_post/', views.csearchproduct_post),


    path('customer_upload_prescription/', views.upload_prescription),
    path('upload_post/', views.upload_post),

    path('view_availability_status/', views.view_availability_status),

    path('availabilityview_post/', views.availabilityview_post),


    path('customer_confirm_order/', views.confirm_order),
    path('confirmorder_post/', views.confirmorder_post),


    path('view_order_status/', views.view_order_status),
    path('vieworderstatus_post/', views.vieworderstatus_post),

    path('view_order_statussub/<id>', views.view_order_statussub),
    path(' vieworderstatussub_post', views. vieworderstatussub_post),

     path('customer_payment/', views.payment),
     path('payment_post/', views.payment_post),

     path('confirmorder_pay_post', views.confirmorder_pay_post),


    path('customer_view_payment_history/', views.view_payment_history),
    path('viewpaymenthistory_post/', views.viewpaymenthistory_post),
    path('phistoryview_more/<id>', views.phistoryview_more),

    path('customer_send_complaint/', views.send_complaint),
    path('sendcomplaint_post/', views.sendcomplaint_post),

    path('customer_view_reply/', views.view_reply),
    path('viewreply_post/', views.viewreply_post),

    path('customer_send_feedback/', views.send_feedback),
    path('sendfeedback_post/', views.sendfeedback_post),

    path('customer_edit_profile/<id>', views.edit_profile),
    path('editprofile_post/', views.editprofile_post),

    path('verifycustomer_post/', views.verifycustomer_post),
    path('load_on_type/', views.load_on_type),
]
