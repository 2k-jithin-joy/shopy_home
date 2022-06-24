from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import accessories
from django.urls import reverse

class feed_pro(Feed):
    title="shopy_home"
    link="/drcomments/"
    description="shopy_home is a shopping site"
    def items(self):
        pro=accessories.objects.all()[:5]
        return pro
    def item_title(self,item):
        
        return item.name
    def item_description(self,item):
        return truncatewords(item.desc,30)
    def item_link(self):
        return reverse("home page")
    