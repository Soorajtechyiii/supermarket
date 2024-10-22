from django.urls import path  #type:ignore
from.import views
urlpatterns=[path('pagehtml/',views.pagehtml),
             path('items/',views.items),
             path('dataread/',views.dataread),
             path('setcookie/',views.setcookie),
             path('getcookie/',views.getcookie),
             ]