from django.shortcuts import render
from rest_framework import generics

from authors.models import Author
from authors.serializers import AuthorSerializer
# Create your views here.


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
