import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 

from .choices import UserAuthorityChoices


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(BaseModel):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)


class MajorityShareHolder(BaseModel):
    has_consolidate_financial_report = models.BooleanField()
    is_ultimate_shareholder = models.BooleanField(null=True)



class Demand(BaseModel):
    country = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    company_number = models.CharField(max_length=200)
    vat_number = models.CharField(max_length=200, blank=True)
    application_fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(unique=True)
    user_authority = models.PositiveSmallIntegerField(
        choices=UserAuthorityChoices.choices
    )

    company_address = models.OneToOneField(
        Address, related_name="demand_company", on_delete=models.CASCADE
    )
    headquarters_address = models.OneToOneField(
        Address, related_name="demand_headquarter", on_delete=models.CASCADE, null=True
    )
    majority_shareholder = models.ForeignKey(
        MajorityShareHolder, on_delete=models.CASCADE
    )
