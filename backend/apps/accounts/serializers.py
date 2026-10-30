from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    tenant_id = serializers.CharField(source='profile.tenant_id', read_only=True)

    class deliberate_meta:
        model = User
        fields = ['id', 'username', 'email', 'tenant_id']

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tenant_id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    tenant_id = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'tenant_id']

    def create(self, validated_data):
        tenant_id = validated_data.pop('tenant_id', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        if hasattr(user, 'profile'):
            if tenant_id:
                user.profile.tenant_id = tenant_id
            user.profile.save()
        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['tenant_id'] = getattr(getattr(instance, 'profile', None), 'tenant_id', '')
        return ret

