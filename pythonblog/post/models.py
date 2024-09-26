from django.db import models

# Blog Status Draft and Publish
# B_STATUS = [
#     ('DRAFT', 'DRAFT'),
#     ('PUBLISH', 'PUBLISH'),
# ]

# Create your models here.
class Article(models.Model):
    # Second Way to define choices
    class Status(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISH = 'Publish'
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    # status = models.CharField(max_length=8,choices = B_STATUS,default = 'DRAFT' )
    status = models.CharField(max_length=50, choices=Status.choices, default = Status.DRAFT)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.title}"