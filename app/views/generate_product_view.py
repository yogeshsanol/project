from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from app.tasks import generate_product_task
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class GenerateProductView(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication,TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user_input_number = request.data.get('number', 0)  
        generate_product_task(user_input_number)
        # Start the Redis server if want to use delay method of celery
        #generate_product_task.delay(user_input_number)
        return Response({"message": "Product generation started"}, status=status.HTTP_202_ACCEPTED)