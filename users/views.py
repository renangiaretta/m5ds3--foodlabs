from rest_framework.views import APIView, Request, Response, status


class UserView(APIView):
    def get(self, request: Request) -> Response:
        return Response({'msg': 'hue'})
