# Unit tests for grayscii.py

# imports
try:
    import grayscii
except ImportError as e:
    import sys
    sys.path.append('.')
    import grayscii

import unittest
from PIL import Image

# test case
class TestConvert(unittest.TestCase):
    """
    Tests for the convert_image() function of grayscii.py
    """
    def setUp(self) -> None:
        """
        Set up the test image to use
        """
        self.image = Image.radial_gradient('L')

        return super().setUp()


    def testResize(self):
        """
        tests convert_image()'s resizing
        """
        dimensions = (4, 5)
        grid = grayscii.convert_image(self.image, dimensions, 'a')
        self.assertEqual(grid.width, dimensions[0], msg="Grid width was not resized correctly")
        self.assertEqual(grid.height, dimensions[1], msg="Grid height was not resized correctly")


    def testNoPalette(self):
        """
        tests convert_image() for a palette of length zero (expect failure)
        """
        with self.assertRaises(ValueError) as context:
            grayscii.convert_image(self.image, None, '')


    def testLargePalette(self):
        """
        Tests conversion with a large palette
        """
        expected = "_*^#!988889!#^*_\n*^@0754334579@%*\n^@9631zyyz1369@%\n#063zwvutuwz369#\n!73zwtqppqsvz37!\n951wtpmllmpsw159\n84zvqmjhhjmquz48\n83yuplhddglpty37\n83ytplhdcgkpty37\n84zuqmjggimquz48\n951wspmlkmpsw159\n!73zvsqppqsvz37!\n#963zwuttuwz269#\n^@9631zyyz1369@%\n*%@9754334579@%*\n_*%#!987789!#%*_\n"
        grid = grayscii.convert_image(self.image, (16, 16), 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=')
        actual = str(grid)
        
        self.assertEqual(len(expected), len(actual), msg="Result was of a different length than the expected result")
        self.assertEqual(expected, actual, msg="Ascii conversion yielded a different result than the expected value")


    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()