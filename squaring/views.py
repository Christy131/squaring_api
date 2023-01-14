from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello world!')

class SquareView(View):
    def get(self, request, number):
        return HttpResponse(number**2)