from django.test import SimpleTestCase

# Create your tests here.

class simpletests(SimpleTestCase):
    def check_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def check_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
