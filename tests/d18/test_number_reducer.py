from unittest import TestCase

from aoc.d18.number_reducer import NumberReducer


class TestNumberReducer(TestCase):
    def setUp(self):
        numbers = [
            '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
            '[[[5,[2,8]],4],[5,[[9,9],0]]]',
            '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
            '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
            '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
            '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
            '[[[[5,4],[7,7]],8],[[8,3],8]]',
            '[[9,3],[[9,9],[6,[4,9]]]]',
            '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
            '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'
        ]
        self.reducer = NumberReducer(numbers)

    def test_reduces_all_combinations_of_snailfish_numbers(self):
        self.assertEqual(len(self.reducer.reduce_all_combinations()), 100)

    def test_reduces_a_list_of_snailfish_numbers(self):
        reduced = '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
        self.assertEqual(self.reducer.reduce(), reduced)

    def test_reduces_another_list_of_snailfish_numbers(self):
        numbers = [
            '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
            '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
            '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
            '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
            '[7,[5,[[3,8],[1,4]]]]',
            '[[2,[2,2]],[8,[8,1]]]',
            '[2,9]',
            '[1,[[[9,3],9],[[9,0],[0,7]]]]',
            '[[[5,[7,4]],7],1]',
            '[[[[4,2],2],6],[8,7]]'
        ]
        reduced = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
        self.assertEqual(NumberReducer(numbers).reduce(), reduced)

    def test_reduces_two_snailfish_numbers_example0(self):
        left = '[[[[4,3],4],4],[7,[[8,4],9]]]'
        right = '[1,1]'
        reduced = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example1(self):
        left = '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]'
        right = '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'
        reduced = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example2(self):
        left = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'
        right = '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]'
        reduced = '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example3(self):
        left = '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]'
        right = '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]'
        reduced = '[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example4(self):
        left = '[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]'
        right = '[7,[5,[[3,8],[1,4]]]]'
        reduced = '[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example5(self):
        left = '[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]'
        right = '[[2,[2,2]],[8,[8,1]]]'
        reduced = '[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example6(self):
        left = '[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]'
        right = '[2,9]'
        reduced = '[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example7(self):
        left = '[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]'
        right = '[1,[[[9,3],9],[[9,0],[0,7]]]]'
        reduced = '[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example8(self):
        left = '[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]'
        right = '[[[5,[7,4]],7],1]'
        reduced = '[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example9(self):
        left = '[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]'
        right = '[[[[4,2],2],6],[8,7]]'
        reduced = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)

    def test_reduces_two_snailfish_numbers_example10(self):
        left = '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]'
        right = '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]'
        reduced = '[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]'
        self.assertEqual(self.reducer.reduce_pair(left, right), reduced)
