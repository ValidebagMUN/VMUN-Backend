from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Institution(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=slugify(name))
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ["name"]


class Conference(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=slugify(name), unique=True)
    venue = models.CharField(max_length=200)
    host = models.ForeignKey(Institution, on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateField(default=timezone.now)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ["start"]


class Committee(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=slugify(name))
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ["slug"]
