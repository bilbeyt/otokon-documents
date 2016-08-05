from django.contrib import admin
from uploader.models import DocumentType, Document, Tag


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "slug", "doc_type", "created", "updated"]
    list_filter = ["author", "doc_type", "created"]
    search_fields = ["author", "title"]
    exclude = ["slug", "author"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class DocumentTypeAdmin(admin.ModelAdmin):
    list_diplay = ["title", "created"]
    list_filter = ["created"]
    search_fields = ["title"]
    exclude = ["slug"]


class TagAdmin(admin.ModelAdmin):
    list_diplay = ["name", "created"]
    exclude = ["slug"]
    search_fields = ["name"]
    list_filter = ["created"]


admin.site.register(Tag, TagAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
