
from django.test import TestCase

from goat.apps.lists.models import Item, List

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        alist = List()
        alist.save()

        first_item = Item()
        first_text = 'The first (ever) list item'
        first_item.text = first_text
        first_item.list = alist
        first_item.save()

        second_item = Item()
        second_text = 'Item the second'
        second_item.text = second_text
        second_item.list = alist
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, alist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, first_text)
        self.assertEqual(first_saved_item.list, alist)
        self.assertEqual(second_saved_item.text, second_text)
        self.assertEqual(second_saved_item.list, alist)
