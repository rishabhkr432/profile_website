from django.urls import path

import jobs.views
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path("<int:blog_id>/", views.detail, name='detail')

]
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
