# Plagiarism Detector (Python CLI Application)

A Python-based plagiarism detection tool that compares two essays using **Jaccard Similarity**, filters stop words, performs word verification, and generates a timestamped similarity report.

## Features

### Text Preprocessing
- Lowercases text  
- Removes punctuation  
- Splits into words  
- Removes stop words  
- Works with any `.txt` file  

### Similarity Analysis
- Calculates Jaccard similarity  
- Finds common meaningful words  
- Gives a clear similarity decision  

### Word Verification
- User inputs a word  
- Tool checks if word exists in essay  
- Counts occurrences  
- Shows results interactively  

### Report Generation
- Automatically saves with a timestamp:
- similarity_report_2025-02-16_03-41-22.txt
- - Includes:
- similarity percentage  
- verified word + count  
- list of common words  

### Directory Structure
project/
│── essays/
│ ├── essay1.txt
│ └── essay2.txt
│
│── reports/
│ └── similarity_report_<timestamp>.txt
│
│── plagiarism-detector.py
│── README.md


## Installation & Requirements

### Clone Repository
git clone https://github.com/Oluwatimilehin2004/plagiarism-detector.git
cd plagiarism-detector

# Plagiarism Detector (Python CLI Application)

A Python-based plagiarism detection tool that compares two essays using **Jaccard Similarity**, filters stop words, performs word verification, and generates a timestamped similarity report.

## ⚙️ Python Version

Requires **Python 3.8+**

### Dependencies

All modules are built-in:

- `os`
- `re`
- `pathlib`
- `datetime`

No extra installation required.

## How to Use

```bash
### 1. Add Essays
Place two files inside the `essays/` folder:
essay1.txt
essay2.txt

### 2. Run Program
python plagiarism-detector.py

3. Word Verification
Enter any word when prompted:
Enter a word to verify:

4. Similarity Analysis
When asked:
Do you want to proceed with similarity analysis? (y/n)
Choose yes to see:
Similarity percentage
Common words
Decision threshold

5. Save Report
Do you want to save the report? (y/n)
A timestamped report will be created in the reports/ folder.
```

### Sample Output
```bash
=== Plagiarism Detector ===

Enter a word to verify: education
"education" is present in the essay 3 time(s).

Analyzing Similarities...
Jaccard Similarity: 57.14%
Decision: Similarity is likely (>= 50%).

Common words (12):
education, system, learning, student, ...

Report saved to: reports/similarity_report_2025-02-16_03-41-22.txt
```

### Author
_Ayomide Ojudun_
_Python Developer | ALU Student | Tech Enthusiast_


