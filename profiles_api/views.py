from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self,request,format=None):

        an_apiview=['Uses http methods as function (get,post,put,delete)',
        'is smilar to django view',
        'gives you most control',
        'is manually mapped to urls']

        return Response({'msg':'Hello!','an_apiview':an_apiview})
