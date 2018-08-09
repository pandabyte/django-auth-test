import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_view(request):
    return Response(json.dumps({'foo': 'bar'}))
