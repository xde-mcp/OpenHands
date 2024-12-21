import json
import sys
sys.path.append('/workspace/OpenHands')
from evaluation.benchmarks.aime.run_infer import parse_final_answer

def test_extraction():
    with open('/workspace/output-new2.jsonl', 'r') as f:
        for line_number, line in enumerate(f, 1):
            data = json.loads(line)
            history = data.get('history', [])
            for turn_index, turn in enumerate(history):
                for message_index, message in enumerate(turn):
                    if message.get('source') == 'agent':
                        content = message.get('message', '')
                        answers = parse_final_answer(content)
                        if answers:
                            for answer_index, answer in enumerate(answers):
                                path = f"[{line_number-1}].history[{turn_index}][{message_index}].message"
                                print(f"Answer: {answer}")
                                print(f"Path: {path}")
                                print(f"jq command: jq '{path}' /workspace/output-new2.jsonl")
                                print()

if __name__ == "__main__":
    test_extraction()