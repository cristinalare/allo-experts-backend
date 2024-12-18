from django.shortcuts import render
from rest_framework import generics,response,status
from .models import Mechanism
from .serializers import MechanismSerializer

class MechanismListAPIView(generics.ListAPIView):
  serializer_class=MechanismSerializer

  def get_queryset(self):
    return Mechanism.objects.filter(hidden=False)
  

class MechanismDetailAPIView(generics.GenericAPIView):
  serializer_class=MechanismSerializer


  def get(self,requst,slug):
    # md = markdown.Markdown(extensions=["fenced_code"])

    query_set= Mechanism.objects.filter(slug=slug, hidden=False).first()
    # query_set.description=md.convert(query_set.description)

    if query_set:
            serializer = self.serializer_class(query_set)
            return response.Response(serializer.data)
    return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)