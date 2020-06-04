from rest_framework import serializers


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    redirect_url = serializers.CharField(required=True)
