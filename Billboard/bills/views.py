# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Billboard
from . serializers import BillboardSerializer
# Create your views here.


class BillList(APIView):
	def get(self,request):
		bills = Billboard.objects.all()
		serializer = BillboardSerializer(bills,many=True)
		return Response(serializer.data)

	def post(self):
		pass