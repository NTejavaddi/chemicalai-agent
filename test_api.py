import unittest
from backend.api import InputData, predict

class TestChemicalAIAgent(unittest.TestCase):

    def test_predict_typical_case(self):
        data = InputData(400, 5, 0.05, 5)
        result = predict(data)
        self.assertIn("predicted_yield", result)
        self.assertIsInstance(result["predicted_yield"], float)

    def test_predict_bounds(self):
        data = InputData(300, 1, 0.01, 1)
        result = predict(data)
        self.assertGreaterEqual(result["predicted_yield"], 0)

    def test_predict_invalid_input(self):
        with self.assertRaises(ValueError):
            InputData("high", "low", "none", "zero")

if __name__ == "__main__":
    unittest.main()
