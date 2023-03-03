from django.shortcuts import render
from rest_framework import status, generics, viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def get_product(request):
    """
        Get all product
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_product(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListGenericView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateGenericView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductListCreateGenericView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # GET
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # POST
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def list(self, request, *args, **kwargs):
    #     return Response('hello')

class ProductMixin(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                #    mixins.UpdateModelMixin,
                #    mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ViewSet, ModelViewSet, mixins
