import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


def create_question(question_text, days):

    """
    Create a question with given "question_text" and offset the amount of days from now. Amount
    of days should be positive for future date, and negative for a date in the past.
    """

    offsetted_date_to_publish = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=offsetted_date_to_publish)

    return question


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):

        """
        If no questions exist, an appropriate message is displayed
        """

        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_past_question(self):

        """
        Questions with a pub_date in the past are displayed on the index page
        """

        create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question>']
        )


    def test_future_question(self):

        """
        Questions with a pub_date in the future aren't displayed on the index page
        """

        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))

        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_past_and_future_questions(self):

        """
        If both past and future questions exist, only past questions are displayed on the page
        """

        create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question>']
        )


    def test_two_questions(self):

        """
        The questions index page displays multiple questions
        """

        create_question(question_text="Past question one", days=-30)
        create_question(question_text="Past question two", days=-5)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question two>', '<Question: Past question one>']
        )


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        """
        was_published_recently() should return False for questions with pub_date set in the future
        """

        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):

        """
        was_published_recently() returns True for questions with pub_date within the last day
        """

        within_last_day = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=within_last_day)

        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):

        """
        was_published_recently() returns True for questions with pub_date older than one day
        """

        older_than_one_day = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=older_than_one_day)

        self.assertIs(old_question.was_published_recently(), False)
