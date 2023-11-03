import unittest

from back.main import MODELS


class TestModel(unittest.TestCase):

    def test_models_ok(self):
        for model in MODELS:
            assert (model != None)
            print(str(model), "is available")

if __name__ == '__main__':
    unittest.main()