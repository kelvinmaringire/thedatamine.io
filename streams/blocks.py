from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class NavigationItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    href = blocks.CharBlock()
    show = blocks.BooleanBlock(default=True, required=False)

    class Meta:
        template = "home/header.html"
        icon = "placeholder"
        label = "Header Navigation"


class ClientImageBlock(blocks.StructBlock):
    client = ImageChooserBlock()

    class Meta:
        template = "home/main/clients_section.html"
        icon = "image"
        label = "Clients Section"  


class AboutListItem(blocks.StructBlock):
    item = blocks.CharBlock()

    class Meta:
        template = "home/main/about_us.html"  
        label = "About Us List Item"


class WhyUsAccordion(blocks.StructBlock):
    span = blocks.CharBlock()
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock()

    class Meta:
        template = "home/main/why_us.html" 


class SkillsBlock(blocks.StructBlock):
    skill_title = blocks.CharBlock()
    skill_value = blocks.CharBlock()

    class Meta:
        template = "home/main/skills.html" 


class ServicesBlock(blocks.StructBlock):
    icon = blocks.CharBlock(help_text="https://boxicons.com/ example bx bxs-user")
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock()

    class Meta:
        template = "home/main/services.html"  


class FeaturesBlock(blocks.StructBlock):
    icon = blocks.CharBlock(help_text="https://icons.getbootstrap.com/ example bi bi-binoculars")
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()
    ul_list = blocks.ListBlock(blocks.CharBlock(required=False))

    class Meta:
        template = "home/main/features.html"                                          


class PortfolioItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    category = blocks.CharBlock()
    image = ImageChooserBlock()
    details_url = blocks.URLBlock(required=False)

    class Meta:
        template = "home/main/portfolio.html"


class SocialLinkBlock(blocks.StructBlock):
    icon = blocks.CharBlock(help_text="https://remixicon.com/ example ri-twitter-fill")
    href = blocks.URLBlock()


class TeamItemBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    profession = blocks.CharBlock()
    image = ImageChooserBlock()
    subtitle = blocks.RichTextBlock(required=False)
    socials = blocks.ListBlock(SocialLinkBlock, required=False)

    class Meta:
        template = "home/main/team.html"


class PricingFeaturesBlock(blocks.StructBlock):
    feature = blocks.CharBlock()
    na_feature = blocks.CharBlock(required=False, help_text=" class name 'na' for no feature")


class PricingItemBlock(blocks.StructBlock):
    plan = blocks.CharBlock()
    currency = blocks.CharBlock()
    price = blocks.CharBlock()
    duration = blocks.CharBlock()
    button_url = blocks.CharBlock()
    button_name = blocks.CharBlock()
    featured_box = blocks.CharBlock(required=False, help_text=" class name 'featured' for a featured box")
    features = blocks.ListBlock(PricingFeaturesBlock)

    class Meta:
        template = "home/main/pricing.html"


class FAQItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    subtitle = blocks.RichTextBlock()

    class Meta:
        template = "home/main/faqs.html"          