"""Functional testing module for Harry Percivals' TDD book."""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

