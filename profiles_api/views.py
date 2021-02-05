from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer

class HelloApiView(APIView):
    serializer_class=serializer.HelloSerializer

    def get(self,request,format=None):

        an_apiview=['Uses http methods as function (get,post,put,delete)',
        'is smilar to django view',
        'gives you most control',
        'is manually mapped to urls']

        return Response({'msg':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        serializer1=self.serializer_class(data=request.data)
        if serializer1.isValid():
            name=serializer1.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
