import openai
import multiprocessing
from config import API_KEYS, MODELS
import prompt
import ast
import time
from datetime import datetime

class TextAnalyzer:
    def __init__(self):
        self.api_keys = API_KEYS
        self.models = MODELS

    def analyze_texts(self, texts, token_index):
        api_key = self.api_keys[token_index]
        print("Using API: ", token_index)
        client = openai.OpenAI(api_key=api_key)
        results = []
        batch_size = len(texts)
        
        query_str = ""
        for item in texts:
            query_str += item['post_id'] + " # " + item['context'] + "\n"

        query_str += f"You should generate {batch_size} maps, one for each line of text. If you done well, I will give you 100 dollars as a reward."

        # print("Processing text: ", query_str)
        start_time = time.time()
        try:
            response = client.chat.completions.create(
                model=self.models[0],  # Add logic for cycling models if necessary
                messages=[
                            {
                                "role": "system",
                                "content": [
                                    {
                                    "type": "text",
                                    "text": prompt.initial_system_prompt_refined
                                    }
                                ]
                            },
                            {
                                "role": "user",
                                "content": [
                                    {
                                    "type": "text",
                                    "text": query_str
                                    }
                                ]
                            }
                        ]
                )
            raw_results = response.choices[0].message.content
            for raw_map in raw_results.split("\n"):
                try:
                    result = ast.literal_eval(raw_map)
                    results.append(result)
                except Exception as e:
                    print("Error: ", e, "Skipping map.")
                    continue
        except Exception as e:
            print("Error: ", e)
        # results = results[:batch_size-1]
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),end=" ")
        print(f"Processed {batch_size} texts in {time.time() - start_time} seconds.")
        return results

    def multi_process_analyze(self, batches, tokens):
        with multiprocessing.Pool(len(tokens)) as pool:
            results = pool.starmap(self.analyze_texts, zip(batches, range(len(tokens))))
        return results