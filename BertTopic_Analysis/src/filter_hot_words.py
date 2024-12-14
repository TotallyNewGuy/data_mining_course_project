import json
import os

custom_stop_words = {
    "post", "posts", "removed", "submission", "submissions", "bot", "moderator", "moderators",
    "discussed", "subreddit", "sub", "rule", "rules", "discussion", "comment", "commenting",
    "comments", "message", "submit", "submitting", "posting", "content", "ban", "removal",
    "thread", "threads", "mod", "mods", "compose", "action", "violating", "approved", "economic", 
    "economics", "economist", "remindmebot", "question", "asking", "questions", "contact", 
    "economists", "allow", "discuss", "elaboration", "resubmit", "domains", "domain", "opinion", 
    "opinions", "spaces", "article", "economy", "reddit", "topic", "idea", "isn", "performed"
}

def filter_hot_words(input_file, output_file, stop_words):
   
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, 'r') as f:
        hot_words = json.load(f)

    filtered_hot_words = [item for item in hot_words if item[0].lower() not in stop_words]

    with open(output_file, 'w') as f:
        json.dump(filtered_hot_words, f, indent=4, ensure_ascii=False)

    print(f"Filtered hot words saved to {output_file}")

if __name__ == "__main__":
    input_files = [
        "data/yearly/economics_2023_top_100_hot_words.json",
        "data/yearly/sports_2023_top_100_hot_words.json",
        "data/yearly/politics_2023_top_100_hot_words.json"
    ]

    output_dir = "data/yearly"

    for input_file in input_files:
        output_file = os.path.join(output_dir, f"filtered_{os.path.basename(input_file)}")
        
        filter_hot_words(input_file, output_file, custom_stop_words)
