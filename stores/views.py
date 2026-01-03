from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()   # 👈 REQUIRED by DRF
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_profile = self.request.user.userprofile

        # Admin → all stores
        if user_profile.role.name == "Admin":
            return Store.objects.all()

        # User without store assigned → empty list (safe)
        if user_profile.store is None:
            return Store.objects.none()

        # Manager / Pharmacist → only their store
        return Store.objects.filter(id=user_profile.store.id)

    def create(self, request, *args, **kwargs):
        if request.user.userprofile.role.name != "Admin":
            return Response(
                {"detail": "Only Admin can create stores."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.userprofile.role.name != "Admin":
            return Response(
                {"detail": "Only Admin can delete stores."},
                status=status.HTTP_403_FORBIDDEN
            )

        store = self.get_object()
        store.is_active = False
        store.save()

        return Response(
            {"detail": "Store deactivated successfully."},
            status=status.HTTP_200_OK
        )
