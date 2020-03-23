from django.contrib import admin
from page.models import *


class NavbarTabular(admin.TabularInline):
    model=Navbarhome
class HomeCardTabular(admin.TabularInline):
    model=HomeCard
class ImageBackgroundTabular(admin.TabularInline):
    model=BackgroundImage

class AboutusparagrapTabular(admin.TabularInline):
    model=Aboutusparagrap

class AboutusimageTabular(admin.TabularInline):
    model=Aboutusimage

class GalleryprojectsTabular(admin.TabularInline):
    model=Galleryprojects

class InfoContactusTabular(admin.TabularInline):
    model=InfoContactus

class MapContactusTabular(admin.TabularInline):
    model=MapContactus

class ServicesNavbarTabular(admin.TabularInline):
    model=ServicesNavbar

@admin.register(Home)
class Homeadmin(admin.ModelAdmin):
    inlines=(NavbarTabular,HomeCardTabular,ImageBackgroundTabular)

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    inlines=(AboutusparagrapTabular,AboutusimageTabular)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines=[GalleryprojectsTabular]

@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    inlines=(InfoContactusTabular,MapContactusTabular)
# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    inlines=[ServicesNavbarTabular]

admin.site.register(Footer)