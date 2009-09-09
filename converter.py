import urllib2
from decimal import Decimal

URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={from_curr}{to_curr}=X'

def _get_data(url):
    request = urllib2.Request(url, None, {'Accept-encoding': '*'})
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError:
        return None
    result = response.read()
    return result

def convert(from_curr, to_curr='USD', amount=1.0):
    if from_curr.lower() == to_curr.lower():
        return amt
    
    data = _get_data(URL.format(from_curr=from_curr, to_curr=to_curr))
    if data:
        exchange = data.split(',')
        try:
            return u'{0:.3f}'.format(round(float(exchange[1]) * amount, 3))
        except (IndexError, ValueError):
            pass
    return u'0.000'