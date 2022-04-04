from django.shortcuts import render
from django.db import models
from django.forms import ModelChoiceField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from wagtail.contrib.routable_page.models import RoutablePageMixin,route
from streams import blocks




# Create your models here.
class BlogListingPage(RoutablePageMixin,Page):
    """ LIsting PAge"""

    template = "blog/blog_list_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null= False,
        help_text= " Overrigth defuat Title")

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]
    
    def get_context(self, request, *args, **kargs):
        context = super().get_context(request, *args,**kargs)
        context["posts"]= BlogDetailPage.objects.live().public()
        # context["a_special_link"] = self.reverse_subpage('latest_posts')
        return context

    @route(r'^latest/$', name='latest_posts')
    def latest_blog_post(self,request,*args,**kwargs):
        context = self.get_context(request,*args,**kwargs)
        # context["latest_posts"] = BlogDetailPage.objects.live().public()[:1]
        # context["name"] = "MAnju Ghorse"
        # context["website"] = "Learnwagtail.com"
        context['posts'] = context['posts'][:1]
        return render(request, "blog/latest_posts.html", context)

    def get_sitemap_urls(self, request):
        # return []
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
            "location" : self.full_url + self.reverse_subpage("latest_posts"),
            "lastmod": (self.last_published_at or self.latest_revision_created_at),
            "priority" :0.9,
            }
            )
        return sitemap

class BlogDetailPage(Page):
    """ Blog Detail Page"""
    template = "blog/blog_detail_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank= False,
        null=False,
        help_text = "Overwrites the default title",

    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank =False,
        null =True,
        related_name= "+",
        on_delete = models.SET_NULL,
    )

    content = StreamField(
        [
            ("title_and_text_block", blocks.TitleAndTextBlock()),
            ("full_richtext",blocks.RichtextBlock()),
            ("simple_richtext",blocks.SimpleRichtextBlock()),
            ("cards",blocks.CardBlock()),
            ("cta",blocks.CTABlock())
        ],
        null=True,
        blank=True,


    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content")

    ]