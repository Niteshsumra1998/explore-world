from django.db import models

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='package_images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
