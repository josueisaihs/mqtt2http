from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from ..config.validators import validation_pattern


class AbstractModel(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    description = models.TextField(
        _("Description"), max_length=2500, blank=True, null=True
    )
    slug = AutoSlugField(
        populate_from="name",
        unique=True,
        always_update=True,
        editable=False,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class AbstractServerModel(AbstractModel):
    host = models.URLField(_("Host"), max_length=1000)
    port = models.PositiveIntegerField(
        _("Port"),
        default=80,
        blank=True,
        null=True,
    )
    username = models.CharField(_("Username"), max_length=100, blank=True, null=True)
    password = models.CharField(_("Password"), max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class MQTTBroker(AbstractServerModel):
    class Meta:
        verbose_name = _("MQTT Broker")
        verbose_name_plural = _("MQTT Brokers")

    def __str__(self):
        return self.name


class HTTPClient(AbstractServerModel):
    method = models.CharField(
        _("Method"),
        max_length=4,
        default="POST",
        editable=False,
        blank=True,
        null=False,
    )

    class Meta:
        verbose_name = _("HTTP Client")
        verbose_name_plural = _("HTTP Clients")

    def __str__(self):
        return self.name


class TopicPattern(AbstractModel):
    pattern = models.CharField(
        _("Topic Pattern"), max_length=1000, validators=[validation_pattern]
    )

    class Meta:
        verbose_name = _("Topic Pattern")
        verbose_name_plural = _("Topic Patterns")
        unique_together = ("slug", "name", "pattern")

    def __str__(self):
        return f"{self.name} - {self.pattern}"


class Endpoint(AbstractModel):
    endpoint = models.CharField(_("Endpoint"), max_length=1000)

    class Meta:
        verbose_name = _("Endpoint")
        verbose_name_plural = _("Endpoints")

    def __str__(self):
        return self.endpoint


class Mapping(AbstractModel):
    topic_pattern = models.ForeignKey(
        TopicPattern, verbose_name=_("Topic Pattern"), on_delete=models.CASCADE
    )
    endpoint = models.ForeignKey(
        Endpoint, verbose_name=_("Endpoint"), on_delete=models.CASCADE
    )
    mqtt_broker = models.ForeignKey(
        MQTTBroker, verbose_name=_("MQTT Broker"), on_delete=models.CASCADE
    )
    http_client = models.ForeignKey(
        HTTPClient, verbose_name=_("HTTP Client"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Mapping")
        verbose_name_plural = _("Mappings")
        unique_together = ("topic_pattern", "mqtt_broker", "http_client")

    def __str__(self):
        return f"{self.topic_pattern.name} - {self.mqtt_broker.name} - {self.http_client.name}"

    @property
    def endpoint_url(self):
        if self.http_client.port in [80, 443, None]:
            return f"{self.http_client.host}/{self.endpoint}"
        return f"{self.http_client.host}:{self.http_client.port}/{self.endpoint}"
