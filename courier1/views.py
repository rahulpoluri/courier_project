
from urllib import response
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import authentication
from .models import Package_Category, Package_Sizes
from .authentication import *

# Create your views here.

class Get_Quote(APIView):
    # authentication_classes = (QuietBasicAuthentication)
    # serializer_class = Package_SizesSerializer
    #
    # # def get(self, request):
    # #     # print(request.query_params)
    # #     data = request.query_params
    # #
    # #     # print(request.data)
    # #
    # #     quotes = list(Package_Sizes.objects.all().values_list('size', flat=True))
    # #     # print(quotes)
    # #     if data.get("Package_size") in quotes:
    # #         pass
    # #     serializer = Package_SizesSerializer(quotes, many=True)
    # #     return Response(200)
    #
    # def post(self, request):
    #     return Response(self.serializer_class(request.user).data)

    def get(self,request):
        data = dict(request.query_params)
        print(data)

        # checking if all params are available
        required_params = ["Source_pincode", "Destination_pincode", "Package_size", "Category", "Package_value"]
        for i in required_params:
            if i not in data.keys():
                return Response(data=f"Missing required parameter {i}", status=400)

        # extracting data
        size = data.get('Package_size')[0]
        category = data.get('Category')[0]
        package_value = data.get('Package_value')[0]

        # checking for given package size available
        available_sizes = list(Package_Sizes.objects.all().values_list('size', flat=True))
        size_found = [1 for i in available_sizes if size.lower() == i.lower()]
        row = Package_Sizes.objects.get(size=size)
        bill_amount = row.bill_amount
        if not size_found:
            return Response(data=f"Please give appropriate package size value", status=400)

        # checking if given category available
        available_category = list(Package_Category.objects.all().values_list('category', flat=True))
        category_found = [1 for i in available_category if category.lower() == i.lower()]
        if not category_found:
            return Response(data=f"Please give appropriate category value", status=400)

        # checking if package value is more than 50000
        try:
            package_value = int(package_value)
        except:
            return Response(data=f"Please give integer package value", status=400)

        if package_value > 50000:
            return Response(data=f"Package value should not be more than 50000", status=400)

        return Response(200)


