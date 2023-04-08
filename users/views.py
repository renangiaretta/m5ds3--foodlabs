from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from addresses.models import Address


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        address_data = serializer.validated_data.pop('address')
        user_obj = User.objects.create(**serializer.validated_data)
        Address.objects.create(**address_data, user=user_obj)
        serializer = UserSerializer(user_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        return Response({'message': 'UPDATEUZRBYID'})

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        return Response({'message': 'DELETEUZRBYID'})
