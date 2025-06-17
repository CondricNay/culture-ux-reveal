import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

class TestEdgeSeleniumHeadless(unittest.TestCase):
    def setUp(self):
        edge_options = Options()
        edge_options.add_argument("--headless")        # Run without UI
        edge_options.add_argument("--disable-gpu")     # Disable GPU acceleration
        edge_options.add_argument("--window-size=1920,1080")  # Optional: set resolution

        self.driver = webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()),
            options=edge_options
        )
    
    def test_example_com_title(self):
        self.driver.get("https://example.com")
        h1_element = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Example Domain")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
