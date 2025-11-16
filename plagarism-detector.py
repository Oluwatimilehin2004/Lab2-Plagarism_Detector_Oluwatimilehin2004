#!/usr/bin/env python3
"""
plagiarism-detector.py
Follows ALU lab naming & folders:
- Reads essays from essays/essay1.txt and essays/essay2.txt (falls back to essay1.txt/essay2.txt)
- Saves report to reports/similarity_report.txt
"""

import re
import os
from pathlib import Path
from datetime import datetime


# ---- CONFIG ----
STOP_WORDS = {'a', 'an', 'the', 'is', 'in', 'of', 'and', 'to', 'has', 'it', 'this', 'for'}
ESSAYS_DIR = Path("essays")
REPORTS_DIR = Path("reports")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
REPORT_FILENAME = f"similarity_report_{timestamp}.txt"

# ---- UTIL ----
# Loading animation
def loading_ani(message):
    print(message, end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        import time
        time.sleep(0.5)
    

def find_essay_path(basename: str) -> Path:
    """
    Return Path to essay:
    Prefer essays/<basename>, otherwise look for <basename> in current directory.
    """
    p1 = ESSAYS_DIR / basename
    p2 = Path(basename)
    if p1.exists():
        return p1
    if p2.exists():
        return p2
    return None

def text_processor(filepath: Path):
    """
    Read file, lowercase, remove punctuation, split, filter stop words.
    Returns list of meaningful words (may be empty).
    """
    if filepath is None:
        return None  # caller will handle missing file

    try:
        text = filepath.read_text(encoding="utf-8").strip()
    except Exception as e:
        print(f"[Error] Could not read '{filepath}': {e}")
        return None

    if not text:
        # empty file
        return []

    # lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()
    meaningful = [w for w in words if w not in STOP_WORDS]
    return meaningful

#Get the number of times the words was found the essay.
def word_verification(essay):
    ver_word = input("Enter a word to verify: ").strip().lower()
    loading_ani("Verifying word")
    print("")

    if ver_word in STOP_WORDS:
        print(f'"{ver_word}" is a stop word.')
        return ver_word, 0

    word_count = essay.count(ver_word)

    if word_count > 0:
        print(f'"{ver_word}" is present in the essay {word_count} time(s).')
    else:
        print(f'"{ver_word}" is not present in the essay.')

    return ver_word, word_count

def find_common_words(words1, words2):
    return set(words1).intersection(set(words2))

def jaccard_similarity(words1, words2):
    set1 = set(words1)
    set2 = set(words2)
    union = set1.union(set2)
    if not union:
        return 0.0, set()
    inter = set1.intersection(set2)
    similarity_pct = (len(inter) / len(union)) * 100.0
    return similarity_pct, inter

def save_report(similarity_pct, common_words, ver_word, word_count):
    path = REPORTS_DIR / REPORT_FILENAME
    try:
        with path.open("w", encoding="utf-8") as f:
            f.write("Plagiarism Detector - Similarity Report\n")
            f.write("Generated Time:\n")
            f.write(f"Verified word: {ver_word}\n")
            f.write(f"Occurrences: {word_count}\n")
            f.write(f"Similarity: {similarity_pct:.2f}%\n\n")
            f.write(f"Common words ({len(common_words)}):\n")
            for w in sorted(common_words):
                f.write(w + "\n")
        return path
    except Exception as e:
        print(f"[Error] Could not write report to '{path}': {e}")
        return None


def prompt_yes_no(message):
    ans = input(message + " (y/n): ").strip().lower()
    return ans == "y"

# ---- MAIN ----
def main():
    loading_ani("Loading")
    print("\n=== Plagiarism Detector ===")

    # locate essays
    p1 = find_essay_path("essay1.txt")
    p2 = find_essay_path("essay2.txt")

    if p1 is None:
        print("[Error] essay1.txt not found in 'essays/' or current directory.")
    if p2 is None:
        print("[Error] essay2.txt not found in 'essays/' or current directory.")
    if p1 is None or p2 is None:
        print("Please place essay1.txt and essay2.txt in 'essays/' or the project root, then run again.")
        return

    # process texts
    e1_words = text_processor(p1)
    e2_words = text_processor(p2)

    if e1_words is None or e2_words is None:
        print("Error processing files. Exiting.")
        return

    # word verification: find occurrences of a word in essay 1
    ver_word, word_count = word_verification(e1_words)


    if prompt_yes_no("Do you want to proceed with similarity analysis?"):
        print('')
        loading_ani("Analyzing Similarities")
        # common words & similarity
        common = find_common_words(e1_words, e2_words)
        sim_pct, intersection = jaccard_similarity(e1_words, e2_words)

        print(f"\nJaccard Similarity: {sim_pct:.2f}%") 
        if sim_pct >= 50.0:
            print("Decision: Similarity is likely (>= 50%).")
        else:
            print("Decision: Similarity below 50% (< 50%).")

        print(f"\nCommon words: ({len(intersection)}):")
        if common:
            print(", ".join(sorted(list(common))[:50]) + (", ..." if len(common) > 50 else ""))
        else:
            print("(No common meaningful words found)")
    else:
        print("You are not allowed to saved report because no similarites analysis was done, hence nothing save...")
        loading_ani("Exiting")
        exit(0)

    # save report
    if prompt_yes_no("Do you want to save the report to 'reports/similarity_report.txt'?"):
        saved = save_report(sim_pct, common, ver_word, word_count)
        if saved:
            print(f"Report saved to: {saved}")
            print("Thanks for using Plagarism Detector!!!")
            loading_ani("Exiting")
        else:
            print("Failed to save report.")
            loading_ani("Exiting")


if __name__ == "__main__":
    main()

