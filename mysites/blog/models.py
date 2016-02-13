#coding=utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.
class Category(models.Model):
    name = models.CharField(u'文章分类', max_length=64)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name


class Post(models.Model):
    
    title = models.CharField(u"标题", max_length=128)
    istj=models.IntegerField()
    author = models.ForeignKey(User)
    summary = models.TextField(blank=True, null=True)
    po_type = models.ForeignKey(Category, verbose_name=u'文章类型', blank=True, null=True)
    content=UEditorField(u'文章内容',width=600, height=300, toolbars="full", imagePath="/media/images/", filePath="/media/images/", upload_settings={"imageMaxSize":1204000},
                 settings={},command=None,blank=True)
    pub_data = models.DateTimeField(auto_now_add=True)
    click_times=models.IntegerField()
    comment_times=models.IntegerField()
    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        return self.title


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_data')


class LiuYan(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    liuyantitle=models.CharField(max_length=50)
    liuyan=models.TextField(u"留言")
    liuyan_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.liuyantitle
    
class Links(models.Model):
    name=models.CharField(u"链接",max_length=30)
    url=models.URLField(max_length=128)
    def __unicode__(self):
        return self.name
        
        
class Comment(models.Model):
    user = models.CharField(u"评论人",max_length=30)
    content = models.TextField(u"评论")
    email=models.EmailField()
    commentdate = models.DateTimeField(auto_now_add=True)
    ofpost = models.ForeignKey(Post)

class PhotoAll(models.Model):
    name=models.CharField(u"相册",max_length=30)
    def __unicode__(self):
        return self.name

   
class Photo(models.Model):
    name=models.CharField(max_length=30)
    src=models.URLField(max_length=128)
    ofphotoall = models.ForeignKey(PhotoAll)
    image=models.ImageField(u"相片",upload_to="images")
    comment_times=models.IntegerField()
    def __unicode__(self):
        return self.name
    
class PhotoComment(models.Model):
    user = models.CharField(u"评论人",max_length=30)
    content = models.TextField(u"评论")
    email=models.EmailField()
    commentdate = models.DateTimeField(auto_now_add=True)
    ofphoto = models.ForeignKey(Photo)
    
    
class XinQing(models.Model):
    xinqing = models.CharField(u"心情",max_length=128)
    date = models.DateTimeField(auto_now_add=True)


class AboutMe(models.Model):
    qq=models.CharField(max_length=20)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    facesrc=models.URLField(max_length=128)
    abouttitle=models.CharField(u"关于", max_length=128)
    aboutme=models.TextField(u"关于我")
    def __unicode__(self):
        return self.abouttitle        