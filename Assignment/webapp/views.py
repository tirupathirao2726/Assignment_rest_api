from django.shortcuts import render
from .models import user_info
from django.http import JsonResponse
from .serializers import user_infoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def user_info_list(request,format=None):
    if request.method=='GET':
        users=user_info.objects.all()
        serializer=user_infoSerializer(users,many=True)
        return  JsonResponse({'get_user_info':serializer.data})
    if  request.method=='POST':
        serializer=user_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])

def user_info_detail(request,id,format=None):
    try:
        user=user_info.objects.get(pk=id)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=user_infoSerializer(user)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=user_infoSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
