from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from profiles.models import (Profile,
                             Recommendation,
                             Country)


class CountrySerializer(serializers.ModelSerializer):
    profiles_count = serializers.ReadOnlyField(source='profiles.count')

    class Meta:
        model = Country
        fields = ('id', 'name', 'profiles_count')


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        exclude = ('seen_at_conf', 'publish_date',)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    recommendations = RecommendationSerializer(many=True, read_only=True)

    brain_structure = MultipleChoiceField(choices=Profile.get_structure_choices(), allow_blank=True)
    modalities = MultipleChoiceField(choices=Profile.get_modalities_choices(), allow_blank=True)
    methods = MultipleChoiceField(choices=Profile.get_methods_choices(), allow_blank=True)
    domains = MultipleChoiceField(choices=Profile.get_domains_choices(), allow_blank=True)

    class Meta:
        model = Profile
        exclude = ('is_public', 'publish_date',)


class PositionsCountSerializer(serializers.ModelSerializer):
    profiles_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('position', 'profiles_count')
