import time

from django.test import LiveServerTestCase
from django.utils import timezone
from selenium import webdriver

from polls.models import Choice, Question


class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_browse_polls_and_vote(self):
        # There's a new poll app that has a couple of questions in it
        question_1 = Question.objects.create(
            question_text='Dogs or cats?', pub_date=timezone.now())
        Choice.objects.create(question=question_1, choice_text='Dogs')
        Choice.objects.create(question=question_1, choice_text='Cats')

        #:- Filler questions, maybe remove these?
        question_2 = Question.objects.create(
            question_text='Do you think it will rain?', pub_date=timezone.now())
        question_3 = Question.objects.create(
            question_text='Chocolates or flowers?', pub_date=timezone.now())

        # John heared about it and visited to see what's up
        self.browser.get(self.live_server_url)

        # He sees that indeed, the app is about answering polls
        title_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn(title_text, 'Polls')

        # There's a list of polls to answer, he chooses the first one
        polls_list = self.browser.find_elements_by_css_selector(
            'ul#polls>li>a')
        polls_list[0].click()

        time.sleep(1)

        # He is sent to another page where there's a question and
        # a list of answers to choose from
        self.assertRegex(self.browser.current_url, r'/polls/.+')
        self.assertTrue(
            self.browser.find_element_by_css_selector('h2#poll-question').text)
        self.assertTrue(
            self.browser.find_element_by_css_selector('ul#choices').text)

        self.fail('Finish the tests!')
        # He chose the second answer and submitted his choice

        # He was then sent to a 'results' page where he can sees the
        # results of the polls he just answered

        # Satisfied, he went back to sleep
