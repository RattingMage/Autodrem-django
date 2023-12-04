from rest_framework.response import Response
from rest_framework.views import APIView
from .pusher import pusher_client


class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'sender': request.data['sender'],
            'text': request.data['text'],
        })

        return Response(request.data)