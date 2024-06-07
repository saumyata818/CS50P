import unittest
from unittest.mock import patch
from project import calculate_percentage, calculate_gpa, main

class TestProject(unittest.TestCase):

    def test_calculate_percentage(self):
        subject_marks = {'Mathematics': 80, 'Science': 90, 'English': 75}
        self.assertAlmostEqual(calculate_percentage(subject_marks), 81.66666666666667)

    def test_calculate_gpa(self):
        self.assertEqual(calculate_gpa(95), 4.0)
        self.assertEqual(calculate_gpa(85), 3.5)
        self.assertEqual(calculate_gpa(75), 3.0)
        self.assertEqual(calculate_gpa(65), 2.5)
        self.assertEqual(calculate_gpa(55), 2.0)
        self.assertEqual(calculate_gpa(45), 1.5)
        self.assertEqual(calculate_gpa(35), 0.0)

    @patch('builtins.input', side_effect=["John Doe", "12345", "85", "90", "75", "60", "70"])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()

        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Percentage" in line and "76.00" in line for line in output))
        self.assertTrue(any("GPA" in line and "3.00" in line for line in output))
        self.assertTrue(any("Result: Pass" in line for line in output))

if __name__ == '__main__':
    unittest.main()
