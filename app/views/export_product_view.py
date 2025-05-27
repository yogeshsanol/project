from django.http import HttpResponse
from rest_framework import generics
from app.models.product import Product
import csv
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class ExportProductView(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication,TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(['title', 'description','price','status','category_id','created_at','updated_at'])

        users = Product.objects.all().values_list('title', 'description','price','status','category_id','created_at','updated_at')
        for user in users:
            writer.writerow(user)

        return response
            