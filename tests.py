import unittest
import converter

class ConverterTestCase(unittest.TestCase):
    
    def test_converter(self):
        usd = converter.convert('usd', 'usd', 1.00)
        self.assertEquals(usd, 1.0)
        
        jpy = converter.convert('usd', 'jpy', 1.00)
        self.assertEquals(type(1.0), type(jpy))