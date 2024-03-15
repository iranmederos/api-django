from .models import User, Role
from rest_framework.serializers import ModelSerializer


class SerializerRole(ModelSerializer):
    class Meta:
        model=Role
        fields="__all__"


class SerializerUser(ModelSerializer):
    class Meta:
        model=User
        fields=('id','email','password','nombre','telefono','rol')

    def create(self, validated_data):
        password= validated_data.pop('password', None) #extraemos el password de la informacion recibida
        instance= self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance
        

        
    

    