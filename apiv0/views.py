from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from technique.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
# Create your views here.


def test_api_view(request):
    first_technique = technique.objects.first()
    f_b = {
        'name': first_technique.name,
        'company': [item.salutation for item in first_technique.company.all()],
        'price': first_technique.price.name,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def technique_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=techniqueSerializer(instance=technique.objects.all(), many=True).data, status=200)
        else:
            the_technique = get_object_or_404(technique, pk=pk)
            return Response(data=techniqueSerializer(instance=the_technique).data, status=200)
    
    elif request.method == "POST":
        sb = techniqueSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_technique = get_object_or_404(technique, pk=pk)
        sb = techniqueSerializer(data=request.data, instance=the_technique)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_technique = get_object_or_404(technique, pk=pk)
        the_technique.delete()
        return Response('Deleted', status=200)


class techniqueListAPIView(ListAPIView):
    queryset = technique.objects.all()
    serializer_class = techniqueSerializer


class techniqueCreateAPIView(CreateAPIView):
    queryset = technique.objects.all()
    serializer_class = techniqueSerializer


class techniqueUpdateAPIView(UpdateAPIView):
    queryset = technique.objects.all()
    serializer_class = techniqueSerializer


class techniqueDestroyAPIView(DestroyAPIView):
    queryset = technique.objects.all()
    serializer_class = techniqueSerializer





@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Brand_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=BrandSerializer(instance=Brand.objects.all(), many=True).data, status=200)
        else:
            the_Brand = get_object_or_404(Brand, pk=pk)
            return Response(data=BrandSerializer(instance=the_Brand).data, status=200)
    
    elif request.method == "POST":
        sb = BrandSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Brand = get_object_or_404(Brand, pk=pk)
        sb = BrandSerializer(data=request.data, instance=the_Brand)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Brand = get_object_or_404(Brand, pk=pk)
        the_Brand.delete()
        return Response('Deleted', status=200)


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDestroyAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def size_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=sizeSerializer(instance=size.objects.all(), many=True).data, status=200)
        else:
            the_size = get_object_or_404(size, pk=pk)
            return Response(data=sizeSerializer(instance=the_size).data, status=200)
    
    elif request.method == "POST":
        sb = sizeSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_size = get_object_or_404(size, pk=pk)
        sb = sizeSerializer(data=request.data, instance=the_size)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_size = get_object_or_404(size, pk=pk)
        the_size.delete()
        return Response('Deleted', status=200)


class sizeListAPIView(ListAPIView):
    queryset = size.objects.all()
    serializer_class = sizeSerializer


class sizeCreateAPIView(CreateAPIView):
    queryset = size.objects.all()
    serializer_class = sizeSerializer


class sizeUpdateAPIView(UpdateAPIView):
    queryset = size.objects.all()
    serializer_class = sizeSerializer


class sizeDestroyAPIView(DestroyAPIView):
    queryset = size.objects.all()
    serializer_class = sizeSerializer







@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Company_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CompanySerializer(instance=Company.objects.all(), many=True).data, status=200)
        else:
            the_Company = get_object_or_404(Company, pk=pk)
            return Response(data=CompanySerializer(instance=the_Company).data, status=200)
    
    elif request.method == "POST":
        sb = CompanySerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Company = get_object_or_404(Company, pk=pk)
        sb = CompanySerializer(data=request.data, instance=the_Company)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Company = get_object_or_404(Company, pk=pk)
        the_Company.delete()
        return Response('Deleted', status=200)


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDestroyAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



