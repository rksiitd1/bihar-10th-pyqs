import time
from process_hindi_paper import process_question_paper
import pathlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Thread-safe print
print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def process_single_paper(input_pdf: pathlib.Path, output_json: pathlib.Path) -> dict:
    """Process a single paper and return status."""
    result = {
        "input": input_pdf.name,
        "output": output_json.name,
        "status": "unknown",
        "time": 0,
        "error": None
    }
    
    safe_print(f"🚀 Starting: {input_pdf.name}")
    start = time.time()
    
    try:
        process_question_paper(str(input_pdf), str(output_json))
        result["status"] = "success"
        safe_print(f"✅ Completed: {input_pdf.name}")
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        safe_print(f"❌ Failed: {input_pdf.name} - {e}")
    
    end = time.time()
    result["time"] = end - start
    safe_print(f"⏱️  Time for {input_pdf.name}: {result['time']:.2f}s ({result['time']/60:.2f}min)")
    
    return result

def main():
    # Configuration
    MAX_WORKERS = 4  # Number of parallel requests (adjust based on API limits)
    
    # List of years to process
    years = list(range(2025, 2020, -1))  # 2025 to 2021
    input_folder = pathlib.Path("hindi_papers")
    output_folder = pathlib.Path("hindi_data")
    output_folder.mkdir(exist_ok=True)

    # Collect all papers to process
    papers_to_process = []
    
    for year in years:
        input_pdf = input_folder / f"hindi_{year}.pdf"
        output_json = output_folder / f"hindi_{year}.json"
        
        # Check if input file exists
        if not input_pdf.exists():
            print(f"⚠️  Skipping {input_pdf.name} -> file not found")
            continue
            
        # Check if output file already exists
        if output_json.exists():
            print(f"⏭️  Skipping {input_pdf.name} -> {output_json.name} (already processed)")
            continue
        
        papers_to_process.append((input_pdf, output_json))
    
    if not papers_to_process:
        print("\n✨ All papers already processed!")
        return
    
    print(f"\n{'='*60}")
    print(f"📚 Processing {len(papers_to_process)} papers with {MAX_WORKERS} parallel workers")
    print(f"{'='*60}\n")
    
    total_start = time.time()
    results = []
    
    # Process papers in parallel
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        future_to_paper = {
            executor.submit(process_single_paper, pdf, json): (pdf, json)
            for pdf, json in papers_to_process
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_paper):
            result = future.result()
            results.append(result)
    
    total_end = time.time()
    total_time = total_end - total_start
    
    # Summary
    print(f"\n{'='*60}")
    print(f"📊 SUMMARY")
    print(f"{'='*60}")
    
    successful = [r for r in results if r["status"] == "success"]
    failed = [r for r in results if r["status"] == "error"]
    
    print(f"✅ Successful: {len(successful)}")
    print(f"❌ Failed: {len(failed)}")
    print(f"⏱️  Total time: {total_time:.2f}s ({total_time/60:.2f}min)")
    
    if successful:
        avg_time = sum(r["time"] for r in successful) / len(successful)
        print(f"📈 Average time per paper: {avg_time:.2f}s")
    
    if failed:
        print(f"\n❌ Failed papers:")
        for r in failed:
            print(f"   - {r['input']}: {r['error']}")

if __name__ == "__main__":
    main()
