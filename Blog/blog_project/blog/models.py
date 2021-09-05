from django.db import models

class post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField(null=True)


    def __str__(self):
        return self.title


