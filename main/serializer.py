from rest_framework import serializers
from main.models import *

serializer = serializers.ModelSerializer 

class InfoSerializer(serializer):
    class Meta:
        model = Info
        fields = "__all__"

class ClientSerializer(serializer):
    class Meta:
        model = Client
        fields = "__all__"



class ClientSerializer(serializer):
    class Meta:
        model = Client
        fields = "__all__"

class BenzinSerializer(serializer):
    class Meta:
        model = Benzin
        fields = "__all__"

class BenzinProductionSerializer(serializer):
    class Meta:
        model = BenzinProduction
        fields = "__all__"

class CashSerializer(serializer):
    class Meta:
        model = Cash
        fields = "__all__"

class PaySerializer(serializer):
    class Meta:
        model = Pay
        fields = "__all__"

class NewsSerializer(serializer):
    class Meta:
        model = News
        fields = "__all__"
