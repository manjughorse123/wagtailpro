
from django.shortcuts import render
from django.db import models

from django import forms

from wagtail.core.models import Page ,Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePageMixin,route
from streams import blocks
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

class BlockAuthorsOrderable(Orderable):

    page = ParentalKey("blog.BlogDetailPage" , related_name="blog_authors")
    author = models.ForeignKey(
        'blog.BlogAuthor',
        on_delete = models.CASCADE,

    )

    panels = [
        SnippetChooserPanel("author")
    ]


class BlogAuthor(models.Model):

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True,null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete = models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                ImageChooserPanel("image"),

            ],
            heading= "Name and Image"
        ),
        MultiFieldPanel(
            [
                FieldPanel('website'),
            ],heading="Links"
        )

    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)

class BlogCategory(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text = 'A slug to identify posts by this category'
    )
    panels = [
        FieldPanel("name"),
        FieldPanel("slug")
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = " Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

register_snippet(BlogCategory)

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
        context["authors"]= BlogAuthor.objects.all()
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

    categories = ParentalManyToManyField("blog.BlogCategory",blank= True)

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
        MultiFieldPanel(
            [
                InlinePanel("blog_authors",label="author",min_num=1,max_num= 4)
            ],
            heading="Author(s)"
        ),
        MultiFieldPanel(
            [
                FieldPanel("categories",widget=forms.CheckboxSelectMultiple )
            ],
            heading="Categories"
        ),
        StreamFieldPanel("content")

    ]