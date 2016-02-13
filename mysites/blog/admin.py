#coding=utf-8

from django.contrib import admin
from blog.models import Category,Post,PostAdmin ,LiuYan ,Links,XinQing ,Photo ,PhotoAll,Comment,AboutMe,PhotoComment

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(LiuYan)
admin.site.register(Links)
admin.site.register(XinQing)
admin.site.register(Photo)
admin.site.register(PhotoAll)
admin.site.register(AboutMe)
admin.site.register(PhotoComment)