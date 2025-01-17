# serialize data to render
# convert objects into data types render function can understand

from rest_framework import serializers
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'