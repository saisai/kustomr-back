from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework import generics
from .serializers import UserSerializer
from Vendor.serializers import VendorFullSerializer


class CurrentUser(APIView):
    """
    View to get the current user's info
    """

    def get(self, request, format=None):
        if request.user.is_authenticated:
            response = {}
            response['user'] = UserSerializer(request.user).data
            if request.user.is_vendor:
                response['vendor'] = VendorFullSerializer(request.user.vendor).data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Aucun utilisateur connecté.'}, status=status.HTTP_403_FORBIDDEN)
