
from rest_framework import serializers

from .models import Profile, Country


class CountrySerializer(serializers.ModelSerializer):
    profiles_count = serializers.ReadOnlyField(source='profile_set.count')

    class Meta:
        model = Country
        fields = ('id', 'name', 'profiles_count')


class PositionsCountSerializer(serializers.ModelSerializer):
    profiles_count = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ('position', 'profiles_count')
