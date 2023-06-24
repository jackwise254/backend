from rest_framework import serializers
from .models import Property
from users.serializers import UserSerializer

class PropertySerializer(serializers.ModelSerializer):
    agent = UserSerializer() # Include the UserSerializer here

    class Meta:
        model = Property
        fields = '__all__'

# class ReactionsSerializer(serializers.ModelSerializer):
#     agent = UserSerializer()
#     properties = PropertySerializer()

#     class Meta:
#         model = Reactions
#         fields = '__all__'