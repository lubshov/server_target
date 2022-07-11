from .models import ListeningResponses
from rest_framework import viewsets, permissions
from .serializers import ListeningResponsesSerializer

import time





# Category ViewSet
class ListeningResponseViewSet(viewsets.ModelViewSet):
    queryset = ListeningResponses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListeningResponsesSerializer
