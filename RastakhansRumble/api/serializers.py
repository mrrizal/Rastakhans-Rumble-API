from api.models import Card
from rest_framework_mongoengine import serializers


class CardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Card
        fields = "__all__"
