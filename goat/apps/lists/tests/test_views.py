from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from goat.apps.lists.models import Item
from goat.apps.lists.views import home_page


class HomePageTest(TestCase):

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

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, spam)

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/uberlist/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/uberlist/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/uberlist/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


