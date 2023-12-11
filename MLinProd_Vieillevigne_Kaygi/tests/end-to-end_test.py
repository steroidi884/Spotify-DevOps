import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestAppEndToEnd(unittest.TestCase):
    def setUp(self):
        # Configure le navigateur WebDriver
        self.driver = webdriver.Chrome()  
        self.driver.get('http://localhost:5000/')  
    def tearDown(self):
        self.driver.quit()

    def test_add_suggestion_end_to_end(self):
        # Test d'ajout d'une suggestion
        artist_input = self.driver.find_element_by_id('artiste')
        music_input = self.driver.find_element_by_id('musique')
        submit_button = self.driver.find_element_by_id('btn-add')

        artist_input.send_keys('Nouvel Artiste')
        music_input.send_keys('Nouvelle Musique')
        submit_button.click()

        # Vérifie que la suggestion est présente dans le tableau
        table_rows = self.driver.find_elements_by_xpath('//table[@id="table-dyn"]/tbody/tr')
        last_row = table_rows[-1]
        self.assertIn('Nouvel Artiste', last_row.text)
        self.assertIn('Nouvelle Musique', last_row.text)

if __name__ == '__main__':
    unittest.main()
