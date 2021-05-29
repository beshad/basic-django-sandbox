from django.db import models


class Content(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}, {self.password}"

    class Meta:
        verbose_name_plural = "Content"
        verbose_name_plural  =  "Contents"    
