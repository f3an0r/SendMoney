from django.shortcuts import get_object_or_404
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
        print(request.data)
        if serializer.is_valid():
            print("data is valid")
            print(serializer.data)
        print("Before responce")
        return JsonResponse(status=200, data={'msg': "send money id successful"})