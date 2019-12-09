from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField
from rest_framework.validators import UniqueTogetherValidator

from ..models import (Profile,
                      Recommendation,
                      Country)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name')


class ProfileBasicDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'name', 'institution']


class RecommendationBasicDetailsSerializer (serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        exclude = ['id', 'profile']


class RecommendationSerializer(serializers.ModelSerializer):
    profile = ProfileBasicDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = Recommendation
        exclude = ('publish_date', 'last_updated')
        validators = [
            UniqueTogetherValidator(
                queryset=Recommendation.objects.all(),
                fields=['profile', 'reviewer_name', 'reviewer_institution'],
                message='You have already recommended that person!'
            )
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)
    recommendations = RecommendationBasicDetailsSerializer(many=True, read_only=True)
    # country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), many=False)

    brain_structure = MultipleChoiceField(choices=Profile.get_structure_choices(), allow_blank=True)
    modalities = MultipleChoiceField(choices=Profile.get_modalities_choices(), allow_blank=True)
    methods = MultipleChoiceField(choices=Profile.get_methods_choices(), allow_blank=True)
    domains = MultipleChoiceField(choices=Profile.get_domains_choices(), allow_blank=True)

    class Meta:
        model = Profile
        exclude = ('is_public', 'publish_date',)
        depth = 1


class ProfilesCountByPositionSerializer(serializers.ModelSerializer):
    profiles_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('position', 'profiles_count')


class ProfilesCountByCountrySerializer(serializers.ModelSerializer):
    profiles_count = serializers.ReadOnlyField(source='profiles.count')

    class Meta:
        model = Country
        fields = ('id', 'name', 'profiles_count')
