from typing import Any
from django.db.models import Manager


class AbstractServerManager(Manager):
    def get_active(self):
        return self.get_queryset().filter(is_active=True)

    def get_inactive(self):
        return self.get_queryset().filter(is_active=False)

    def inactive_other_servers(self):
        self.get_queryset().filter(is_active=True).update(is_active=False)
