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
