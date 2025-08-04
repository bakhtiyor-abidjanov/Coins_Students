from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=255)

    def name(self):
        return self.fullname.split()[0]

    def surname(self):
        return self.fullname.split()[1] if len(self.fullname.split()) > 1 else ""

    def __str__(self):
        return self.fullname