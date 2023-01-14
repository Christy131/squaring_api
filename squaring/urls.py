from django.urls import path
from squaring.views import HelloWorldView, SquareView

urlpatterns = [
    path('', HelloWorldView.as_view(), name="home"),
    path('<int:number>', SquareView.as_view(), name="number"),
    ]