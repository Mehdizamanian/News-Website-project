from django import template
from news.models import News , Category


register = template.Library()




@register.simple_tag
def mycustom_tag():
    return "Recent News"



@register.inclusion_tag('news/includes/news-recent.html')
def recent_post():
  news=News.objects.filter(active=True).order_by('-id')[:2]
  return {'news':news}



# @register.inclusion_tag('news/includes/news-category.html')
# def category():
#   categories=Category.objects.all()
#   return {'categories':categories}
