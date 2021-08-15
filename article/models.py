from os import read
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField

from django.shortcuts import reverse
# Create your models here.


class Article(models.Model):

    category = (

        ('Bilim', 'Bilim'),
        ('Teknoloji', 'Teknoloji'),
        ('Spor', 'Spor'),
        ('Kültür', 'Kültür'),
        ('Sanat', 'Sanat'),

    )

    subtitle = (
        ('Sağlık', 'Sağlık'),
        ('Araba', 'Araba'),
        ('Futbol', 'Futbol'),
        ('Film', 'Film'),
        ('Yazılım', 'Yazılım')
    )

    author = models.ForeignKey(
        "userprofile.UserAccount", on_delete=models.CASCADE, verbose_name="Yazar ")
    title = models.CharField(max_length=150, verbose_name="Başlık")
    article_subtitle = models.TextField(
        max_length=250, verbose_name="Alt Metin")

    content = RichTextUploadingField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    article_category = models.CharField(
        max_length=20, choices=category, default='Bilim', verbose_name="Makale Kategori")
    category_subtitle = MultiSelectField(choices=subtitle)

    article_image = models.FileField(
        blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    likes = models.ManyToManyField(
        "userprofile.UserAccount", related_name="likes", blank=True
    )
    favourite = models.ManyToManyField(
        "userprofile.UserAccount", related_name="favourite", blank=True
    )
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_read(self):
        return self.read.count()

    def get_absolute_url(self):
        return reverse("article:detail", args=[self.id])

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_photo = models.FileField(
        blank=True, null=True, verbose_name="Yoruma Fotograf Ekleyin"
    )
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = RichTextUploadingField("Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    def get_absolute_url(self):
        return reverse("article:detail", args=[self.id])

    def total_likes(self):
        return self.comment_likes.count()

    class Meta:
        ordering = ['-comment_date']


# class Reply(models.Model):

#     comment = models.ForeignKey(
#         Comment, on_delete=models.CASCADE, verbose_name="Yorum", related_name="comments")
#     reply_content = RichTextField("Yanıt")
#     reply_author = models.CharField(max_length=50, verbose_name="İsim")
#     reply_date = models.DateTimeField(auto_now_add=True)
#     reply_photo = models.FileField(
#         blank=True, null=True, verbose_name="Yanıta Fotograf Ekleyin"
#     )
