from rest_framework import serializers
from Countries.models import Countries

#This class will manage serialization and deserialization from json
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Countries
        fields=('id','name','capital')