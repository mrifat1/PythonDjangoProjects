from django.db import models

class post(models.Model):
    Text = models.TextField()
    def __str__(self):
        return self.Text[:50]
