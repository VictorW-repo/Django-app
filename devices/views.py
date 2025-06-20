from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from .serializers import PayloadSerializer


class PayloadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PayloadSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                payload = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'Duplicate payload. This fCnt already exists for this device.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)