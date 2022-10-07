from .models import Krosovka
from rest_framework import serializers

class KrsaovkaAPI(serializers.ModelSerializer):
    class Meta:
        model = Krosovka
        fields = '__all__'