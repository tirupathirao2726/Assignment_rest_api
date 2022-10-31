from rest_framework import serializers
from .models import user_info

class user_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_info
        fields=['id','First_Name','Last_Name','Email']
