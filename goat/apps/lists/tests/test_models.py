
from django.core.exceptions import ValidationError
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

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item_ = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item_.save()          # save() does not trigger validation, DOH!
            item_.full_clean()    # but full_clean() does, hooray

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%s/' % (list_.id,))
