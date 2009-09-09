import urllib
import csv
from cStringIO import StringIO

URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={from_curr}{to_curr}=X'

def convert(from_curr, to_curr='USD', amt=1.0):
    if from_curr == to_curr:
        return amt
    response = urllib.urlopen(URL.format(from_curr=from_curr, to_curr=to_curr)).read()
    buff = StringIO()
    buff.write(response)
    
    curr_reader = csv.reader([buff.getvalue()])
    exchange = curr_reader.next()
    return float(exchange[1]) * amt