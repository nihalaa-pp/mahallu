from django.db import models

# Model to store basic information of a household
class Household(models.Model):

    panchayath = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    house_number = models.IntegerField()
    mahallu_number = models.CharField(max_length=20)
    mahallu_area = models.CharField(max_length=100)
    standard_of_living = models.CharField(
        max_length=10,
        choices=[('high', 'ഉയർന്നത്'), ('medium', 'ഇടത്തരം'), ('low', 'താഴ്ന്നത്')],
        default='medium'  # Add a default value here
    )
    head_of_household = models.CharField(max_length=100, default='Unknown')  # Add a default value here


# Model to store details of members in the household
class HouseholdMember(models.Model):
    # fields for HouseholdMember model
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    relationship_to_head = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    whatsapp_number = models.IntegerField()
    age = models.IntegerField()
    is_married = models.BooleanField(default=False)
    studying_course = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    education_qualification = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    country_of_job = models.CharField(max_length=100, blank=True, null=True)
    place_of_job = models.CharField(max_length=100, blank=True, null=True)
    job_sector = models.CharField(max_length=100, blank=True, null=True)
    job_experience = models.IntegerField(blank=True, null=True)
    is_government_employee = models.BooleanField(default=False)
    is_expat = models.BooleanField(default=False)
    is_entrepreneur = models.BooleanField(default=False)
    is_business_owner = models.BooleanField(default=False)
    is_looking_for_job = models.BooleanField(default=False)
    is_chronic_patient = models.BooleanField(default=False)
    chronic_disease_info = models.TextField(blank=True, null=True)
    is_differently_abled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.relationship_to_head}"
