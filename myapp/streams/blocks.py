""" Stream Field"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True,help_text="Add Your Title")
    text = blocks.TextBlock(required=True,help_text="Add Additional text")

    class Meta :
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):

    title  = blocks.CharBlock(required=True,help_text="Add Your Title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title",blocks.CharBlock(required=True,max_length=100)),
                ("text",blocks.CharBlock(required=True,max_length=400)),
                ("button_page",blocks.PageChooserBlock(required=False)),
                ("button_url",blocks.URLBlock(required=False, help_text="if the button page above is selected.that will be use first. ")),
            ]
        )
    )

    class Meta :
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "staff card"

class RichtextBlock(blocks.RichTextBlock):
    """ Richtext with all the features """

    class Meta :
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """ Richtext without(limited) all the features """

    def __init__(self,required=True,help_text=None,editor='default',features=None,**kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]
        
    class Meta :
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple Richtext"


class CTABlock(blocks.StructBlock):
    """ A simple call to action section """

    title = blocks.CharBlock(required=True,max_length=60)
    text = blocks.RichTextBlock(required=True,features =["bold", "italic", "underline"]) 
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text  = blocks.CharBlock(required=True, default="learn More", max_length=40)

    class Meta:
        template = "streams/cta_block.html"
        icon = "Placeholder"
        label = "Call to action"

class ListStructValue(blocks.StructValue):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page :
            return button_page.url
        elif button_url:
            return button_url
        
        return None

    # def latest_posts(self):

    #     return BlogDetailPage.object.live().public()[:3]

class ButtonBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False, help_text= "if selected,this url willbe used first")
    button_url = blocks.URLBlock(required=False, help_text= "if added, this url ill be used secondaril to the button page")
   
    # def get_contex(self, request,*args,**kwargs):

    #     context = super().get_context(request,*args,**kwargs)
    #     context['latest_posts'] = BlogDetailPage.object.live().public()[:3]
    #     return context

    class Meta:
        template = "streams/button_block.html"
        icon = "Placeholder"
        label = "Single Button"
        value_class = ListStructValue