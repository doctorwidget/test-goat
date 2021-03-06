"""Functional testing module for Harry Percivals' TDD book."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Ursula hears about our cool new web app and goes to check out
        self.browser.get(self.server_url)

        # she notices the page title and header mention to-do lists
        todo = 'To-Do'
        self.assertIn(todo, self.browser.title)
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(todo, header)

        # she is invited to enter a to-do item somewhere on the page
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # 1. Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        itemOne = '1: Buy peacock feathers'
        self.check_for_row_in_list_table(itemOne)

        # there is still text inviting her to add another item. She enters
        # "use peacock feathers to make a fly" (she is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list.
        self.check_for_row_in_list_table(itemOne)
        itemTwo = '2: Use peacock feathers to make a fly'
        self.check_for_row_in_list_table(itemTwo)

        # Now a new user, Francis, comes along to the site
        ## Use a new browser session to protect vs shenanigans
        ## due to cookies and sessions
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page and does *not* see Edith's list.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(itemOne, page_text)
        self.assertNotIn(itemTwo, page_text)

        # Francis starts a new list by entering a new item.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # There should still be no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #Satisfied, they both go back to sleep

