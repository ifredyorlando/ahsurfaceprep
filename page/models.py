from django.db import models

class Home(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.TextField()
    class Meta:
        verbose_name_plural = "A-Home"
class HomeCard(models.Model):
    home=models.ForeignKey(Home,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/') 


class Navbarhome(models.Model):
    home=models.ForeignKey(Home,on_delete=models.CASCADE)
    navbaritem=models.CharField(max_length=50)

class BackgroundImage(models.Model):
    home=models.ForeignKey(Home,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/') 

class Footer(models.Model):
    title=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='images/') 
    number=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    direction=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "F-Footer"
    

class Aboutus(models.Model):
    title=models.CharField(max_length=50,)
    subtitle=models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "B-About Us"


class Aboutusparagrap(models.Model):
    paragrap=models.TextField(max_length=255)
    aboutus=models.ForeignKey(Aboutus,on_delete=models.CASCADE)

class Aboutusimage(models.Model):
    aboutus=models.ForeignKey(Aboutus,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/') 

class Projects(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    gallerytitle=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "E-Projects"

class Galleryprojects(models.Model):
    projects=models.ForeignKey(Projects,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/') 

class Contactus(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "D-Contact Us"

class InfoContactus(models.Model):
    contactus=models.ForeignKey(Contactus,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)

class MapContactus(models.Model):
    contactus=models.ForeignKey(Contactus,on_delete=models.CASCADE)
    ubication=models.CharField(max_length=255)


class Services(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    subtitle_paragrap=models.CharField(max_length=50)
    paragrap=models.TextField()
    class Meta:
        verbose_name_plural = "C-Services" 
    

class ServicesNavbar(models.Model):
    services=models.ForeignKey(Services,on_delete=models.CASCADE)
    navbaritem=models.CharField(max_length=50)

