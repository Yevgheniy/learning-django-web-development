from django.conf.urls import include, url
from django.contrib import admin
from tweets.views import Index, Profile, PostTweet


admin.autodiscover()
urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/post/$', PostTweet.as_view())
]
