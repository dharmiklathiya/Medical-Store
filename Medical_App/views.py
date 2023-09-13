from django.shortcuts import render
from rest_framework import viewsets
from Medical_App.serializers import CompanySerializers,CompanyBankSerializers,MedicineSerializer
from Medical_App.models import Company,CompanyBank,Medicine
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def list(self,request):
        company=Company.objects.all()
        serializer=CompanySerializers(company,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Company List Data","data":serializer.data}
        return Response(response_dict)
    
    def create(self,request):
        try:
            serializer=CompanySerializers(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Company Data Saving Successfully"}
        except:
            dict_response={"error":True,"message":"Error During  Saving Company Data Successfully"}
        return Response(dict_response)

    def update(sefl,request,pk=None):
        try:
            queryset=Company.objects.all()
            company = Company.objects.get(pk=pk)
            serializer=CompanySerializers(company,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Successfully Update Data"}
        except:
            dict_response={"error":True,"message":"Error During Update Data"}
        return Response(dict_response)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def list(self,request):
        company=CompanyBank.objects.all()
        serializer=CompanyBankSerializers(company,many=True,context={"request":request})
        response_dict={"error":False,"message":"All CompanyBank List Data","data":serializer.data}
        return Response(response_dict)
    
    
    def create(self,request):
        try:
            serializer=CompanyBankSerializers(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Company Bank Data Saving Successfully"}
        except:
            dict_response={"error":True,"message":"Error During  Saving Company Bank Data Successfully"}
        return Response(dict_response)


    def retrieve(self,request,pk=None):
            queryset=CompanyBank.objects.all()
            companybank=CompanyBank.objects.get(pk=pk)
            serializer=CompanyBankSerializers(companybank,context={"request":request})
            return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})
    
    def update(self,request,pk):
        try:
            companybank=CompanyBank.objects.get(pk=pk)
            serializer=CompanyBankSerializers(companybank,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Successfully Update Data"}
        except:
            dict_response={"error":True,"message":"Error During Update Data"}
        return Response(dict_response)


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializers
    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name=name)


class MedicineViewSet(viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def list(self,request):
        medicine=Medicine.objects.all()
        serializer=MedicineSerializer(medicine,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Medicine List Data","data":serializer.data}
        return Response(response_dict)
    
    
    def create(self,request):
        try:
            serializer=MedicineSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Medicine Data Saving Successfully"}
        except:
            dict_response={"error":True,"message":"Error During  Saving Medicine Data Successfully"}
        return Response(dict_response)


    def retrieve(self,request,pk=None):
            queryset=Medicine.objects.all()
            medicine=Medicine.objects.get(pk=pk)
            serializer=CompanyBankSerializers(medicine,context={"request":request})
            return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})
    
    def update(self,request,pk):
        try:
            medicine=Medicine.objects.get(pk=pk)
            serializer=CompanyBankSerializers(medicine,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Successfully Update Data"}
        except:
            dict_response={"error":True,"message":"Error During Update Data"}
        return Response(dict_response)




company_list=CompanyViewSet.as_view({"get":"list"})
company_create=CompanyViewSet.as_view({"post":"create"})
company_update=CompanyViewSet.as_view({"put":"update"})