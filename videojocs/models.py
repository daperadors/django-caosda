from django.db import models
class platform(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['name', 'date']
    def __str__(self):
        return "%s the user" % self.name