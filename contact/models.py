from django.db import models

# Create your models here.
class ContactForm(models.Model):
    Name = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    CompanyName = models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    Message = models.TextField(max_length=255,default=None)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.Name


# Create your models here.
class CatelogRequest(models.Model):
    Name = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    CompanyName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Application = models.CharField(max_length=255)
    Message = models.TextField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.Name
