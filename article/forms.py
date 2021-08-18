from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "article_subtitle", "content",
                  "article_category", "category_subtitle", "article_image"]
