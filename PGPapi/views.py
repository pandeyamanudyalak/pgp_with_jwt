import datetime
from datetime import timedelta
from os import EX_NOINPUT, access
import re
from telnetlib import LOGOUT
from termios import NL1
from urllib import response
from django.shortcuts import redirect
from rest_framework.response import Response
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header

from PGPapi.authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import *
from .models import *
from django.contrib.auth import login,logout
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.authentication import  BasicAuthentication
from rest_framework import permissions,exceptions
from rest_framework.permissions import IsAuthenticated

# Create your views here.


############# GET and POST REQUEST of userLocation MODEL ##############
class userLocationAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args,**kwargs):
        print(request.user)
        user_location= userLocation.objects.all()
        get_userlocation_data = userLocationSerializer(user_location, many=True)
        return JsonResponse(get_userlocation_data.data, safe=False, status=HTTP_200_OK)

    def post(self, request, *args,**kwargs):
        serializer=userLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of userLocation MODEL ##############
class userLocationIDAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get_object(self, id):
        try:
            return userLocation.objects.get(pk=id)
        except userLocation.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def post(self, request, id,*args,**kwargs):
        location= self.get_object(id)
        serializer = userLocationSerializer(location, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        locationobj = self.get_object(id)
        serializer = userLocationSerializer(locationobj)
        return JsonResponse(serializer.data)

    def put(self, request, id,*args,**kwargs):
        user_location= self.get_object(id)
        serializer = userLocationSerializer(user_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userRole MODEL ##############
class userRoleAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args,**kwargs):
        
        user_role= userRole.objects.all()
        get_userRole_data = userRoleSerializer(user_role, many=True)
        return JsonResponse(get_userRole_data.data, safe=False, status=HTTP_200_OK)

    def post(self, request, *args,**kwargs):
        serializer=userRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of userRole MODEL ##############
class userRoleIDAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get_object(self, id):
        try:
            return userRole.objects.get(pk=id)
        except userLocation.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        roleobj = self.get_object(id)
        serializer = userRoleSerializer(roleobj)
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def post(self, request, id,*args,**kwargs):
        user_role= self.get_object(id)
        serializer = userRoleSerializer(user_role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, id,*args,**kwargs):
        userRole= self.get_object(id)
        serializer = userRoleSerializer(userRole, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userDetails MODEL ##############
class userLoginAPI(APIView):
    def get(self, request, *args,**kwargs):
        user_login= CustomUser.objects.all()
        get_userdetail_data = userLoginSerializer(user_login, many=True)
        return JsonResponse(get_userdetail_data.data, safe=False, status=HTTP_200_OK)

    def post(self, request, *args,**kwargs):
        serializer=userLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of userDetails MODEL ##############
class userLoginIDAPI(APIView):
    def get_object(self, id):
        try:
            return CustomUser.objects.get(pk=id)
        except CustomUser.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def post(self, request, id,*args,**kwargs):
        user_login= self.get_object(id)
        serializer = userLoginSerializer(user_login, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = userLoginSerializer(getobj)
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def put(self, request, id,*args,**kwargs):
        userLogin= self.get_object(id)
        serializer = userLoginSerializer(userLogin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of userDetails MODEL ##############
class userDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args,**kwargs):
        user_detail= userDetails.objects.all()
        get_userdetail_data = userDetailSerializer(user_detail, many=True)
        return JsonResponse(get_userdetail_data.data, safe=False, status=HTTP_200_OK)

    def post(self, request, *args,**kwargs):
        serializer=userDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'msg':'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of userDetails MODEL ##############
class userDetailIDAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get_object(self, id):
        try:
            return userDetails.objects.get(pk=id)
        except userDetails.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = userDetailSerializer(getobj)
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def post(self, request, id,*args,**kwargs):
        user_detail= self.get_object(id)
        serializer = userDetailSerializer(user_detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, id,*args,**kwargs):
        userDetail= self.get_object(id)
        serializer = userDetailSerializer(userDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of Form MODEL ##############
class formDataAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args,**kwargs):
        form_data= formData.objects.all()
        get_from_data = formDataSerializer(form_data, many=True)
        return JsonResponse(get_from_data.data, safe=False, status=HTTP_200_OK)

    def post(self, request):
        serializer = formDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of FORM MODEL ##############
class formDataIDAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get_object(self, id):
        try:
            return formData.objects.get(pk=id)
        except formData.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = formDataSerializer(getobj)
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def put(self, request, id,*args,**kwargs):
        formDetail= self.get_object(id)
        serializer = formDataSerializer(formDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def post(self, request, id,*args,**kwargs):
        formDetail= self.get_object(id)
        serializer = formDataSerializer(formDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# GET and POST REQUEST of AGENCY MODEL ##############
class agencyNameAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args,**kwargs):
        agency_data= issueAgency.objects.all()
        get_agency_data = issueAgencySerializer(agency_data, many=True)
        return JsonResponse(get_agency_data.data, safe=False)

    def post(self, request):
        serializer = issueAgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'}, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

############# GET, UPDATE, DELETE from ID of AGENCY MODEL ##############
class issueAgencyDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get_object(self, id):
        try:
            return issueAgency.objects.get(pk=id)
        except issueAgency.DoesNotExist:
            return JsonResponse(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        getobj = self.get_object(id)
        serializer = issueAgencySerializer(getobj)
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def post(self, request, id,*args,**kwargs):
        issue_agency= self.get_object(id)
        serializer = issueAgencySerializer(issue_agency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, id,*args,**kwargs):
        issueAgencyDetail= self.get_object(id)
        serializer = issueAgencySerializer(issueAgencyDetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        deleteobj = self.get_object(id)
        deleteobj.delete()
        return JsonResponse({'msg':'Data Deleted'},status=HTTP_204_NO_CONTENT)

############# FILTER DATA ACCORDING TO THE LOCATION SELECTED ##############
class filter(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, name, *args, **kwargs):
        loc =  userLocation.objects.get(location=name)
        user_details = userDetails.objects.filter(userLocation=loc.id)
        userDetail = userDetailSerializer(user_details, many=True)
        return JsonResponse(userDetail.data, safe=False,  status=HTTP_200_OK)

############# FILTER DATA ACCORDING TO THE NEWFLAG SELECTED ##############


class newFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        #logged_person = CustomUser.objects.get(name=name)
        form_data = formData.objects.filter(loggedPerson=request.user.id, newFlag = True)
        serializer = formDataSerializer(form_data, many=True)
        
        return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)

class oldFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        form_data = formData.objects.filter(loggedPerson=request.user.id, oldFlag = True)
        serializer = formDataSerializer(form_data, many=True)
        return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)

class completedFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        form_data = formData.objects.filter(loggedPerson=request.user.id, completedFlag = True)
        serializer = formDataSerializer(form_data, many=True)
        return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)

class closeFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        form_data = formData.objects.filter(loggedPerson=request.user.id, closeFlag = True)
        serializer = formDataSerializer(form_data, many=True)
        return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)

class notification(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request):
        notification_data = formData.objects.filter(person1=request.user.id)
        if notification_data != None:
            form_filter_data = formDataSerializer(notification_data, many=True)
            return JsonResponse(form_filter_data.data, safe=False, status=HTTP_200_OK)
        else:
            return JsonResponse({"msg":"PROBLEM IN GET"}, status=HTTP_400_BAD_REQUEST)

class changeOldFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request):
        form_data = formData.objects.all()
        for data in form_data:
            date_after_1_days = data.created_at + timedelta(days=1)
            if date_after_1_days == datetime.date.today():
                formData.objects.filter(id=data.id).update(oldFlag=True ,newFlag=False, tocloseFlag=False, completedFlag=False)
        return JsonResponse({"msg":"Close Flag Changed"}, status=HTTP_200_OK)


class changeToCloseFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request):
        form_data = formData.objects.all()
        for data in form_data:
            date_after_6_days = data.created_at + timedelta(days=6)
            if date_after_6_days == datetime.date.today():
               formData.objects.filter(id=data.id).update(tocloseFlag=True, oldFlag=False ,newFlag=False,completedFlag=False)
        return JsonResponse({"msg":"Close Flag Changed"}, status=HTTP_200_OK)



class changeCompleteFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self,request):
        form_data=formData.objects.filter(tocloseFlag=True,person1=request.user.id)
        for data in form_data:
            formData.objects.filter(id=data.id).update(completedFlag=True)
        return JsonResponse({"msg":"Completed Flag Changed"}, status=HTTP_200_OK) 

class completedByLoggedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self,request,id):
        form_data=formData.objects.filter(tocloseFlag=True,loggedPerson=request.user.id)
        formData.objects.filter(id=id).update(closedByLoggedUser=True)
        return JsonResponse({"msg":"Closed By Logged Use"}, status=HTTP_200_OK)    
        
       



class completedFlag(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self,request,id):
        formData.objects.filter(id=id).update(completedFlag=True)
        return JsonResponse({"msg":"Changed Complated Flag"}, status=HTTP_200_OK)  



class approvedByPersonForm(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request,id):
        form_data = formData.objects.filter(id=id).values()
        for data in form_data:
            if request.user.id == data['person1_id']:
                formData.objects.filter(id=data['id']).update(verified_by_person1=True)
                return JsonResponse({'msg':'Verfied'}, status=HTTP_200_OK)
            if request.user.id == data['person2_id']:
                formData.objects.filter(id=data['id']).update(verified_by_person2=True)
                return JsonResponse({'msg': 'Verfied'}, status=HTTP_200_OK)


