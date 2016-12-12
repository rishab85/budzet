from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .models import budgetCat
from .serializer import budgetCatSerializer

class budgetC(APIView):

    def get(self, request, format=None):
        cat = budgetCat.objects.all()
        serializer = budgetCatSerializer(cat, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = budgetCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class budgetCDetail(APIView):
    def get_object(self, pk):
        try:
            return budgetCat.objects.get(pk=pk)
        except budgetCat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cat = self.get_object(pk)
        serializer = budgetCatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cat = self.get_object(pk)
        serializer = budgetCatSerializer(due, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cat = self.get_object(pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

