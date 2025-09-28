import PyPDF2
import re

STOPWORDS = {
    "the","a","an","and","or","in","on","for","to","of","with","is","are","that",
    "this","as","by","from","be","it","at","have","has","will","can","we","you"
}

#reads job description from user pasted text
def read_job_description(prompt="Paste the job description and write EOF on a new line when done:"):
    print(prompt)
    lines = []
    while True:
     try:
         line = input()
     except EOFError:
       break
     if line.strip() == "EOF":
         break
     lines.append(line)
    return "\n".join(lines)

#reads resume pdf document provided by the user
def read_resume():
    path = input("Provide path to your resume file: ").strip()
    texts = []
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
     try:
        text = page.extract_text()
     except Exception:
        text = None
     if text:
         texts.append(text)
    return "\n".join(texts)

# cleans the text by lowering cases and removing stopwords defined in the above set 
def clean(text, stopword = True):
    lowered_text = text.lower()
    tokens = re.findall(r"\b[a-z0-9]+\b",lowered_text)
    if stopword:
        tokens = [token for token in tokens if token not in STOPWORDS]
    return tokens

#this section calls clean() along with performing comparision between resume and
#job description and finally returns result
def compare(job_text, resume_text):
    job_token = clean(job_text, stopword = True)
    resume_token = clean(resume_text, stopword = True)

    job_set = set(job_token)
    resume_set = set(resume_token)

    match = job_set.intersection(resume_set)
    missing = job_set.difference(resume_set)

    score = 0.0
    if len(job_set)>0:
        score = round(len(match) / len(job_set) * 100, 2)

    result = {
        "score": score,
        "missing": missing
    }
    return result


def main():
          job_text = read_job_description()
          try:
           resume_text = read_resume()
          except Exception:
              print("File not found")
              exit() 

          result = compare(job_text, resume_text)

          print("----------------")
          print("RESULT ANALYZER")
          print("----------------")
          print(f"Match Score: {result['score']}%")
          print(f"Missing Keywords:")
          print(",".join(result['missing']) or "None")



if __name__ == "__main__":
    main()