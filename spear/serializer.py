from rest_framework import serializers
from spear.models import Question

class SpearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'