from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from telegram.serializer import CountrySerializer
from telegram.models import Country
from telegram.telgram_msg import regular_update_task
# Create your views here.

class CountryLatestView(GenericAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get(self, request,**kwargs):
        params = request.query_params
        country_name = params.get("country")
        if not country_name:
            return Response({"message":"Provide Country name"},status=status.HTTP_400_BAD_REQUEST)
        country = self.queryset.filter(name=country_name).latest("date")
        serializer = self.get_serializer(country)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

class CountryView(GenericAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get(self, request,**kwargs):
        params = request.query_params
        country_name = params.get("country")
        if not country_name:
            return Response({"message":"Provide Country name"},status=status.HTTP_400_BAD_REQUEST)

        sort = params.get("sort","date")
        countries = self.queryset.filter(name=country_name).order_by(sort)
        if len(countries)>1:
            serializer = self.get_serializer(countries, many=True)
        else:
            serializer = self.get_serializer(countries)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

    def put(self,request):
        try:
            regular_update_task()
        except Exception:
            pass
        return Response({"Succussfully updated"},status=status.HTTP_201_CREATED)