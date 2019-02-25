# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.

class BranchApiView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self,request,format=None):
        branch_list = Branch.objects.all()
        serializer = BranchDetailSerializer(branch_list,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self,request,format=None):
        """{
            "name":"Nairobi",
            "address":"P.O BOX 0100",
            "branch_code":"BRH00"
        }
        """
        name = request.data['name']
        address = request.data['address']
        branch_code = request.data['branch_code']

        branch_obj = Branch.objects.create(
            name=name,
            address=address,
            branch_code=branch_code
        )

        serializer = BranchSerializer(branch_obj)

        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class BranchDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def get(self,request,pk,format=None):
        branch = Branch.objects.get(pk=pk)
        serializer = BranchDetailSerializer(branch)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        branch = Branch.objects.get(pk=pk)
        serializer = BranchDetailSerializer(branch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        branch =Branch.objects.get(pk=pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)