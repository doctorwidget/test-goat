
from django.test import TestCase

from goat.apps.lists.models import Item

class ItemModelTester(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_text = 'The first (ever) list item'
        first_item.text = first_text
        first_item.save()

        second_item = Item()
        second_text = 'Item the second'
        second_item.text = second_text
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, first_text)
        self.assertEqual(second_saved_item.text, second_text)
