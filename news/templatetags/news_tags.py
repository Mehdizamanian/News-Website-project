from django import template
from ..models import News , Category ,Tag


register = template.Library()


@register.simple_tag
def news_counter():
  news=str(News.objects.filter(active=1).count())
  return f"all avaliable News   :  {news} "


@register.filter
def upper(value):
  return value.upper()


@register.inclusion_tag('news/includes/news-recent.html')
def recent_news():
  news=News.objects.filter(active=True).order_by('-created_time')[0:2]  
  return {'news':news}


@register.filter
def lower(value):
  return value.lower()




@register.inclusion_tag('news/includes/news-category.html')
def categories():
  categories=Category.objects.all()
  news=News.objects.filter(active=True)
  categories_count={}

  for cat in categories:
    categories_count[cat]=news.filter(category__title=cat).count()

  return {'categories_count': categories_count}




@register.inclusion_tag('news/includes/news-recent.html')
def recent_post():
  news=News.objects.filter(active=True).order_by('-id')[:2]
  return {'news':news}


@register.inclusion_tag('news/includes/news-all-tags.html')
def show_all_tags():
  tags=Tag.objects.all()
  return {'tags':tags}





# Banner is for showing ctt on base.html

@register.inclusion_tag('news/includes/news-category-banner.html')
def category_banner():
  categories=Category.objects.all()
  return {'categories':categories}


@register.inclusion_tag('news/includes/banner/news-banner-recentnews.html')
def banner_recent_news():
  news=News.objects.filter(active=True).order_by('-id')[0:3]
  return {'news':news}



@register.inclusion_tag('news/includes/banner/news-banner-preview.html')
def banner_preview():
  news=News.objects.filter(active=True).order_by('-id')[0:4]
  return {'news':news}