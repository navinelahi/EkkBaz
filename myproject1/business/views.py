from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from .serializers import BusinessSerializer

@api_view(['POST'])
def register_business(request):
    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.gis.geos import Point
from rest_framework.decorators import api_view, permission_classes
from django.contrib.gis.db.models.functions import Distance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Business
from .serializers import BusinessSerializer
from rest_framework.permissions import IsAuthenticated

from django.contrib.gis.measure import D
from django.contrib.gis.geos import *
from business.models import Business


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Add this line for JWT token validation
def find_nearby_business(request):
    try:
        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))
        # user_location = Point(longitude, latitude, srid=4326)
        user_location = fromstr(f'POINT({longitude} {longitude})', srid=4326)
        print("User Location:", user_location)

        businesses = Business.objects.annotate(
            distance=Distance('coordinates', user_location)
        ).filter(distance__lte=2000*1000)

        # businesses = Business.objects.all()

        print("Found Businesses:", businesses)

        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)
    except (TypeError, ValueError) as e:
        print("Error:", e)
        return Response({"error": "Invalid latitude or longitude"}, status=400)
