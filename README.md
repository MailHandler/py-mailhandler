# py-mailhandler

Python client library for [MailHandler API](https://mailhandler.ru/docs/).

This library is in active development now. Contributions are very welcome!


Installation
------------
You may install MailHandler python client with `pip`:

`pip install mailhandler`


Example Usage
-------------
Send single transactional email:

```python
from mailhandler.core import Client

client = Client(token='<API_TOKEN>')
result = client.transactional.send_email(
    from_email='alice@example.com',
    to_email=['bob@example.com'],
    subject='MailHandler is awesome',
    html_body='<html><body>Hello! This is your test email.</body></html>'
)
```

Track email events:

```python
from mailhandler.core import Client

client = Client(token='<API_TOKEN>')
events = client.tracking.email_events('<UNIQUE_EMAIL_ID>')
```


MailHandler Documentation
-------------------------
You may view full API documentation here - [MailHandler API docs](https://mailhandler.ru/docs/).


Thanks
------
Thanks to [Stranger6667](https://github.com/Stranger6667) for architecture inspiration!