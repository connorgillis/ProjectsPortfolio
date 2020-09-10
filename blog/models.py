from django.db import models
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.documents.models import Document

from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.search import index
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.documents.blocks import DocumentChooserBlock


from wagtail.admin.edit_handlers import FieldRowPanel

from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField



class ContactPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class ResumePage(Page):
    intro = RichTextField(blank=True)
    hobbies = RichTextField(blank=True)
    ri = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('hobbies', classname="full"),
        FieldPanel('ri', classname="full"),

    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        resumeitemsskills = self.get_children().live().order_by('-first_published_at')
        context['resumeitemsskills'] = resumeitemsskills
        return context


@register_snippet
class ResumeCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'resume categories'


class ResumePageItem(Page):
    headA = models.CharField(max_length=250)
    headB = models.CharField(max_length=250)
    loc = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    desc = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.ResumeCategory', blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('headA', classname="full"),
        FieldPanel('headB', classname="full"),
        FieldPanel('loc', classname="full"),
        FieldPanel('time', classname="full"),
        FieldPanel('desc', classname="full")
    ]



class ResumePageSkillIcon(TaggedItemBase):
    content_object = ParentalKey(
        'Resume',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class Resume(Page):
    head = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    icons = ClusterTaggableManager(through=ResumePageSkillIcon, blank=True)
    categories = ParentalManyToManyField('blog.ResumeCategory', blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('head', classname="full"),
        FieldPanel('desc', classname="full"),
        FieldPanel('icons', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    class Meta:
        verbose_name = "this"

class ResumeOther(Page):
    text = models.CharField(max_length=250)
    categories = ParentalManyToManyField('blog.ResumeCategory', blank=True)
    desc = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('desc', classname="full"),


    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        resumeother = self.get_children().live().order_by('-first_published_at')
        context['resumeother'] = resumeother
        return context

class ResumeDocument(Page):
    doc = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    categories = ParentalManyToManyField('blog.ResumeCategory', blank=True)


    content_panels = Page.content_panels + [
        DocumentChooserPanel('doc'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


class BlogIndexPage(Page):
    intro = models.CharField(max_length=250)


    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),

    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
