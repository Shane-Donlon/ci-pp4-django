from django.db import models

# Create your models here.


class Faq(models.Model):
    summary = models.CharField(max_length=500)
    details = models.TextField(max_length=5000)
    status_choices = [("Shown", "Shown"), ("Hidden", "Hidden")]
    status = models.CharField(
        max_length=50, choices=status_choices, null=True, default="Shown")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.summary}"
