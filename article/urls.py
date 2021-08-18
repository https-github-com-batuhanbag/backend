from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [

    path('article/<int:id>', views.detail, name="detail"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment"),
    # path('reply/<int:id>', views.addReply, name="reply"),
    path('like/<int:id>', views.like_post_article, name="like_post"),
    path('favourite_post/<int:id>', views.favourite_post, name="favourite_post"),
    path('favourite_list/', views.favourite_list, name="favourite_list"),
    path('science/', views.category_science, name="category_science"),
    path('culture/', views.category_culture, name="category_culture"),
    path('technology/', views.category_technology, name="category_technology"),
    path('art/', views.category_art, name="category_art"),
    path('sport/', views.category_sport, name="category_sport"),
    path('editordashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addArticle"),

]