class closedByPersonForm(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request,id):
        form_data = formData.objects.filter(id=id).values()
        for data in form_data:
            if request.user.id == data['person1_id']:
                formData.objects.filter(id=data['id']).update(closedByPerson1=True)
                return JsonResponse({'msg':'Closed successfully'}, status=HTTP_200_OK)

            if request.user.id == data['person2_id']:
                formData.objects.filter(id=data['id']).update(completedFlag=True)
                return JsonResponse({'msg': 'Closed successfully'}, status=HTTP_200_OK)

            if request.user.id == data['loggedPerson_id']:
                formData.objects.filter(id=data['id']).update(closedByLoggedUser=True)
                return JsonResponse({'msg': 'Closed successfully'}, status=HTTP_200_OK)


class completedTask(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self, request,name):
        form_data = formData.objects.all().values()
        for data in form_data:
            if request.user.id == data['person1_id']:
                formData.objects.filter(id=data['id'],completedFlag=True)
                return JsonResponse({'msg':'Closed successfully'}, status=HTTP_200_OK)

            if request.user.id == data['person2_id']:
                formData.objects.filter(id=data['id'],completedFlag=True)
                return JsonResponse({'msg': 'Closed successfully'}, status=HTTP_200_OK)

            if request.user.id == data['loggedPerson_id']:
                formData.objects.filter(id=data['id'],completedFlag=True)
                return JsonResponse({'msg': 'Closed successfully'}, status=HTTP_200_OK)


class extensionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self,request,id):
        form_data=formData.objects.filter(id=id)
        serialized_data=formDataSerializer(form_data,many=True)
        return JsonResponse(serialized_data.data,safe=False)


class updateExtension(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    def get(self,request,id):
        formData.objects.filter(id=id).update(verified_by_person1=False,verified_by_person2=False,oldFlag=False,tocloseFlag=False,closedByLoggedUser=False,closedByPerson1=False,completedFlag=False)
        return JsonResponse({"msg":"Work Extended"}, status=HTTP_200_OK)  



class loginApiView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=CustomUser.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        access_token = create_access_token(user.id)
        refresh_token=create_refresh_token(user.id)

        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )
        response = Response()
        response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
        response.data = {
            'token' : access_token
        }
        return response




# class userAPIView(APIView):
#     def get(self,request):
#         auth=get_authorization_header(request).split()
#         if auth and len(auth) ==2:
#             token=auth[1].decode('utf-8')
#             print('----------------------token inside view',token)

#             id = decode_access_token(token)
#             print('----------------id',id)

#             user= CustomUser.objects.get(id=id)
#             print('======user',user)
             
#             if user:
#                 serializer=   userLoginSerializer(user)
#                 print(serializer)
#                 return Response(serializer.data)

#         raise exceptions.AuthenticationFailed('unauthenticated')

class userAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        print(request)
        return Response(userLoginSerializer(request.user).data) 

class refreshAPIView(APIView):
    def post(self,request):
        refresh_token=request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)

        if not UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            raise exceptions.AuthenticationFailed('Unauthenticated')

        return Response({
            'token':access_token
        })


class logoutAPIView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        UserToken.objects.filter(user_id=request.user.id).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'msg':'success'
        }
        return response