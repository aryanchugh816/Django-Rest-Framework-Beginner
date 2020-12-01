from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    # First will make a serializer_class which is read by rest_framework on it's own
    serializer_class = serializers.HelloSerializer

    # Writing what happens on a get request
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Have to return a response in the form of a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hellow message with our name"""

        # Passing data to serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            # If data is not valid we will send a 400 code
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
