# Resume Analyzer  

#### Video Demo: <https://www.youtube.com/watch?v=NPM-ZZjZuog>  

---

## Description  

Resume Analyzer is a Python-based tool that helps job seekers evaluate how well their resume aligns with a specific job description. In today’s competitive job market, it is often not enough to have a well-written resume, but it must also be tailored to the keywords and skills that employers are actively searching for. This project addresses that need by comparing the text of a resume against the text of a job posting, identifying overlaps as well as gaps.  

The program currently works with resumes in PDF format and accepts job descriptions as text pasted directly by the user. It then extracts and cleans both texts, tokenizes them into meaningful words, and performs a keyword-based comparison. The results show the percentage of overlap and the important keywords missing from the resume.  

The project began as a beginner-friendly Python script.



## Features  

Resume Analyzer currently provides the following features:  

**1. Resume Parsing**  
- Extract text from resumes in PDF format using the `PyPDF2` library.  
- Handle multi-page resumes gracefully.  
- Provide error handling in case of invalid or missing files.  

**2. Text Cleaning and Tokenization**  
- Convert all text to lowercase for consistent comparison.  
- Remove punctuation and unnecessary symbols.  
- Tokenize text into words using regular expressions.  
- Remove stopwords (common words like *the*, *and*, *is* and so on).  

**3. Resume–Job Description Comparison**  
- Accept job description text pasted directly by the user (ending with `EOF`).  
- Compare the cleaned tokens from the resume and the job description.  
- Display the match percentage between the two.  
- List keywords that appear in the job description but are missing from the resume.  

## Files in the Project

- `project.py`: The main script containing functions for reading resumes, processing text, and comparing with job descriptions.
- `requirements.txt`: A list of Python libraries required to run this project.
- `README.md`: This documentation file.

## Design Decisions
I chose PyPDF2 for text extraction because it’s lightweight and easy to use for basic PDF parsing. For tokenization, I used regex with optional stopword removal to ensure that irrelevant words do not affect keyword matching. One debate was whether to use NLP libraries like spaCy or NLTK, but for the beginner version, I stuck with regex for simplicity. However, an advanced version could use NLP for more accurate results.


## Requirements  

- Python 3.12+  
- PyPDF2 (for PDF parsing)  
- A terminal or IDE such as VS Code  



## Installation  

The installation steps aside from step 1 and step 2 should be the same in all environments. The following instructions are written for **Ubuntu 24.04**:  

1. Install Python 3.12+ on your machine.  
```bash
sudo apt update
sudo apt install python3
``` 
2. Install pip
```bash
sudo apt install python3-pip
```
3. Create a virtual environment
```bash
python3 -m venv myenv
cd myenv
```
4. Clone this repository
```bash
git clone https://github.com/pratikshyachand/Resume_Analyzer.git
cd Resume_Analyzer
```
5. Activate the virtual environment
```bash
source .../bin/activate
```
>assuming you are inside the Resume_Analyzer directory clone in step 4.
6.Install required module:
```bash
pip install PyPDF2
```

## Start Guide
Run the program from the terminal as follows:
```bash
python3 project.py
```
The program will then:

i. Prompt you to paste the job description text (end input by typing EOF).

ii. Ask you for the path to your resume file (PDF).

iii. Process the text and display:

- The resume–job description match percentage

- The list of missing keywords
