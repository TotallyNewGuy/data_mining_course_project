import pandas as pd
import os

class PoolManager:
    def __init__(self, input_file, output_file, batch_size):
        self.input_file = input_file
        self.output_file = output_file
        self.batch_size = batch_size
        self.pool = []
        self.processed = self.load_processed()

    def load_processed(self):
        if os.path.exists(self.output_file):
            df = pd.read_csv(self.output_file)
            return set(df['post_id'])
        return set()

    def load_input(self):
        if os.path.exists(self.input_file):
            df = pd.read_csv(self.input_file)
            return df[~df['post_id'].isin(self.processed)]
        else:
            raise FileNotFoundError(f"Input file {self.input_file} not found.")

    def initialize_pool(self):
        data = self.load_input()
        self.pool = data.to_dict('records')  # [{'post_id': ..., 'text': ...}, ...]

    def get_batch(self):
        batch = self.pool[:self.batch_size]
        self.pool = self.pool[self.batch_size:]
        left = len(self.pool)
        print(f"Pool size: {left}")
        return batch

    def replenish(self, failed_texts):
        self.pool.extend(failed_texts)
