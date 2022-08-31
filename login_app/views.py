from dataclasses import dataclass
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response as RestResponse
from rest_framework.decorators import api_view
from .import service


@api_view(['POST'])
def login_auth(request):
    if not all (k in request.data for k in ("email_id","password")):
        return RestResponse("Some parameter is missing")
    if request.data['email_id']=="" or None:
        return RestResponse("emai_id should not be empty")
    if request.data['password']=="" or None:
        return RestResponse("password should not be empty")
    if not request.data['email_id'].endswith('.com'):
        return RestResponse("please enter valid email address")
    data_validation = service.login_service().login_check_service(request)
    if len(data_validation)>0:
        if data_validation[0]['is_admin']==True:
            url_list=service.login_service().url_query(request)
            return JsonResponse(url_list,safe=False)
        else:
            url_list = service.login_service().user_non_adim_query(request)
            return JsonResponse(url_list,safe=False)
    else:
        return JsonResponse("User no longer active",safe=False)