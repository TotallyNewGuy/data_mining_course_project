from pool_manager import PoolManager
from analyzer import TextAnalyzer
from utils import save_results_to_csv, validate_result
from config import OUTPUT_FILE, ERROR_FILE, INPUT_FILE, BATCH_SIZE
import signal

def signal_handler(sig, frame):
    print("KeyboardInterrupt received. Exiting...")
    exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print("Creating the pool manager... ...")
    pool_manager = PoolManager(input_file=INPUT_FILE, output_file=OUTPUT_FILE, batch_size=BATCH_SIZE)
    print("Creating the text analyzer... ...")
    analyzer = TextAnalyzer()

    # Load input data into the pool
    print("Initializing the pool... ...")
    pool_manager.initialize_pool()

    while pool_manager.pool:
        failed_results = []
        
        batch = pool_manager.get_batch()
        results = analyzer.multi_process_analyze([batch], analyzer.api_keys)
        print("Results #: ", len(results))
        results = results[0] # dirty hack to get the results from the list of lists
        batch_size = len(batch)
        results_size = len(results)
        # if results_size != batch_size:
        #     for item in batch:
        #         post_id = item['post_id']
        #         if not any(next(iter(m)) == post_id for m in results):
        #             failed_results.append(item)

        save_results_to_csv(results, OUTPUT_FILE)

        # Replenish the pool with failed texts
        # pool_manager.replenish(failed_results)

if __name__ == "__main__":
    main()
