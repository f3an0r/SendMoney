from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import DistributionMoneyFormSerializer
from .models import  User


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'distribution_form.html'

    def get(self, request):
        serializer = DistributionMoneyFormSerializer()
        users = User.objects.all()
        return Response({'serializer': serializer, 'users': users})

    def post(self, request):
        serializer = DistributionMoneyFormSerializer(data=request.data)
        msg = ''
        if serializer.is_valid():
            inns = serializer.validated_data.get("inn")
            user = User.objects.get(id=serializer.validated_data.get('users'))
            users = User.objects.filter(inn__in=inns)
            if users:
                # проверка что введенные ИНН есть в базе
                if users.count() != len(inns):
                    msg = 'Не все введенные ИНН есть в базе'
                    return JsonResponse(status=200, data={'msg': msg})
                summa = serializer.validated_data.get('summa')
                summa_for_user =  summa / users.count()
                if not user.get_money(summa):
                    msg = 'Не корректная сумма или недостаточно средств у пользователя'
                    return JsonResponse(status=200, data={'msg': msg})
                for user_for_refill in users:
                    user_for_refill.add_money(summa=summa_for_user)
                msg = 'Средства распределены'
            else:
                msg = 'Нет поьзователей с введеными inn'
        else:
            msg = 'Введены некорректные данные'
        return JsonResponse(status=200, data={'msg': msg})