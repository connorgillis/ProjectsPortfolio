from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    sec1 = RichTextField(blank=True)
    sec2 = RichTextField(blank=True)
    sec3 = RichTextField(blank=True)
    featured = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('sec1', classname="full"),
        FieldPanel('sec2', classname="full"),
        FieldPanel('sec3', classname="full"),
        FieldPanel('featured', classname="full"),
    ]
