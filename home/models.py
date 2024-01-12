from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from modelcluster.fields import ParentalKey

from streams import blocks


class ContactPage(AbstractEmailForm):
    template = "home/main/contact_form.html"
    subtitle = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('subtitle'),
        InlinePanel('form_fields', label="Form fields"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='form_fields')


class HomePage(Page):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    navigation = StreamField([
        ('navigation', blocks.NavigationItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    hero_title = models.CharField(max_length=100, blank=False, null=True)
    hero_subtitle = RichTextField(null=True, blank=False)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_button_page_title = models.CharField(max_length=100, blank=False, null=True)
    hero_button_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_button_url_title = models.CharField(max_length=100, blank=False, null=True)
    hero_button_url = models.URLField(null=True, blank=False)

    clients = StreamField([
        ('client', blocks.ClientImageBlock()),
    ], use_json_field=True, blank=True, null=True, collapsed=True,)

    about_title = models.CharField(max_length=100, blank=False, null=True)
    about_subtitle1 = RichTextField(null=True, blank=False)
    about_subtitle2 = RichTextField(null=True, blank=False)
    about_href_title = models.CharField(max_length=100, blank=True, null=True)
    about_href = models.CharField(max_length=100, blank=True, null=True)
    about_list_items = StreamField([
        ('about_list_item', blocks.AboutListItem()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    why_us_title = models.CharField(max_length=100, blank=False, null=True)
    why_us_subtitle = RichTextField(null=True, blank=False)
    why_us_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    why_us_accordion = StreamField([
        ('why_us_accordion', blocks.WhyUsAccordion()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    skills_title = models.CharField(max_length=100, blank=False, null=True)
    skills_subtitle = RichTextField(null=True, blank=False)
    skills_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    skills = StreamField([
        ('skill', blocks.SkillsBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    services_title = models.CharField(max_length=100, blank=False, null=True)
    services_subtitle = RichTextField(null=True, blank=False)
    services = StreamField([
        ('service', blocks.ServicesBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    features_title = models.CharField(max_length=100, blank=False, null=True)
    features_subtitle = RichTextField(null=True, blank=False)
    features = StreamField([
        ('feature', blocks.FeaturesBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    portfolio_title = models.CharField(max_length=100, blank=False, null=True)
    portfolio_subtitle = RichTextField(null=True, blank=False)
    portfolio = StreamField([
        ('portfolio', blocks.PortfolioItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)

    team_title = models.CharField(max_length=100, blank=False, null=True)
    team_subtitle = RichTextField(null=True, blank=False)
    team = StreamField([
        ('team', blocks.TeamItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)  

    pricing_title = models.CharField(max_length=100, blank=False, null=True)
    pricing_subtitle = RichTextField(null=True, blank=False)
    pricing = StreamField([
        ('pricing', blocks.PricingItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)    

    faq_title = models.CharField(max_length=100, blank=False, null=True)
    faq_subtitle = RichTextField(null=True, blank=False)
    faq = StreamField([
        ('faq', blocks.FAQItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)    

    contact_title = models.CharField(max_length=100, blank=False, null=True)
    contact_subtitle = RichTextField(null=True, blank=False)
    contact_address = models.CharField(max_length=100, blank=False, null=True)
    contact_email = models.CharField(max_length=100, blank=False, null=True)
    contact_number = models.CharField(max_length=100, blank=False, null=True)
    contact_map = models.URLField(null=True, blank=True)
    
    faq = StreamField([
        ('faq', blocks.FAQItemBlock()),
    ], use_json_field=True, blank=False, null=True, collapsed=True,)     


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("logo"),
            FieldPanel("navigation"),
        ], heading="Header Options",  classname="collapsed", icon="h1"),
        MultiFieldPanel([
            FieldPanel("hero_title"),
            FieldPanel("hero_subtitle"),
            FieldPanel("hero_image"),
            FieldPanel("hero_button_page_title"),
            PageChooserPanel("hero_button_page"),
            FieldPanel("hero_button_url_title"),
            FieldPanel("hero_button_url"),
        ], heading="Hero Options",  classname="collapsed", icon="desktop"),
        FieldPanel("clients", classname="collapsed"),
        MultiFieldPanel([
            FieldPanel("about_title"),
            FieldPanel("about_subtitle1"),
            FieldPanel("about_subtitle2"),
            FieldPanel("about_href_title"),
            FieldPanel("about_href"),
            FieldPanel("about_list_items"),
        ], heading="About Us",  classname="collapsed", icon="user"), 
        MultiFieldPanel([
            FieldPanel("why_us_title"),
            FieldPanel("why_us_subtitle"),
            FieldPanel("why_us_image"),
            FieldPanel("why_us_accordion"),
        ], heading="Why Us",  classname="collapsed", icon="openquote"),            
        MultiFieldPanel([
            FieldPanel("skills_title"),
            FieldPanel("skills_subtitle"),
            FieldPanel("skills_image"),
            FieldPanel("skills"),
        ], heading="Skills",  classname="collapsed", icon="order-up"), 
        MultiFieldPanel([
            FieldPanel("services_title"),
            FieldPanel("services_subtitle"),
            FieldPanel("services"),
        ], heading="Services",  classname="collapsed", icon="cogs"),
        MultiFieldPanel([
            FieldPanel("features_title"),
            FieldPanel("features_subtitle"),
            FieldPanel("features"),
        ], heading="Features",  classname="collapsed", icon="regex"), 
        MultiFieldPanel([
            FieldPanel("portfolio_title"),
            FieldPanel("portfolio_subtitle"),
            FieldPanel("portfolio"),
        ], heading="Portfolio",  classname="collapsed", icon="image"), 
        MultiFieldPanel([
            FieldPanel("team_title"),
            FieldPanel("team_subtitle"),
            FieldPanel("team"),
        ], heading="Team",  classname="collapsed", icon="group"),   
        MultiFieldPanel([
            FieldPanel("pricing_title"),
            FieldPanel("pricing_subtitle"),
            FieldPanel("pricing"),
        ], heading="Pricing",  classname="collapsed", icon="table"),
        MultiFieldPanel([
            FieldPanel("faq_title"),
            FieldPanel("faq_subtitle"),
            FieldPanel("faq"),
        ], heading="Frequently Asked  Questions",  classname="collapsed", icon="help"), 
        MultiFieldPanel([
            FieldPanel("contact_title"),
            FieldPanel("contact_subtitle"),
            FieldPanel("contact_address"),
            FieldPanel("contact_email"),
            FieldPanel("contact_number"),
            FieldPanel("contact_map"),
        ], heading="Contact",  classname="collapsed", icon="mail"),                                       
             
    ]
