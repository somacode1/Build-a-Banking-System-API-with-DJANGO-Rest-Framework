# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics,status
from rest_framework import Response 
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.

class BranchApiView(APIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

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

