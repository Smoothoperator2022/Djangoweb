from django.shortcuts import render, get_object_or_404 #allows to find object via propper name or show 404 mistake
from .models import Article
# in this file i`ll translate object on web page

# Create your views here.
def all_articles(request): #article_count = Article.objects.count
    articles = Article.objects.all() # order_by('-pub_date') [:5] sort objects by latest date and till 5
    return render(request, 'blog/all_articles.html', {'articles': articles})

def detail(request, article_id):
    article = get_object_or_404 (Article, pk=article_id) #this func try to search object with propper number
    return render (request, 'blog/detail.html', {'article':article})