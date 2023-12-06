from rest_framework.response import Response
from rest_framework.views import APIView
from .pusher import pusher_client


class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger(f'chat-{request.data["chat_id"]}', 'message', {
            'sender': request.data['sender'],
            'text': request.data['text'],
            'chat_id': request.data['chat_id'],
        })

        return Response(request.data)