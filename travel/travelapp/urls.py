from . import views
from django.urls import path

urlpatterns = [

    # path('',views.display,name='display'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('display1/',views.display1,name='display1')

    path('',views.form,name='form'),

    #path('addition/',views.addition,name='addition')
    ]