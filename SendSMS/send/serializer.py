from rest_framework import serializers
from .models import Send

class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Send
        fields = "__all__"