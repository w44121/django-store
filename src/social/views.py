from rest_framework import views, status
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review


class ReviewView(views.APIView):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product__id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        request.data.update({'product': product_id, 'user': request.user.id})
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
