import unittest 


###############################################

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')
		#unit test to check if uppercase

	def test_isupper(self)
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
		# test if there is an uppercase in the word
	def test_split(self):
		#variable s equal to string
		s = 'hello world'
		self.assertEqual(s.split(), [ 'hello', 'world'])

		#Check that s.split fails when the seperator is not a string

		with self.assertRaises(TypeError):
			s.split(2)

	if __name__ == '__main__':
		unittest.main()