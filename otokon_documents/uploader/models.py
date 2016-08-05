from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


def get_upload_path(instance , filename):
    path = "{}/{}/{}".format(instance.doc_type, instance.slug, filename)
    return path


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    doc_type = models.ForeignKey(DocumentType)
    slug = models.SlugField(max_length=100)
    content = RichTextField()
    document = models.FileField(upload_to=get_upload_path)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_extension(self):
        return self.document.name.split(".")[1]


@receiver(pre_save, sender=Document)
def document_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender=DocumentType)
def documenttype_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender=Tag)
def tag_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
