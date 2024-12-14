import json
from collections import Counter
import os

def load_hot_words(file_paths):
    combined_hot_words = Counter()
    for file_path in file_paths:
        print(f"Loading file: {file_path}")
        with open(file_path, 'r') as f:
            data = json.load(f)
            for topic, hot_words_with_scores in data.items():
                for word, score in hot_words_with_scores:
                    combined_hot_words[word] += score
    return combined_hot_words

def get_top_hot_words(combined_hot_words, top_n=100):
    return combined_hot_words.most_common(top_n)

def save_combined_hot_words(output_file, top_hot_words):
    with open(output_file, 'w') as f:
        json.dump(top_hot_words, f, indent=4, ensure_ascii=False)
    print(f"Top hot words successfully saved to {output_file}")

if __name__ == "__main__":
    input_files = [
        "data/topics/RC_sports_2023-01_hot_words.json",
        "data/topics/RC_sports_2023-02_hot_words.json",
        "data/topics/RC_sports_2023-03_hot_words.json",
        "data/topics/RC_sports_2023-04_hot_words.json",
        "data/topics/RC_sports_2023-05_hot_words.json",
        "data/topics/RC_sports_2023-06_hot_words.json",
        "data/topics/RC_sports_2023-07_hot_words.json",
        "data/topics/RC_sports_2023-08_hot_words.json",
        "data/topics/RC_sports_2023-09_hot_words.json",
        "data/topics/RC_sports_2023-10_hot_words.json",
        "data/topics/RC_sports_2023-11_hot_words.json",
        "data/topics/RC_sports_2023-12_hot_words.json",
        "data/topics/RS_sports_2023-01_hot_words.json",
        "data/topics/RS_sports_2023-02_hot_words.json",
        "data/topics/RS_sports_2023-03_hot_words.json",
        "data/topics/RS_sports_2023-04_hot_words.json",
        "data/topics/RS_sports_2023-05_hot_words.json",
        "data/topics/RS_sports_2023-06_hot_words.json",
        "data/topics/RS_sports_2023-07_hot_words.json",
        "data/topics/RS_sports_2023-08_hot_words.json",
        "data/topics/RS_sports_2023-09_hot_words.json",
        "data/topics/RS_sports_2023-10_hot_words.json",
        "data/topics/RS_sports_2023-11_hot_words.json",
        "data/topics/RS_sports_2023-12_hot_words.json",
    ]

    output_file = "data/yearly/sports_2023_top_100_hot_words.json"

    combined_hot_words = load_hot_words(input_files)
    top_100_hot_words = get_top_hot_words(combined_hot_words, top_n=100)
    save_combined_hot_words(output_file, top_100_hot_words)
