from rest_framework import serializers
from base.models import Student
from base.constants import MARK_CHOICES


class StudentSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(
        input_formats=['%d-%m-%Y', 'iso-8601'], format='%d-%m-%Y')

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'birth_date', 'mark')
