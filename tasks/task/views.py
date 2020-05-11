from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.

class TestRequest(APIView):

    def post(self, request, *args, **kwargs):
        body = request.body
        req_obj = json.loads(body)
        return JsonResponse(req_obj, safe=False)
