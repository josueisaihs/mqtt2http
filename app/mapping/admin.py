from django.contrib import admin

from .models import (
    HTTPClient, 
    MQTTBroker, 
    TopicPattern, 
    Mapping,
    Endpoint
)

@admin.register(HTTPClient)
class HTTPClientAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "host", "port", "username", "password", "description")
    search_fields = ("name", "host", "port", "username", "password", "description")
    ordering = ("name", "host", "port", "username", "password", "description")
    fieldsets = (
        (None, {
            "fields": ("name", ("host", "port", "method"))
        }),
        ("Authentication", {
            "fields": [("username", "password")]
        }),
        ("Description", {
            "fields": ("description",)
        })
    )
    readonly_fields = ("method",)


@admin.register(MQTTBroker)
class MQTTBrokerAdmin(admin.ModelAdmin):
    list_display = ("name", "host", "port", "username", "password", "description")
    search_fields = ("name", "host", "port", "username", "password", "description")
    ordering = ("name", "host", "port", "username", "password", "description")
    fieldsets = (
        (None, {
            "fields": ["name", ("host", "port")]
        }),
        ("Authentication", {
            "fields": [("username", "password")]
        }),
        ("Description", {
            "fields": ("description",)
        })
    )


@admin.register(TopicPattern)
class TopicPatternAdmin(admin.ModelAdmin):
    list_display = ("name", "pattern", "description")
    search_fields = ("name", "pattern")
    ordering = ("name", "pattern")
    fieldsets = (
        (None, {
            "fields": ("name", "pattern")
        }),
        ("Description", {
            "fields": ("description",)
        })
    )


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ("name", "endpoint")
    search_fields = ("name", "endpoint")
    ordering = ("name", "endpoint")
    fieldsets = (
        (None, {
            "fields": ("name", "endpoint")
        }),
    )


@admin.register(Mapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = ("topic_pattern", "mqtt_broker", "http_client", "endpoint")
    search_fields = ("topic_pattern", "mqtt_broker", "http_client", "endpoint")
    ordering = ("topic_pattern", "mqtt_broker", "http_client", "endpoint")
    fieldsets = (
        (None, {
            "fields": ("name",)
        }),
        ("Mapping", {
            "fields": ("topic_pattern", "endpoint",)
        }),
        ("Configuration", {
            "fields": ("mqtt_broker", "http_client",)
        }),
    )
    readonly_fields = ("endpoint_url",)
