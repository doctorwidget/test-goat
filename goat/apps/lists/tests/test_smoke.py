from django.core.urlresolvers import resolve
from django.test import TestCase

class SmokeTests(TestCase):

    def test_sanity(self):
        """Confirm that math works today."""
        self.assertEqual(1 + 1, 2)

