from rest_framework import generics
from geo.models import Country, Riddle
from .serializers import CountrySerializer, RiddleSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class CountryList(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
     
class AnswerList(generics.ListAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Country.objects.filter(status= 'correct')
    serializer_class = CountrySerializer
    

class RiddleRetrieve(generics.RetrieveAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Riddle.objects.all()
    serializer_class = RiddleSerializer


