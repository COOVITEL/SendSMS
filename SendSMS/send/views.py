from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Send
from .serializer import SendSerializer
from .sendSMS import soap_sms

class SendViews(viewsets.ModelViewSet):
    """"""
    serializer_class = SendSerializer
    queryset = Send.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            send_instance = serializer.save()
            phone = send_instance.phone
            city = send_instance.city
            turn = send_instance.turn
            soap_sms(phone, turn, city)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)