import unittest
import sys
sys.path.append('/workspace/OpenHands')
from evaluation.benchmarks.aime.run_infer import parse_final_answer

class TestAnswerExtraction(unittest.TestCase):
    def test_single_answer(self):
        text = "Here's the answer: <<FINAL_ANSWER||289||FINAL_ANSWER>>"
        result = parse_final_answer(text)
        self.assertEqual(result, ['289'])

    def test_multiple_answers(self):
        text = "First answer: <<FINAL_ANSWER||289||FINAL_ANSWER>> Second answer: <<FINAL_ANSWER||881||FINAL_ANSWER>>"
        result = parse_final_answer(text)
        self.assertEqual(result, ['289', '881'])

    def test_case_insensitivity(self):
        text = "Answer: <<final_answer||42||FINAL_ANSWER>>"
        result = parse_final_answer(text)
        self.assertEqual(result, ['42'])

    def test_whitespace_variation(self):
        text = "Answer: <<FINAL_ANSWER  ||  123  ||  FINAL_ANSWER  >>"
        result = parse_final_answer(text)
        self.assertEqual(result, ['123'])

    def test_newline_in_answer(self):
        text = "Answer: <<FINAL_ANSWER||\n456\n||FINAL_ANSWER>>"
        result = parse_final_answer(text)
        self.assertEqual(result, ['456'])

    def test_no_answer(self):
        text = "There is no answer here."
        result = parse_final_answer(text)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()