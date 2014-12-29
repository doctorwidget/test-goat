"""Functional testing module for Harry Percivals' TDD book."""
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, expected):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(expected, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Ursula hears about our cool new web app and goes to check out
        self.browser.get(self.live_server_url)

        # she notices the page title and header mention to-do lists
        todo = 'To-Do'
        self.assertIn(todo, self.browser.title)
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(todo, header)

        # she is invited to enter a to-do item somewhere on the page
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # 1. Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        itemOne = '1: Buy peacock feathers'
        self.check_for_row_in_list_table(itemOne)

        # there is still text inviting her to add another item. She enters
        # "use peacock feathers to make a fly" (she is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list.
        self.check_for_row_in_list_table(itemOne)
        itemTwo = '2: Use peacock feathers to make a fly'
        self.check_for_row_in_list_table(itemTwo)

        # Edith wonders whether or not the site will remember her list. Then
        # she sees that the site has generated a unique URL for her. There is
        #  now some explanatory text to that effect
        self.fail('Finish the test! Still need to generate a unique URL')

        # She visits that URL and sees that her to-do list is still there.

        # Satisfied, she goes back to sleep.

