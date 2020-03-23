from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',views.homeindex,name='homeindex'),
    path('aboutus/',views.aboutusindex,name="aboutusindex"),
    path('projects',views.projectsindex,name="projectsindex"),
    path('contactus',views.contactusindex,name="contactusindex"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)