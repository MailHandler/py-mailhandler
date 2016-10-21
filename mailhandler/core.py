# coding: utf-8
from mailhandler.tracking.adapters import TrackingAdapter
from mailhandler.transactional.adapters import TransactionalAdapter
from mailhandler.bulk.adapters import BulkAdapter


class Client:
    token = None
    adapters = (
        TrackingAdapter,
        TransactionalAdapter,
        BulkAdapter
    )

    def __init__(self, token):
        self.token = token
        self.setup_adapters()

    def setup_adapters(self):
        for adapter_class in self.adapters:
            instance = adapter_class(headers={'X-Secure-Token': self.token})
            setattr(self, instance.name, instance)
