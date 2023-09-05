
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Information(models.Model):#
   # LOGO = models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   # FaviconIco= models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   SlideImage = models.FileField(upload_to = "files/images/Home/Slide/Image/%Y/%m/%d/",blank=True, null=True)
   Address= models.CharField(max_length=300, blank=True, null=True)
   Map_Address= models.CharField(max_length=500,blank=True, null=True)
   WebName= models.CharField(max_length = 300 ,blank=True, null=True)
   Description = models.CharField(max_length = 300 , null = True)
   Gmail= models.CharField(max_length = 300 ,blank=True, null=True)
   PHONE = models.CharField(max_length = 300 ,blank=True, null=True)
   Twitterlinke= models.CharField(max_length=500,blank=True, null=True)
   instagramlinke= models.CharField(max_length=500,blank=True, null=True)
   facebooklinke= models.CharField(max_length=500,blank=True, null=True)
   Youtubelinke= models.CharField(max_length=500,blank=True, null=True)
   linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
   Whatsapp= models.CharField(max_length=500,blank=True, null=True)
   snapchat= models.CharField(max_length=500,blank=True, null=True)
   Address= models.CharField(max_length=500,blank=True, null=True)
   OpeningHours= models.CharField(max_length=500,blank=True, null=True)
   pixal_id= models.CharField(max_length=500,blank=True, null=True)
   Copyright = models.CharField(max_length = 300 ,blank=True, null=True)

   def __str__(self):
         return self.WebName



class About(models.Model):
     Image = models.FileField(upload_to = "files/images/About/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Titel= models.CharField(max_length = 300 , null = True)
     Description = models.CharField(max_length = 300 , null = True)
     Ourmessage= models.CharField(max_length = 300 , null = True)
     Ourvision= models.CharField(max_length = 300 , null = True)
     Image2 = models.FileField(upload_to = "files/images/About/photos/Image/%Y/%m/%d/",blank=True, null=True)

     def __str__(self):
        return self.Titel




class ChooseUs(models.Model):
     Experience = models.CharField(max_length = 300 , null = True)
     CustomSolutions= models.CharField(max_length = 300 , null = True)
     StrongNetwork= models.CharField(max_length = 300 , null = True)
     Customers= models.IntegerField(default=0, blank=True, null=True)
     Projects= models.IntegerField(default=0, blank=True, null=True)
     Hours_of_support= models.IntegerField(default=0, blank=True, null=True)
     hard_at_work= models.IntegerField(default=0, blank=True, null=True)
     def __str__(self):
        return self.Experience





class Service(models.Model):
      Title= models.CharField(max_length = 300 , null = True)
      Description= models.CharField(max_length = 300 , null = True)
      def __str__(self):
        return self.Title


class businessplan(models.Model):
      Description= models.CharField(max_length = 300 , null = True)
      def __str__(self):
        return self.Description

class Reviews(models.Model):
     Image = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     jobtitel= models.CharField(max_length = 300 , null = True)
     Description = models.CharField(max_length = 300 , null = True)
     def __str__(self):
        return self.Name

class Ourcustomers(models.Model):
     Title= models.CharField(max_length = 300 , null = True)
     Image = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     def __str__(self):
        return self.Title


class team(models.Model):
     Image = models.FileField(upload_to = "files/images/team/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     jobtitel= models.CharField(max_length = 300 , null = True)
     def __str__(self):
        return self.Name

class Blog(models.Model):
   active = models.BooleanField(default = False)
   Image = models.FileField(upload_to = "files/images/Blog/Image/%Y/%m/%d/",blank=True, null=True)
   Titel= models.CharField(max_length = 300 , null = True)
   Description = models.CharField(max_length = 300 , null = True)
   slideImage =models.FileField(upload_to = "files/images/Blog/slideImage/%Y/%m/%d/",blank=True, null=True)
   body= RichTextField()

   def __str__(self):
        return self.Titel
