from urllib.parse import quote_plus
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .models import Article, Comment
import datetime
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)

    current_detail = article
    share_string = quote_plus(article.content)
    url = "http://localhost:8000" + article.get_absolute_url()

    article.read += 1

    article.save()

    week_ago = datetime.date.today() - datetime.timedelta(days=45)

    sideArticle = Article.objects.filter(created_date__gte=week_ago).order_by(
        '-read').exclude(title=current_detail)[:3]

    is_liked = False
    is_favourite = False

    if article.likes.filter(id=request.user.id):
        is_liked = True

    if article.favourite.filter(id=request.user.id):
        is_favourite = True

    comments = article.comments.all()

    context = {
        'article': article,
        'comments': comments,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'total_likes': article.total_likes(),
        'sideArticle': sideArticle,
        'url': url,
        'share_string': share_string,
    }

    return render(request, "detail.html", context)


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))


@login_required(login_url="userprofile:login")
def like_post_article(request, id):

    post = get_object_or_404(Article, id=id)

    is_liked = False

    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url="userprofile:login")
def favourite_post(request, id):

    post = get_object_or_404(Article, id=id)

    if post.favourite.filter(id=request.user.id):
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)

    return HttpResponseRedirect(post.get_absolute_url())


def favourite_list(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    user = request.user

    favourite_posts = user.favourite.all()

    context = {
        'favourite_posts': favourite_posts
    }

    return render(request, "favourites.html", context)
