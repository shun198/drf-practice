import uuid

from django.db import models

from application.utils.customer_storage import CustomerStorage


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kana = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Customer"


class CustomerPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="customer_photo", storage=CustomerStorage())
