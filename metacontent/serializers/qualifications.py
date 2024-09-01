from rest_framework import serializers
from metacontent.models.qualification import Qualification


class QualificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = (
            'id',
            'qualification'
        )