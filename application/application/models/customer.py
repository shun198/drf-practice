import uuid

from django.db import models

from application.models.user import User


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kana = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="%(class)s_updated_by"
    )

    class Meta:
        db_table = "Customer"
