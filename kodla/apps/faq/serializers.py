# Third-Party
from rest_framework import serializers

# Local Django
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'answer', )
