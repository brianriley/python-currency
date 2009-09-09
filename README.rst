Usage
-----

::

	>>> converter.convert(from_curr='usd', to_curr='jpy')
	u'92.045'
	>>> converter.convert(from_curr='jpy')  # default is USD
	u'0.011'
	>>> converter.convert(from_curr='usd', to_curr='jpy', amount=2.5)
	u'230.113'


Disclaimer
----------

This module uses Yahoo Finance to convert currencies. As such, it is not intended for up-to-the-minute accuracy. Use at your own risk.