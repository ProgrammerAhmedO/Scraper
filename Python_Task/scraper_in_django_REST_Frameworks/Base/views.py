from django.shortcuts import render

# Create your views here.
# scraper/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapedData
from .serializers import ScrapedDataSerializer

class ScrapedDataListView(APIView):
    def get(self, request):
        queryset = ScrapedData.objects.all()
        
        # Filter based on query parameters
        title_contains = request.query_params.get('title_contains')
        if title_contains:
            queryset = queryset.filter(title__icontains=title_contains)
        
        # Serialize the filtered data
        serializer = ScrapedDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ScrapedDataDetailView(APIView):
    def get(self, request, pk):
        try:
            data = ScrapedData.objects.get(pk=pk)
        except ScrapedData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ScrapedDataSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

