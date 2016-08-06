from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from uploader.forms import DocumentCreateForm, DocumentUpdateForm
from uploader.models import Document, DocumentType, Tag


def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        raise PermissionDenied
    else:
        return login(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class DocumentListView(ListView):
    model = Document
    template_name = "uploader/document_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentListView, self).dispatch(request, *args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        context["document_list"] = Document.objects.all()
        return context


class DocumentDetailView(DetailView):
    model = Document
    template_name = "uploader/document_detail.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context["tag_list"] = obj.tags.all()
        return context


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentCreateForm
    success_url = reverse_lazy("base")
    template_name = "uploader/document_create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        check = self.request.user.groups.filter(name="exclusive").exists()
        check2 = self.request.user.is_superuser
        if not check and not check2:
            raise PermissionDenied
        return super(DocumentCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.instance
        instance.author = self.request.user
        return super(DocumentCreateView, self).form_valid(form)


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentUpdateForm
    success_url = reverse_lazy("base")
    template_name = "uploader/document_update.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.instance
        instance.author = self.request.user
        return super(DocumentUpdateView, self).form_valid(form)


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy("base")
    template_name = "uploader/document_delete.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentDeleteView, self).dispatch(request, *args, **kwargs)
