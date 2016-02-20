# Create your views here.
#coding=utf-8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import Post
from blog.models import AboutMe
from blog.models import LiuYan
from blog.models import Category
from blog.models import Links 
from blog.models import Comment
from blog.models import Photo
from blog.models import PhotoComment
from blog.models import PhotoAll
from blog.models import XinQing
import sys, string, os

tjposts=Post.objects.filter(istj=1) 
links=Links.objects.all()
cats=Category.objects.all()
posts = Post.objects.all()
newposts=Post.objects.order_by("-pub_data")
mostclickposts=Post.objects.order_by("-click_times")


def index(request):   
    t = loader.get_template("index.html")
    c = Context({'posts':posts,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))
	
def page(request):
    t = loader.get_template("page.html")
    id = request.GET.get('id')
    post=Post.objects.get(id=id)
    comments=post.comment_set.all() 	
    post.click_times+=1
    post.save()
    c = Context({'post':post,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"comments":comments})
    return HttpResponse(t.render(c))
	
def about(request):
    t = loader.get_template("about.html")
    about=AboutMe.objects.get(id=1)
    c = Context({'about':about,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links})
    return HttpResponse(t.render(c))
	
def pages(request):
    t = loader.get_template("pages.html")
    c = Context({'posts':posts,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))	

def tjpages(request):
    t = loader.get_template("tjpages.html")
    c = Context({'posts':posts,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))	

def news(request):	
	t = loader.get_template("news.html")
	c = Context({'posts':posts,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
	return HttpResponse(t.render(c))

def clickm(request):
	t = loader.get_template("clickm.html")
	c = Context({'posts':posts,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
	return HttpResponse(t.render(c))
	
def catpages(request):	
    t = loader.get_template("catpages.html")
    id = request.GET.get('id')
    catposts=Category.objects.get(id=id)
    catpost=catposts.post_set.all()   
    c = Context({'catpost':catpost,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))
	

def addcomment(request):
    postid = request.GET.get('id')
    id=request.POST['id']
    username=request.POST['username']
    email=request.POST['email']
    content=request.POST['content']
    psw=request.POST['psw']	
    t = loader.get_template("addcommentresult.html")
    if (psw=="123456" and username!="" and email!="" and content!=""):
		comment=Comment()
		comment.user=username
		comment.content=content
		comment.email=email
		post=Post.objects.get(id=postid)
		comment.ofpost=post
		comment.save()
		post.comment_times+=1
		post.save()
		result="评论添加成功"
			
    else:
        result="评论添加不成功 请联系站长"	
    c = Context({"username":username,"result":result,"postid":postid,"id":id})
    return HttpResponse(t.render(c))
       

	
	
	
def addphotocomment(request):
    photoid = request.GET.get('id')
    usrname=request.POST['usrname']
    email=request.POST['email']
    content=request.POST['content']
    psw=request.POST['psw']	
    t = loader.get_template("addcommentresult.html")
    if psw=="123456":
        comment=PhotoComment()
        comment.email=email
        comment.user=usrname
        comment.content=content
        comment.ofphoto=Photo.objects.get(id=photoid)
        comment.save()
        result="评论添加成功"
    else:
        result="评论添加不成功 请联系站长"	
    c = Context({"usrname":usrname,"result":result,"id":id})
    return HttpResponse(t.render(c))	

	
def addlink(request):
    t = loader.get_template("addlink.html")
    c = Context({'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))

	
def addlinktj(request):
    username=request.POST['username']
    name=request.POST['name']
    link=request.POST['link']
    psw=request.POST['psw']	
    t = loader.get_template("addlinkresult.html")
    if (psw=="123456" and username!="" and name!="" and link!=""):
        linkall=Links()
        linkall.name=name
        linkall.url=link
        linkall.save()
        result="连接添加成功"
    else:
        result="链接添加不成功 请联系站长"	
    c = Context({"username":username,"result":result})
    return HttpResponse(t.render(c))
	
def liuyan(request):
    liuyans = LiuYan.objects.all()
    t = loader.get_template("liuyan.html")
    c = Context({'liuyans':liuyans,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))	
	
def liuyantj(request):
    name=request.POST['username']
    title=request.POST['title']
    content=request.POST['content']
    email=request.POST['email']
    result="添加留言成功"
    if (name!="" and title!="" and content!="" and email!=""):
            liuyanall=LiuYan()
            liuyanall.name=name
            liuyanall.email=email
            liuyanall.liuyantitle=title
            liuyanall.liuyan=content
            liuyanall.save()           		
    else:    
	    result="添加留言不成功"
    t = loader.get_template("sucess.html")
    c = Context({"result":result})
    return HttpResponse(t.render(c))
	
	
def photoall(request):
    photoalls=PhotoAll.objects.all()
    t = loader.get_template("photoall.html")
    c = Context({"photoalls":photoalls,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))
	
def photos(request):
    id = request.GET.get('id')
    photoall=PhotoAll.objects.get(id=id)
    photos=photoall.photo_set.all()
    t = loader.get_template("photos.html")
    c = Context({"photos":photos,'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,"tjposts":tjposts})
    return HttpResponse(t.render(c))
	
	
def xinqing(request):
    xinqings=XinQing.objects.all()
    t = loader.get_template("xinqing.html")
    c =  Context({'newposts':newposts,'mostclickposts':mostclickposts,"cats":cats,"links":links,'xinqings':xinqings,"tjposts":tjposts})
    return HttpResponse(t.render(c))		

