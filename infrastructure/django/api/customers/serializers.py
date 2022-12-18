from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    birth_date = serializers.DateTimeField()
    document = serializers.CharField()
    email = serializers.CharField()
