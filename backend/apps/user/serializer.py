from rest_framework import serializers
from .models import Region, Address, User


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        region_data = validated_data.pop('region')
        region_instance, created = Region.objects.get_or_create(**region_data)
        address_instance = Address.objects.create(region=region_instance, **validated_data)
        return address_instance
    
class UserListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = User
        fields ='__all__'

''' 
   def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'rut': instance.rut,
            'email': instance.email,
            'address':{
                'region': instance.address.region.region_name,
                'street':instance.address.street,
                'number':instance.address.number
            }
        }
'''
class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_instance = address_serializer.save()

        password = validated_data.pop('password')
        user_instance = User.objects.create(address=address_instance, **validated_data)

        user_instance.set_password(password)
        user_instance.save()

        return user_instance
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)

        # Actualiza los campos en User
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()

        # Actualiza el campo address si se proporciona
        if address_data:
            address_instance = instance.address
            region_data = address_data.pop('region', None)
            if region_data:
                region_instance, created = Region.objects.get_or_create(**region_data)
                address_instance.region = region_instance

            for key, value in address_data.items():
                setattr(address_instance, key, value)

            address_instance.save()

        instance.save()
        return instance