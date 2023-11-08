import unittest 
from name_function import get_formatted_name 

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        #This is the test below vv
        formatted_name = get_formatted_name('janis', 'joplin')
        #The result of the test is then evaluated below vv
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Puck' work?"""
        formatted_name = get_formatted_name('Wolfgang', 'Amadeus', 'Puck')
        self.assertEqual(formatted_name, 'Wolfgang Puck Amadeus')

if __name__ == '__main__':
    unittest.main()

