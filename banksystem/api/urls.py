from django.conf.urls import url 

from .views import (
    BranchApiView,
    BranchDetailAPIView
)

urlpatterns = [
    url(r'^branches/', BranchApiView.as_view(),name='branches'),
    url(r'^branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(),name='branch-detail')
]