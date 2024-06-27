from rest_framework.serializers import ModelSerializer
from register.models import Register


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
