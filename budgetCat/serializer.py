from rest_framework import serializers
from .models import budgetCat

class budgetCatSerializer(serializers.ModelSerializer):

        class Meta:
            model = budgetCat
            fields = '__all__'
