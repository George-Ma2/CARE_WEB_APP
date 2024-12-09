from django.urls import path
from . import views
from .views import RoomView, CreateRoomView

urlpatterns = [
    # path('vendors/', views.VendorList.as_view()),
    # path('vendor/<int:pk>/', views.VendorDetail.as_view()),
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view())
]
