import unittest
from main import Computer, OS, OSComputer, A1, A2, A3


class RK1_test(unittest.TestCase):

    def setUp(self):
        self.computers = [
            # id, name
            Computer(1, 'PC-007'),
            Computer(2, '2Comp WS-01')
        ]
        self.oss = [
            # id, type, price, name, id компьютера
            OS(1, 'Графический', 0, 'linux', 1),
            OS(2, 'Текстовый', 0, 'Dos', 2),
            OS(3, 'Графический', 12000, 'Windows10', 3)
        ]
        # os_id, computer_id
        oss_computers = [
            OSComputer(1, 1),
            OSComputer(2, 2),
            OSComputer(2, 3)
        ]

    def test_A1(self):
        expected_result = [
            ('Dos', '2Comp WS-01', 'Текстовый', 0),
            ('linux', 'PC-007', 'Графический', 0)
        ]

        result = A1(self.computers, self.oss)
        self.assertEqual(result, expected_result)

    def test_A2(self):
        expected_result = [
            ('2Comp WS-01', 0),
            ('PC-007', 0)
        ]
        result = A2(self.computers, self.oss)
        self.assertEqual(result, expected_result)

    def test_A3(self):
        expected_result = [
            ('2Comp WS-01', ['Dos'])
        ]
        result = A3(self.computers, self.oss, 'Comp')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()