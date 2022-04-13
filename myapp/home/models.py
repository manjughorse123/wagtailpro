from django.shortcuts import render
from django.db import models
from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField,StreamField
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.models import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from streams import blocks

class HomePageCarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image", 
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    Panels = [
        ImageChooserPanel("carousel_image")
    ]

    api_fields = [
        APIField("carousel_image"),
        APIField("a_different_field_name"),
       
    ]


class HomePage(RoutablePageMixin,Page):
    """Home page Model """
    templates = "templates/home/home_page.html"
    max_count=1  
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=["bold","italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"

    )
    content = StreamField([
        ("cta", blocks.CTABlock()),
    ],null=True,blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_subtitle"),
        APIField("banner_image"),
        APIField("banner_cta"),
        APIField("carousel_images"),
        APIField("content"),
        

    ]


    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        InlinePanel("carousel_images")


    ]

    class meta:
        verbose_name = "OH HELLO WORLD"
        verbose_name_plural = "PLURAL NAME"

    @route(r'^subscribe/$')
    def the_subscribe_page(self,request,*args,**kwargs):

        context = self.get_context(request,*args,**kwargs)
        context['a_special_test'] = "Hello World 123122"
        return render(request,"home/subscribe.html",context)