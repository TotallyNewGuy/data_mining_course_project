import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import argparse

def create_wordcloud(year, month, hot_words, output_dir, topic, suffix=""):
    os.makedirs(output_dir, exist_ok=True)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(hot_words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"{topic.capitalize()} - {year} Hot Words")
    plt.axis('off')

    output_path = f"{output_dir}/{topic}_{year}_{month}_{suffix}_wordcloud.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Wordcloud saved to {output_path}")



def create_bar_chart(year, month, hot_words_with_scores, output_dir, topic, suffix=""):
    os.makedirs(output_dir, exist_ok=True)

    words, scores = zip(*hot_words_with_scores)

    plt.figure(figsize=(20, 8))
    plt.bar(words, scores)
    plt.title(f"{topic.capitalize()} - {year}-{month} Hot Words Frequency", fontsize=20)  
    plt.xticks(rotation=60, fontsize=20)  
    plt.yticks(fontsize=18)  
    plt.xlabel("Words", fontsize=24)  
    plt.ylabel("Scores", fontsize=20)  
    plt.subplots_adjust(bottom=0.35)  

    output_path = f"{output_dir}/{topic}_{year}_{month}_{suffix}_barchart.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Bar chart saved to {output_path}")





def process_monthly_files(data_dir, output_dir, topic):
    files = [f for f in os.listdir(data_dir) if f.startswith(topic) and f.endswith("_hot_words.json")]

    for file in files:
        file_path = os.path.join(data_dir, file)
        print(f"Processing file: {file_path}")

        parts = file.split("_")
        year_month = parts[1]  
        year, month = year_month.split("-")

        with open(file_path, 'r') as f:
            hot_words_with_scores = json.load(f)

        hot_words = [word for word, _ in hot_words_with_scores]

        create_wordcloud(year, month, hot_words, os.path.join(output_dir, "wordclouds"), topic)
        create_bar_chart(year, month, hot_words_with_scores, os.path.join(output_dir, "bar_charts"), topic)


def process_yearly_files(data_dir, output_dir, topic):
    files = [f for f in os.listdir(data_dir) if f.startswith(f"filtered_{topic}") and f.endswith("top_10_hot_words.json")]

    for file in files:
        file_path = os.path.join(data_dir, file)
        print(f"Processing file: {file_path}")

        parts = file.split("_")
        year = parts[1]
        suffix = parts[2]  

        with open(file_path, 'r') as f:
            hot_words_with_scores = json.load(f)

        
        hot_words = [word for word, _ in hot_words_with_scores]

        create_wordcloud(year, "annual", hot_words, os.path.join(output_dir, "wordclouds"), topic, suffix=f"_{suffix}")
        create_bar_chart(year, "annual", hot_words_with_scores, os.path.join(output_dir, "bar_charts"), topic, suffix=f"_{suffix}")





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize monthly and yearly hot words for specific topics.")
    parser.add_argument("--data_dir", required=True, help="Directory containing hot words JSON files.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the generated visualizations.")
    parser.add_argument("--topic", required=True, choices=["economics", "sports", "politics"], help="Specify the topic (economics, sports, politics)")

    args = parser.parse_args()

    if "monthly" in args.data_dir:
        process_monthly_files(args.data_dir, args.output_dir, args.topic)
    elif "yearly" in args.data_dir:
        process_yearly_files(args.data_dir, args.output_dir, args.topic)
    else:
        print("Error: The data directory must contain 'monthly' or 'yearly' in its name.")
