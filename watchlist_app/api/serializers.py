from rest_framework import serializers
from watchlist_app.models import Movie

def dis_length(value): # validation with validator
    if len(value) < 4:
        raise serializers.ValidationError("discriton is too short")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[dis_length])
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    def validate(self,data):  #object level validation
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and descrption should not be same")
        else:
            return data

    def validate_name(self,value): # field level vaidation

        if len(value)<2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
