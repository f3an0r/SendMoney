from rest_framework import serializers
from .models import User


class DistributionMoneyFormSerializer(serializers.Serializer):
    inn = serializers.CharField(label='ИНН', max_length=400, style={'placeholder': 'ИНН', 'autofocus': True},
                                help_text="Введите ИНН через запятую ','")
    summa = serializers.DecimalField(max_digits=50, decimal_places=2, label='Сумма', style={'placeholder': 'Сумма'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users'] = serializers.ChoiceField(
            label='Пользователь',
            help_text='Выберите пользователя со счета которого необходимо списать средства',
            choices=[(choice.pk, choice.name) for choice in User.objects.all()]
        )

    def validate(self, data):
        inns = data.get('inn', None)
        data['inn'] = list()
        try:
            for inn in inns.split(','):
                if inn.strip():
                    data['inn'].append(int(inn))
                else:
                    continue
        except:
            raise serializers.ValidationError("inn is not valid")
        return data

