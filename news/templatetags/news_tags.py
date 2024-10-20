from django import template
from ..models import News , Category


register = template.Library()


@register.simple_tag
def news_counter():
  news=str(News.objects.filter(active=1).count())
  return f"all News avaliable  :  {news} "


@register.filter
def upper(value):
  return value.upper()


@register.inclusion_tag('news/includes/news-recent.html')
def recent_news():
  # news=News.objects.filter(active=1).order_by('-created_time')[0:2]  # didnt work by created 
  news=News.objects.filter(active=1).order_by('-id')[0:2]
  return {'news':news}


@register.filter
def lower(value):
  return value.lower()

# @register.simple_tag
# def show_news():
#     news=News.objects.filter(active=True)
#     newstostring=str(news)
#     return f"all News({news})"


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



# @register.inclusion_tag('news/includes/news-category.html')
# def category():
#   categories=Category.objects.all()
#   return {'categories':categories}
