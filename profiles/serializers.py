
from rest_framework import serializers

from .models import Profile, Country, Recommendation


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('id', 'name', 'position', 'country')


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


class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('reviewer_name', 'profile', 'comment')
