from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from nizapp.niz.views import *
#from nizapp.niz.feeds import *

from nizapp.niz.mviews import *

import os.path




#site_media = os.path.join(os.path.dirname(__file__), '/var/www/django/nizapp/niz/site_media')
site_media = '/home/evens/mobile/nizapp/niz/site_media'
#media = '/opt/python2.6/lib/python2.6/site-packages/django/contrib/admin/media' 
media = '/opt/python2.6/lib/python2.6/site-packages/django/contrib/admin/static'


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


upload_thumbnails = os.path.join(os.path.dirname(__file__),'niz/upload/thumbnails')
upload_image = os.path.join(os.path.dirname(__file__), 'niz/upload')

#feeds = {'recent':RecentTours,
#         'user':UserTours} 

urlpatterns = patterns('',
    # Example:
    # (r'^nizapp/', include('nizapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
#    (r'^$', main_page),
#    (r'^user/(\w+)/$', user_page),
#    (r'^login/$', 'django.contrib.auth.views.login'),
#    (r'^account/login/$', 'django.contrib.auth.views.login'),
#    (r'^logout/$', logout_page),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': site_media }),
   
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': media }),
 
#    (r'^register/$', register_page),
#    (r'^register/success$', direct_to_template, { 'template':'registration/register_success.html'}),
    
#    (r'^save/$', tour_save_page),
#    (r'^tag/([^\s]+)/$', tag_page),
#    (r'^tag/$', tag_cloud_page),
#    (r'^search/$', search_page),
#    (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
#    (r'^vote/$', tour_vote_page),
#    (r'^popular/$', popular_page),
    
#    (r'^var/www/django/nizapp/niz/upload/thumbnails/(?P<path>.*)$', 'django.views.static.serve',
#     { 'document_root': upload_thumbnails }),
                       
      
#    (r'^var/www/django/nizapp/niz/upload/(?P<path>.*)$', 'django.views.static.serve',
#     { 'document_root': upload_thumbnails }),
                       
#    (r'^m/list/var/www/django/nizapp/niz/upload/(?P<path>.*)$', 'django.views.static.serve',
#     { 'document_root': upload_thumbnails }),

#    (r'^tour/(\d+)/$', tour_page),

    #(r'^admin/(.*)', admin.site.root),
    (r'^admin/', include(admin.site.urls)),

#    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict':feeds}),
    

#mobile web page
#mobile detail webpage
#mobile read xml page
)



urlpatterns += patterns('',
#			url(r'^login/$', mobile_login_page),
                        url(r'^list/$', mobile_main_page),
                        url(r'^detail/(\d+)/$', mobile_detail_page),
                        url(r'^xml/', mobile_xml_page),
                        url(r'^search/$', mobile_search_page), 
                        url(r'^recommand/', mobile_recommand_page),
                        url(r'^register_subscription/$', mobile_register_subscription),

			url(r'^home/evens/www/mobile/nizapp/niz/upload/thumnails/(?P<path>.*)$', 'django.views.static.serve',
			     { 'document_root': upload_thumbnails }),
			url(r'^home/evens/www/mobile/nizapp/niz/upload/(?P<path>.*)$', 'django.views.static.serve',
			     { 'document_root': upload_image }),
                        )



urlpatterns += patterns('',
                        url(r'^comments/', include('django.contrib.comments.urls')),
                        )
