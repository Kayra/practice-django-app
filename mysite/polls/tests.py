import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


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
