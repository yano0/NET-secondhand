from django.db import models

# Create your models here.
class Contents(models.Model):
    name = models.CharField(max_length=150)
    content = models.FileField(upload_to='uploads/%Y/%m/%d/', default='samples/sample_content.pdf')
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='samples/sample_cover.jpeg')

    def __str__(self):
        return self.name