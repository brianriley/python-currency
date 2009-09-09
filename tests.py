import unittest
import converter

class ConverterTestCase(unittest.TestCase):
    
    def test_usd(self):
        usd = converter.convert('usd', 'USD', 1.00)
        self.assertEquals(usd, 1.0)
        
    def test_jpy(self):
        jpy = converter.convert('usd', 'jpy', 1.00)
        self.assertEquals(type(u'1.0'), type(jpy))
        self.assertNotEquals(jpy, u'0.000')
    
    def test_dummy_currency(self):
        foo = converter.convert('usd', 'foo', 1.00)
        self.assertEquals(foo, u'0.000')

if __name__ == '__main__':
    unittest.main()