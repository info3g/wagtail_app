from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from home.forms import HomeForm


class HomePage(Page):
    text_json = RichTextField(blank=True)
    # body = RichTextField()
    # date = models.DateField("Post date")

    # # Search index configuration
    # search_fields = Page.search_fields + [
    #     index.SearchField('body'),
    #     index.FilterField('date'),
    # ]

    content_panels = Page.content_panels + [
        FieldPanel('text_json', classname="full"),
    ]

    def serve(self, request):
        if request.method == 'POST':
            form = HomeForm(request.POST)
            if form.is_valid():
                # home = form.save()
                objH = self
                objH.text_json = request.POST.get("text_json")
                objH.save()
                return render(request, 'home/thankyou.html', {
                    'page': self,
                    # 'home': objH,
                })
        else:
            form = HomeForm()

        return render(request, 'home/home_page.html', {
            'page': self,
            'form': form,
        })
