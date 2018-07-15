from django.test import TestCase


class PollsTest(TestCase):

    def test_home_page_redirects_to_polls_index(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/polls/')

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/polls/')
        self.assertTemplateUsed(response, 'polls/index.html')
