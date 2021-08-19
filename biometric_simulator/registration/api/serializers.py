from rest_framework import serializers
from registration.models import Register

#Serializador para el modelo de Register
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

    def create(self,validated_data):
        register = Register(**validated_data)
        register.save()
        return register

    def update(self,instance,validated_data):
        updated_register = super().update(instance,validated_data)
        updated_register.save()
        return updated_register

class RegisterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'date': instance['date'],
            'time': instance['time'],
            'fingerprint': instance['fingerprint']
        }