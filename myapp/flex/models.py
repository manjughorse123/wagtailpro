from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks


# Create your models here.
class FlexPage(Page):

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text_block", blocks.TitleAndTextBlock()),
            ("full_richtext",blocks.RichtextBlock()),
            ("simple_richtext",blocks.SimpleRichtextBlock()),
            ("cards",blocks.CardBlock()),
            ("cta",blocks.CTABlock()),
            ("button",blocks.ButtonBlock())
        ],
        null=True,
        blank=True,


    )

    subtitle = models.CharField(max_length=255, blank=True,null=True)

    content_panels = Page.content_panels +[
        FieldPanel("subtitle"),
        StreamFieldPanel("content")

    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural ="Flex Pages"