import time
import pathlib
import re
from process_hindi_paper import process_question_paper
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Thread-safe print
print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def get_year_from_filename(filename):
    """Extracts year from filename like 'hin_2016i.pdf' or 'low_hin_2017ii.pdf'."""
    match = re.search(r'20\d{2}', filename)
    if match:
        return int(match.group(0))
    return 0

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
    MAX_WORKERS = 4
    
    input_folder = pathlib.Path("hindi_papers")
    output_folder = pathlib.Path("hindi_data")
    output_folder.mkdir(exist_ok=True)

    # Collect all papers to process
    papers_to_process = []
    
    all_pdfs = list(input_folder.glob("*.pdf"))
    
    print(f"\nScanning {len(all_pdfs)} files in {input_folder}...")
    
    for input_pdf in all_pdfs:
        filename = input_pdf.name
        
        # 1. Filter by Prefix
        if filename.startswith("sil_") or filename.startswith("noise_"):
            print(f"🚫 Skipping (Noise/Sil): {filename}")
            continue
            
        # 2. Filter by Year
        year = get_year_from_filename(filename)
        if year < 2016:
            print(f"🚫 Skipping (Year < 2016): {filename} (Year: {year})")
            continue
            
        # 3. Check output existence
        output_json = output_folder / f"{input_pdf.stem}.json"
        
        if output_json.exists():
             print(f"⏭️  Skipping (Already Processed): {filename}")
             continue

        # If it passes all filters (including low_ and normal files >= 2016)
        print(f"➕ Adding to queue: {filename}")
        papers_to_process.append((input_pdf, output_json))
    
    if not papers_to_process:
        print("\n✨ All matching papers already processed or no valid papers found!")
        return
    
    print(f"\n{'='*60}")
    print(f"📚 Processing {len(papers_to_process)} TARGETED Hindi papers with {MAX_WORKERS} workers")
    print(f"{'='*60}\n")
    
    total_start = time.time()
    results = []
    
    # Process papers in parallel
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_paper = {
            executor.submit(process_single_paper, pdf, json): (pdf, json)
            for pdf, json in papers_to_process
        }
        
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
    
    if failed:
        print(f"\n❌ Failed papers:")
        for r in failed:
            print(f"   - {r['input']}: {r['error']}")

if __name__ == "__main__":
    main()
