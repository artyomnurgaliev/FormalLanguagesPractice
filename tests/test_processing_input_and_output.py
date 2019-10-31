import solution


class TestClass:
    def test_processing_input(self):
        solution.input = lambda: 'ab+ aba'
        output = solution.process_input()
        assert output[0] == 'ab+'
        assert output[1] == 'aba'

    def teardown_method(self, method):
        solution.input = input

