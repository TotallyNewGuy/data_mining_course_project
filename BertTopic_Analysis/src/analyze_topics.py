import re
from bertopic import BERTopic
from umap import UMAP
from hdbscan import HDBSCAN
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.vectorizers import ClassTfidfTransformer
from bertopic.representation import KeyBERTInspired
import os
import gc
import argparse

os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface_cache"
os.environ["HF_HOME"] = "/tmp/huggingface_home"

def analyze_topics(input_file, output_file, batch_size=50):
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Processing file: {input_file}")
    data = pd.read_csv(input_file, on_bad_lines='skip', engine='python')

    all_texts = data['context'].dropna().tolist()
    all_texts = [text for text in all_texts if len(text.split()) > 5]

    if len(all_texts) < 2:
        print(f"Skipping file {input_file} due to insufficient text data.")
        return

    try:
        umap_model = UMAP(n_neighbors=3, n_components=2, min_dist=0.3, metric='cosine')
        hdbscan_model = HDBSCAN(min_cluster_size=5, min_samples=1, metric='euclidean')
        vectorizer_model = CountVectorizer(stop_words="english")
        ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
        representation_model = KeyBERTInspired()

        topic_model = BERTopic(
            embedding_model="/home/jovyan/work/Angus/Dm_BertTopic_project/models/all-MiniLM-L6-v2",
            umap_model=umap_model,
            hdbscan_model=hdbscan_model,
            vectorizer_model=vectorizer_model,
            ctfidf_model=ctfidf_model,
            representation_model=representation_model,
            low_memory=True
        )
    except Exception as e:
        print(f"Error initializing BERTopic model: {e}")
        return

    hot_words_with_scores = {}

    for i in range(0, len(all_texts), batch_size):
        batch_texts = all_texts[i:i + batch_size]

        valid_batch_texts = [text for text in batch_texts if text.strip()]
        if not valid_batch_texts:
            print(f"Skipping batch {i // batch_size + 1} due to no valid texts.")
            continue

        print(f"Processing batch {i // batch_size + 1}/{(len(all_texts) // batch_size) + 1} with {len(valid_batch_texts)} valid texts...")

        try:
            topics, _ = topic_model.fit_transform(valid_batch_texts)

            topic_words = topic_model.get_topics()
            for j, topic_id in enumerate(topics):
                if topic_id == -1:
                    continue
                hot_words = topic_words.get(topic_id, [])[:10]
                if hot_words:
                    hot_words_with_scores[f"batch_{i // batch_size + 1}_topic_{j}"] = hot_words

        except ValueError as e:
            print(f"Error while modeling batch {i // batch_size + 1}: {e}")
            continue  

    def convert_float32_to_float(data):
        if isinstance(data, dict):
            return {key: convert_float32_to_float(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_float32_to_float(item) for item in data]
        elif isinstance(data, (np.float32, np.float64)):
            return float(data)
        elif isinstance(data, tuple):
            return tuple(convert_float32_to_float(item) for item in data)
        else:
            return data


 
    hot_words_with_scores = convert_float32_to_float(hot_words_with_scores)

  
    if hot_words_with_scores:
        with open(output_file, "w") as f:
            json.dump(hot_words_with_scores, f, indent=4, ensure_ascii=False)
        print(f"Hot words successfully saved to {output_file}.")
    else:
        print(f"No hot words found for {input_file}.")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process specific topic files.")
    parser.add_argument("--file", required=True, help="Path to the input file")
    parser.add_argument("--output", required=True, help="Path to the output JSON file")

    args = parser.parse_args()
    analyze_topics(args.file, args.output, batch_size=1000)

