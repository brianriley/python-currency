import urllib2

URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={from_curr}{to_curr}=X'

def _get_data(url):
    request = urllib2.Request(url, None, {'Accept-encoding': '*'})
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError:
        return None
    result = response.read()
    return result

def convert(from_curr, to_curr='USD', amt=1.0):
    if from_curr.lower() == to_curr.lower():
        return amt
    
    data = _get_data(URL.format(from_curr=from_curr, to_curr=to_curr))
    if data:
        exchange = data.split(',')
        try:
            return float(exchange[1]) * amt
        except (IndexError, ValueError):
            pass
    return 0.0