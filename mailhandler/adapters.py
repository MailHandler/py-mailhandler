# coding: utf-8
from urlparse import urljoin

import requests


class BaseAdapter:
    base_url = 'https://api.mailhandler.ru/'
    default_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, *args, **kwargs):
        self.session = requests.Session()
        self.headers = self.default_headers.copy()
        self.headers.update(kwargs.get('headers', {}))

    def get_url(self, url):
        return urljoin(self.base_url, url)

    def _post(self, url, data, **kwargs):
        with self.session as s:
            return s.post(url=url, json=data, headers=self.headers, verify=False, **kwargs)

    def _get(self, url, params=None, **kwargs):
        with self.session as s:
            return s.get(url=url, params=params, headers=self.headers, verify=False, **kwargs)
