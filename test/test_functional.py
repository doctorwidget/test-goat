"""Functional testing module for Harry Percivals' TDD book."""
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Ursula hears about our cool new web app and goes to check out
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item somewhere on the page

        # she types "buy peacock feathers" into a text box

        # when she hits enter, the page updates, and now the page lists 1. Buy peacock
        # feathers as an item in a to-do list

        # there is still text inviting her to add another item. She enters "use peacock
        # feathers to make a fly" (she is very methodical)

        # The page updates agian, and now shows both items on her list. 


        # Edith wonders whether or not the site will remember her list. Then she sees
        # that the site has generated a unique URL for her. There is now some
        # explanatory text to that effect


        # She visits that URL and sees that her to-do list is still there.

        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
      unittest.main(warnings='ignore')

