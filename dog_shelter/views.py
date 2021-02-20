from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Dog, Breed, Curator, Payment
from .serializers import DogSerializer, BreedSerializer, CuratorSerializer, PaymentSerializer


class DogViewSet(viewsets.ModelViewSet):

    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def check_object_permissions(self, request, obj):
        check_object_permissions_common(self, request, obj, obj.fixed)


class BreedViewSet(viewsets.ModelViewSet):

    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class CuratorViewSet(viewsets.ModelViewSet):

    serializer_class = CuratorSerializer
    queryset = Curator.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dog = serializer.validated_data['dog']
        if dog.fixed:
            self.permission_denied(request, message='The dog is fixed.')

        else:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def check_object_permissions(self, request, obj):
        check_object_permissions_common(self, request, obj, obj.dog.fixed)


def check_object_permissions_common(viewset, request, obj, permission_dog_fixed):

    if permission_dog_fixed:
        viewset.http_method_names = ['get', 'head', 'options']

        if request.method.lower() not in viewset.http_method_names:
            viewset.permission_denied(request, message='Dog is fixed.')

    """
    Check if the request should be permitted for a given object.
    Raises an appropriate exception if the request is not permitted.
    """
    for permission in viewset.get_permissions():
        if not permission.has_object_permission(request, viewset, obj):
            viewset.permission_denied(
                request, message=getattr(permission, 'message', None)
            )
