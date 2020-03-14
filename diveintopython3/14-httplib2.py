>>> from urllib.parse import urlencode
>>> import httplib2
>>> httplib2.debuglevel = 1
>>> h = httplib2.Http('.cache')
>>> data = {'status': 'Test update from Python 3'}
>>> h.add_credentials('diveintomark', 'MY_SECRET_PASSWORD', 'identi.ca') 
>>> resp, content = h.request('https://identi.ca/api/statuses/update.xml',
...  'POST', 
...  urlencode(data), 
...  headers={'Content-Type': 'application/x-www-form-urlencoded'}) 
>>> print(content.decode('utf-8'))


>>> from xml.etree import ElementTree as etree
>>> tree = etree.fromstring(content) ①
>>> status_id = tree.findtext('id') ②
>>> status_id
'5131472'
>>> url = 'https://identi.ca/api/statuses/destroy/{0}.xml'.format(status_id)
>>> resp, deleted_content = h.request(url, 'DELETE')


