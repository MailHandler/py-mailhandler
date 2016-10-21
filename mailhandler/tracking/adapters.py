# coding: utf-8
from mailhandler.adapters import BaseAdapter


class TrackingAdapter(BaseAdapter):
    """
    Tracking features adapter.
    """
    name = 'tracking'

    def email_events(self, unique_id):
        url = self.get_url('/message/events/%s/' % unique_id)
        response = self._get(url)
        return response.json()
