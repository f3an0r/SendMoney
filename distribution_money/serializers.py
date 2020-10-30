from rest_framework import serializers
from .models import User


class DistributionMoneyFormSerializer(serializers.Serializer):
    inn = serializers.CharField(label='ИНН', max_length=100, style={'placeholder': 'ИНН', 'autofocus': True})
    summ = serializers.IntegerField(label='Сумма', style={'placeholder': 'Сумма'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users'] = serializers.ChoiceField(
            choices=[(choice.pk, choice.name) for choice in User.objects.all()]
        )

    def validate(self, data):
        # raise serializers.ValidationError("finish must occur after start")
        return data