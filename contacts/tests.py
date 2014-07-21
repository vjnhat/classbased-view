from django.test import TestCase

# Create your tests here.

from contacts.models import Contact

class ContactTests(TestCase):
	""" Contacts Model Test """

	def test_str(self):
		contact=Contact(first_name='John', last_name='Smith')
		self.assertEquals(
			str(contact),
			'John Smith'
			)