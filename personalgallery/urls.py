from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.post_of_today,name='postOfToday'),
    url('^today/$',views.post_time,name='postToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_day_post,name = 'pastPost')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)