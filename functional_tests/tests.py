from django.test import LiveServerTestCase
from selenium import webdriver


class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_browse_polls_and_vote(self):
        # John heared about our new polls app and visited it
        # to see what's up
        self.browser.get(self.live_server_url)

        # He sees that indeed, the app is about answering polls
        title_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn(title_text, 'Polls')

        self.fail('Finish the tests!')
        # There's a list of polls to answer, he chooses the first one

        # He is sent to another page where there's a question and
        # a list of answers to choose from

        # He chose the second answer and submitted his choice

        # He was then sent to a 'results' page where he can sees the
        # results of the polls he just answered

        # Satisfied, he went back to sleep
