from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""
    def get(self , request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[

        ]
        return Response({'message': 'Hello!' , 'an_apiview' :an_apiview})
