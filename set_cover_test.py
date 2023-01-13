import unittest
from set_cover import set_cover_greedy

class SetCoverTest(unittest.TestCase):
    def test_empty_universe(self):
        universe = set()
        sets = [{1, 2, 3}, {4, 5}]
        expected = []
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_empty_sets(self):
        universe = {1, 2, 3, 4, 5}
        sets = []
        expected = []
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_simple_1(self):
        universe = {1, 2, 3, 4, 5}
        sets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
        solution = set_cover_greedy(universe, sets)
        self.assertEqual(solution, [{1, 2, 3}, {4, 5}])
        
    def test_simple_2(self):
        universe = {1, 2, 3, 4, 5}
        sets = [{1, 2, 3, 4}, {2, 3, 4, 5}]
        solution = set_cover_greedy(universe, sets)
        self.assertEqual(solution, [{1, 2, 3, 4}, {2, 3, 4, 5}])
        
    def test_simple_3(self):
        universe = {1, 2, 3, 4, 5}
        sets = [{1, 2, 3, 4, 5}]
        solution = set_cover_greedy(universe, sets)
        self.assertEqual(solution, [{1, 2, 3, 4, 5}])
        
    def test_simple_4(self):
        universe = {1, 2, 3, 4, 5}
        sets = [{1}, {2}, {3}, {4}, {5}]
        solution = set_cover_greedy(universe, sets)
        self.assertEqual(solution, [{1}, {2}, {3}, {4}, {5}])

    def test_complex_1(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3}, {4, 5}, {6, 7}, {8, 9, 10}, {1, 4, 7, 10}, {2, 5, 8}]
        expected = [{1, 2, 3}, {4, 5}, {6, 7}, {8, 9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_2(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}]
        expected = [{1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_3(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7}, {8, 9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}]
        expected = [{1, 2, 3, 4}, {5, 6, 7}, {8, 9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_4(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_5(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_6(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}, {2,6,10}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_7(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}, {2,6,10}, {3,7,8}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_8(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}, {2,6,10}, {3,7,8}, {4,9,10}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_9(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}, {2,6,10}, {3,7,8}, {4,9,10}, {5,8,10}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)

    def test_complex_10(self):
        universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        sets = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}, {1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}, {1,5,9}, {2,6,10}, {3,7,8}, {4,9,10}, {5,8,10},{6,7,8}]
        expected = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10}]
        result = set_cover_greedy(universe, sets)
        self.assertEqual(result, expected)


        
    # ... other complex tests ...

if __name__ == '__main__':
    unittest.main()
