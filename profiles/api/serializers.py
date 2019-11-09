from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from profiles.models import (DOMAINS_CHOICES,
                             METHODS_CHOICES,
                             MODALITIES_CHOICES,
                             STRUCTURE_CHOICES,
                             Profile,
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
    recommendations = RecommendationSerializer(many=True, read_only=True)

    brain_structure = MultipleChoiceField(choices=STRUCTURE_CHOICES, allow_blank=True)
    modalities = MultipleChoiceField(choices=MODALITIES_CHOICES, allow_blank=True)
    methods = MultipleChoiceField(choices=METHODS_CHOICES, allow_blank=True)
    domains = MultipleChoiceField(choices=DOMAINS_CHOICES, allow_blank=True)

    class Meta:
        model = Profile
        # exclude = ('publish_date',)
        exclude = ('user', 'publish_date',)


class PositionsCountSerializer(serializers.ModelSerializer):
    profiles_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('position', 'profiles_count')
