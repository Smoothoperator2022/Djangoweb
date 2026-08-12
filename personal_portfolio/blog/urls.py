from django.urls import path
from . import views # 'dot' means from same folder

app_name = 'blog'

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('<int:article_id>/', views.detail, name='detail'), # any integer request from blog application: '3674567'
    #after 'per_port/url' "''" shows if nothing in than show 'all_blogs'
    # if i will add 'hello' instead of '', i need to write in site-url 'blog/hello'
]

