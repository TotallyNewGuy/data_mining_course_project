
# Subreddit Text Sentiment Analysis

This repository provides tools to perform sentiment analysis on text data using OpenAI's API. The sentiment types align with those defined in [Google's GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions).

## Folder Structure

```
sentiment-agent/
├── data/
│   ├── errors.csv
│   ├── input.csv
│   ├── output.csv
├── analyzer.py
├── config.py
├── main.py
├── pool_manager.py
├── prompt.py
├── readme.md
├── requirements.txt
├── utils.py
```

## File Descriptions

- **`data/`**: Contains the input (`input.csv`) and output (`output.csv`) data files.
- **`analyzer.py`**: Analyzes text sentiment in batches by calling the OpenAI API.
- **`config.py`**: Configuration file (e.g., storing API keys and other settings).
- **`main.py`**: The main program to run sentiment analysis.
- **`pool_manager.py`**: Manages a pool of text data for analysis.
- **`prompt.py`**: Contains prompts used in the sentiment analysis.
- **`readme.md`**: This README file.
- **`requirements.txt`**: Lists required Python packages.
- **`utils.py`**: Provides utility functions.

## Supported Sentiment Types

The tool supports the following sentiment categories as defined in the [GoEmotions project](https://github.com/google-research/google-research/tree/master/goemotions):

- admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, and neutral.

## How to Run

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Prepare the input data:
   - Add the text to be analyzed in the `data/input.csv` file, following the required format.
3. Run the main program:
   ```bash
   python main.py
   ```
4. Collect the results:
   - The analysis results will be saved in the `data/output.csv` file.

### Resume Support

This tool supports resuming from the last run. If the program is interrupted, it will continue processing from where it stopped.

## Configuration

- Add your OpenAI API key in the `config.py` file.

## License

This project is licensed under the MIT License.
