import argparse
import time
from src.evaluation.benchmark_runner import run_benchmarks

def main():
    parser = argparse.ArgumentParser(description="Run benchmarks for the document parser app.")
    parser.add_argument('--iterations', type=int, default=10, help='Number of benchmark iterations to run.')
    args = parser.parse_args()

    start_time = time.time()
    results = run_benchmarks(iterations=args.iterations)
    end_time = time.time()

    print(f"Benchmarks completed in {end_time - start_time:.2f} seconds.")
    print("Benchmark Results:")
    for metric, value in results.items():
        print(f"{metric}: {value}")

if __name__ == "__main__":
    main()