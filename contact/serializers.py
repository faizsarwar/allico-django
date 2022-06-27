from rest_framework import serializers
from .models import *

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('__all__')


class CatelogRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatelogRequest
        fields = ('__all__')