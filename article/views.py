from urllib.parse import quote_plus
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from article.forms import ArticleForm
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

    print(request.COOKIES)

    articles = Article.objects.all()

    slider_item = Article.objects.all()[:5]

    science_count = Article.objects.filter(
        article_category__contains="Bilim").count()

    sport_count = Article.objects.filter(
        article_category__contains="Spor").count()

    culture_count = Article.objects.filter(
        article_category__contains="Kültür").count()

    art_count = Article.objects.filter(
        article_category__contains="Sanat").count()

    technology_count = Article.objects.filter(
        article_category__contains="Teknoloji").count()

    week_ago = datetime.date.today() - datetime.timedelta(days=30)
    trends = Article.objects.filter(
        created_date__gte=week_ago).order_by('-read')

    context = {
        "articles": articles,
        "slider_item": slider_item,
        "science_count": science_count,
        "art_count": art_count,
        "culture_count": culture_count,
        "sport_count": sport_count,

        "technology_count": technology_count,
        "trends": trends[:5],
    }

    return render(request, "index.html", context)


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


@login_required(login_url="userprofile:login")
def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.user.fullName
        comment_content = request.POST.get("comment_content")
        comment_photo = request.user.account_avatar

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content,
                             comment_photo=comment_photo)

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


def cookie(request):
    pass

# TO-DO

# def like_comment(request, id):

#     comment = get_object_or_404(Comment, id=id)

#     is_liked = False

#     if comment.comment_likes.filter(id=request.user.id):
#         comment.comment_likes.remove(request.user)
#         is_liked = False

#     else:
#         comment.comment_likes.add(request.user)
#         is_liked = True

#     return HttpResponseRedirect(comment.get_absolute_url())


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

    if user.is_authenticated:
        user = request.user

        favourite_posts = user.favourite.all()

        context = {
            'favourite_posts': favourite_posts
        }
    else:
        messages.error(request, "Lütfen giriş yapıp tekrar deneyiniz.")
        return redirect("index")

    return render(request, "favourites.html", context)


def category_science(request):
    return render(request, "categories/science.html")


def category_sport(request):
    return render(request, "categories/sport.html")


def category_technology(request):
    return render(request, "categories/technology.html")


def category_art(request):
    return render(request, "categories/art.html")


def category_culture(request):
    return render(request, "categories/culture.html")


def dashboard(request):

    user = request.user

    if user.is_authenticated and request.user.account_type == "accType2":
        articles = Article.objects.filter(author=request.user)
        context = {
            "articles": articles
        }

        return render(request, "editorPage.html", context)

    else:
        messages.error(
            request, "Bu sayfaya girmeye yetkiniz yeterli değildir, iyi okumalar dileriz.")
        return redirect("index")


def addArticle(request):

    user = request.user

    if user.is_authenticated and request.user.account_type == "accType2":

        form = ArticleForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            messages.success(request, "Yazınız Başarıyla Oluşturuldu")
            return redirect("article:dashboard")

        return render(request, "addarticle.html", {"form": form})

    else:

        messages.error(
            request, "Bu sayfaya girmeye yetkiniz yeterli değildir, iyi okumalar dileriz.")
        return redirect("index")


def updateArticle(request, id):

    user = request.user

    if user.is_authenticated and request.user.account_type == "accType2":

        article = get_object_or_404(Article, id=id)

        form = ArticleForm(request.POST or None,
                           request.FILES or None, instance=article)

        if form.is_valid():
            article = form.save(commit=False)

            article.author = request.user

            article.save()

            messages.success(request, "Yazınız Başarıyla Güncellendi.")
            return redirect("article:dashboard")
        return render(request, "updateArticle.html", {"form": form})
    else:
        messages.error(
            request, "Bu sayfaya girmeye yetkiniz yeterli değildir, iyi okumalar dileriz.")
        return redirect("index")


def deleteArticle(request, id):

    user = request.user

    if user.is_authenticated and request.user.account_type == "accType2":

        article = get_object_or_404(Article, id=id)

        article.delete()

        messages.success(request, "Makale Başarıyla Silindi")

        return redirect("article:dashboard")

    else:
        messages.error(
            request, "Bu sayfaya girmeye yetkiniz yeterli değildir, iyi okumalar dileriz.")
        return redirect("index")
