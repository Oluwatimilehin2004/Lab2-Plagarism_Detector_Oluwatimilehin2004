📘 Plagiarism Detector (Python CLI Application)

A lightweight Python-based plagiarism detection tool that analyzes similarity between two essays using Jaccard Similarity, word preprocessing, and an optional word verification feature where users can test the frequency of any word within the essay.

The tool processes text files, removes punctuation, filters out stop words, compares meaningful words, and generates a detailed similarity report saved with an automatic timestamp.

🚀 Features
🔍 1. Text Preprocessing

Converts text to lowercase

Removes punctuation

Splits into individual words

Removes common stop words

Works with any .txt file

📊 2. Similarity Analysis

Uses Jaccard similarity to compute plagiarism likelihood

Identifies common meaningful words

Presents results clearly in the terminal

📝 3. Word Verification

User inputs any word

Program checks if it exists in essay1

Counts number of occurrences

Displays result interactively

📄 4. Report Generation

Automatically saves a timestamped report:

similarity_report_2025-02-16_03-41-22.txt


Includes:

Verified word & count

Similarity percentage

List of common words

Execution time

📁 5. Organized Directory Structure
project/
│── essays/
│     ├── essay1.txt
│     └── essay2.txt
│
│── reports/
│     └── similarity_report_<timestamp>.txt
│
│── plagiarism-detector.py
│── README.md

⚙️ Installation & Requirements
1. Clone the Repository
git clone https://github.com/yourusername/plagiarism-detector.git
cd plagiarism-detector

2. Python Version

This project requires Python 3.8 or higher.

3. Install Dependencies

This project uses only built-in Python modules:

os

pathlib

re

datetime

No extra installation is required.

▶️ How to Use the Program
1. Place your essays

Add two files inside the essays/ folder:

essay1.txt
essay2.txt

2. Run the Program
python plagiarism-detector.py

3. Word Verification

The program will ask:

Enter a word to verify:


It then checks:

If the word is a stop word

If it appears in the essay

How many times it appears

4. Similarity Analysis

The tool asks:

Do you want to proceed with similarity analysis? (y/n)


If yes:

Calculates Jaccard similarity

Shows common meaningful words

Gives a similarity decision

5. Save Report

Once analysis is done:

Do you want to save the report? (y/n)


If yes:
A file will be created in the reports/ folder with a timestamped name.

📄 Sample Output
=== Plagiarism Detector ===
Loading...

Enter a word to verify: education
Verifying word...
"education" is present in the essay 3 time(s).

Analyzing Similarities...
Jaccard Similarity: 57.14%
Decision: Similarity is likely (>= 50%).

Common words (12):
education, system, learning, student, ...

Report saved to: reports/similarity_report_2025-02-16_03-41-22.txt

🛠️ How It Works Internally
1. Text Processing

Removes punctuation using regex

Converts to lowercase

Splits into words

Removes stop words defined in STOP_WORDS

2. Similarity Calculation

Uses the classic formula:

Similarity = (Intersection of words) / (Union of words) × 100

3. Word Verification

Performs:

count = essay_words.count(input_word)

4. Timestamped Reports

Created using:

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
REPORT_FILENAME = f"similarity_report_{timestamp}.txt"

📌 Future Improvements (Optional)

You may want to add:

PDF or HTML report output

Support for multiple essays

Sentence-level similarity

Cosine similarity with TF-IDF

Web-based frontend (Flask/Django)

AI-based semantic similarity

👨‍💻 Author

Ayomide Ojudun
Python Developer | ALU Student | Tech Enthusiast
