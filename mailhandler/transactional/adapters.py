# coding: utf-8
from mailhandler.adapters import BaseAdapter


class TransactionalAdapter(BaseAdapter):
    """
    Transactional mailing adapter.
    """
    name = 'transactional'

    def send_email(self, from_email, to_email, subject, text_body=None, html_body=None, reply_to=None, cc=None,
                   bcc=None, tag=None, headers=None, disable_inline=False, context=None):

        data = {
            'from': from_email,
            'to': to_email,
            'subject': subject,
        }

        if text_body:
            data['text_body'] = text_body

        if html_body:
            data['html_body'] = html_body

        if reply_to:
            data['reply_to'] = reply_to

        if cc:
            data['cc'] = cc

        if bcc:
            data['bcc'] = bcc

        if tag:
            data['tag'] = tag

        if headers:
            data['headers'] = headers

        if disable_inline:
            data['disable_inline'] = disable_inline

        if context:
            data['context'] = context

        url = self.get_url('/message/send/')
        response = self._post(url=url, data=data)
        return response.json()
