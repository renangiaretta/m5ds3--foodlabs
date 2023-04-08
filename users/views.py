from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(**serializer.validated_data)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
