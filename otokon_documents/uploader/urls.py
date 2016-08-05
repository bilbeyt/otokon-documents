from django.conf.urls import url
from uploader.views import custom_login, custom_logout, DocumentListView, \
    DocumentDetailView, DocumentDeleteView, DocumentUpdateView, \
    DocumentCreateView

urlpatterns = [
    url(r'^$', DocumentListView.as_view(), name="base"),
    url(r'^login/$', custom_login, name="login"),
    url(r'^logout/$', custom_logout, name="logout"),
    url(r'^create/$', DocumentCreateView.as_view(), name="document_create"),
    url(r'^(?P<slug>[\w-]+)/$',
        DocumentDetailView.as_view(),
        name="document_detail"),
    url(r'^(?P<slug>[\w-]+)/update/$',
        DocumentUpdateView.as_view(),
        name="document_update"
    ),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        DocumentDeleteView.as_view(),
        name="document_delete"
        ),

]
