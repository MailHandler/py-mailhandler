# coding: utf-8
from mailhandler.adapters import BaseAdapter
from mailhandler.exceptions import WrongParamException


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
            'text_body': text_body,
            'html_body': html_body,
            'reply_to': reply_to,
            'cc': cc,
            'bcc': bcc,
            'tag': tag,
            'headers': headers,
            'disable_inline': disable_inline,
            'context': context,
        }

        url = self.get_url('/message/send/')
        response = self._post(url=url, data=data)
        return response.json()
