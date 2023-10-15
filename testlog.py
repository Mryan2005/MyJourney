import unittest
from main import log

class TestLog(unittest.TestCase):
    def test_same_province_and_city(self):
        dir = {}
        province = "Beijing"
        city = "Beijing"
        sights = "Forbidden City"
        time = "2023.1.7-15:00"
        thinkings = "thoughts"
        files = ["file1.txt", "file2.txt"]
        
        result = log(dir, province, city, sights, time, thinkings, files)
        
        self.assertEqual(result, 0)
        self.assertEqual(dir, {
            "Beijing": {
                "Forbidden City": {
                    "2023.1.7-15:00": {
                        "thoughts": ["file1.txt", "file2.txt"]
                    }
                }
            }
        })

    def test_different_province_and_city(self):
        dir = {}
        province = "Guangxi"
        city = "Guling"
        sights = "Xiangbi Mountain"
        time = "2023.1.7-15:00"
        thinkings = "ideas"
        files = ["file3.txt", "file4.txt"]
        
        result = log(dir, province, city, sights, time, thinkings, files)
        
        self.assertEqual(result, 0)
        self.assertEqual(dir, {
            "Guangxi": {
                "Guling": {
                    "Xiangbi Mountain": {
                        "2023.1.7-15:00": {
                            "ideas": ["file3.txt", "file4.txt"]
                        }
                    }
                }
            }
        })

if __name__ == "__main__":
    unittest.main()