# BERTopic-Based Hot Words Analysis and Visualization

This project analyzes Reddit data to identify trending hot words in different topics (economics, sports, and politics) using the BERTopic library. It also provides visualizations in the form of word clouds and bar charts for monthly and yearly data.

## **Features**

- **Topic Modeling:** Uses BERTopic to analyze large datasets and identify trending hot words.
- **Data Processing:** Combines and filters hot words data for different topics.
- **Visualization:** Generates word clouds and bar charts to visualize hot words and their frequencies.

## **Directory Structure**

```plaintext
Dm_BertTopic_project/
├── data/                    # Contains input data
│   ├── decompress/          # Decompressed Reddit data files
│   ├── monthly/             # Monthly hot words JSON files
│   ├── topics/              # Intermediate topic data
│   └── yearly/              # Yearly hot words JSON files
├── models/                  # Pre-trained BERTopic models
│   ├── all-MiniLM-L6-v2/   # Extracted model
│   └── all-MiniLM-L6-v2.zip
├── plots/                   # Output visualizations
│   ├── bar_charts/          # Bar charts of hot words
│   └── wordclouds/          # Word clouds of hot words
└── src/                     # Source code
    ├── analyze_topics.py    # Analyze topics using BERTopic
    ├── combine_hot_words_*.py # Scripts for combining hot words
    ├── filter_hot_words.py  # Filter out common/irrelevant words
    └── visualize.py         # Generate word clouds and bar charts
```

## **Dependencies**

To run this project, install the following dependencies:

### **1. Install PyTorch (CPU version)**

```bash
pip install torch
```

or a specific version:

```bash
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

### **2. Install Dependencies for BERTopic**

```bash
pip install umap-learn hdbscan
pip install bertopic
```

### **3. Install WordCloud**

```bash
pip install wordcloud
```

## **How to Run**

### **1. Analyze Topics**

To analyze Reddit data and generate hot words:

```bash
python src/analyze_topics.py --file data/decompress/<your_file>.csv --output data/topics/<output_file>.json
```

### **2. Combine Hot Words**

Combine hot words for a specific topic:

```bash
python src/combine_hot_words_economics.py
```

### **3. Visualize Hot Words**

Generate word clouds and bar charts:

- **For Monthly Data**:

  ```bash
  python src/visualize.py --data_dir data/monthly --output_dir plots --topic economics
  ```

- **For Yearly Data**:

  ```bash
  python src/visualize.py --data_dir data/yearly --output_dir plots --topic sports
  ```

## **Sample Output**

- **Word Clouds:** Saved in `plots/wordclouds/`
- **Bar Charts:** Saved in `plots/bar_charts/`

## **Example Commands**

```bash
python src/visualize.py --data_dir data/monthly --output_dir plots --topic politics
```

This command generates visualizations for monthly hot words related to politics and saves them in the `plots` directory.
