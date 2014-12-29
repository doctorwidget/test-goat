from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from goat.apps.lists.views import home_page


class ListViewsTester(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected)

    def test_home_page_can_save_a_POST_request(self):
        spam = "buy more spam"
        request = HttpRequest()
        request.method = 'POST'
        request.POST['new_item'] = spam

        response = home_page(request)

        expected_html = render_to_string(
            'lists/home.html',
            {'new_item_text': spam}
        )
        self.assertEqual(response.content.decode(), expected_html)
