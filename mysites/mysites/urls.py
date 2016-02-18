
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#tracer_sever.apps.user.views
urlpatterns = patterns('',
    # Examples:
	
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'sites.views.home', name='home'),
    # url(r'^sites/', include('sites.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^/$','blog.views.index'),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^blog/page/$', 'blog.views.page'),
    url(r'^blog/pages/$', 'blog.views.pages'),
    url(r'^blog/catpages/$', 'blog.views.catpages'),
    url(r'^blog/about/$','blog.views.about'),
    url(r'^blog/tjpages/$','blog.views.tjpages'),
    url(r'^blog/xinqing/$', 'blog.views.xinqing'),
    url(r'^blog/photoall/$','blog.views.photoall'),
    url(r'^blog/photos/$','blog.views.photos'),
    url(r'^blog/liuyan/$', 'blog.views.liuyan'),
    url(r'^blog/liuyantj/$','blog.views.liuyantj'),
    url(r'^blog/addlink/$', 'blog.views.addlink'),
    url(r'^blog/addlinktj/$', 'blog.views.addlinktj'),
    url(r'^blog/addcomment/$', 'blog.views.addcomment'),
    url(r'^blog/addphotocomment/$', 'blog.views.addphotocomment'),
    url(r'^blog/clickm/$','blog.views.clickm'),
    url(r'^blog/news/$','blog.views.news'),
    
    
    
    url(r'^blog/', include('blog.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
