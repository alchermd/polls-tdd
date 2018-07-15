from django.test import TestCase
from django.utils import timezone

from .models import Choice, Question


class PollsTest(TestCase):

    def test_home_page_redirects_to_polls_index(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/polls/')

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/polls/')
        self.assertTemplateUsed(response, 'polls/index.html')

    def test_home_page_displays_all_questions(self):
        question_1 = Question.objects.create(
            question_text='This is question 1', pub_date=timezone.now())
        question_2 = Question.objects.create(
            question_text='This is question 2', pub_date=timezone.now())

        response = self.client.get('/polls/')
        self.assertContains(response, question_1.question_text)
        self.assertContains(response, question_2.question_text)

    def test_show_poll_page_uses_correct_template(self):
        new_question = Question.objects.create(
            question_text='How are you?', pub_date=timezone.now())
        response = self.client.get(f'/polls/{new_question.id}/')
        self.assertTemplateUsed(response, 'polls/show.html')

    def test_show_poll_page_displays_its_choices(self):
        new_question = Question.objects.create(question_text='How are you?',
                                               pub_date=timezone.now())
        choice_1 = Choice.objects.create(question=new_question,
                                         choice_text="Doing good!")
        choice_2 = Choice.objects.create(question=new_question,
                                         choice_text="Not doing well.")

        response = self.client.get(f'/polls/{new_question.id}/')
        self.assertContains(response, choice_1.choice_text)
        self.assertContains(response, choice_2.choice_text)
