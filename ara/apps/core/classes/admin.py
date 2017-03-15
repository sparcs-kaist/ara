from django.contrib import admin


class MetaInfoModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
        'deleted_at',
    )
