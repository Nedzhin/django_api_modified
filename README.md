# Django API Extension Task

## Setup Instructions

This is a Django starter project for your take-home task.

### Setup

1. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```
pip install django djangorestframework
```

3. Run migrations:
After including core it created tables in it
```
python manage.py makemigrations core
python manage.py migrate core
```

4. Start the server:

```
python manage.py runserver
```

5. Visit:

```
http://localhost:8000
```


# Section 1 API Extension

## Approach
- Added an APIView to list `Instruction`s for a given GP Surgery.
- Supports filtering by `instruction_type`, `start_date`, and `end_date`.
- Custom serializer includes nested fields: patient full name, GP name, and instruction type name.

## How to Use
curl http://127.0.0.1:8000/api/surgeries/1/instructions/

## Assumptions
- `Instruction` has foreign keys to `Patient`, `GP`, and `InstructionType`.
- `GP` is linked to `GPSurgery`.

## AI Tools Used
This implementation was assisted by ChatGPT for architecture planning and syntax review.





# Section 2 Answers

## Task 1: Prompt design

My suggested prompt is:

"""
Assume that you are a medical report classification assistant. Your task is to analyze a short snippet of a medical report and classify it into one of the following categories:
- Discharge
- Referral
- Results
- Summary
- Other

Also, include a brief justification for your classification.

Return your answer in the following JSON format:

{
  "classification": "<category>",
  "justification": "<brief explanation for your choice>"
}

Here is the report snippet:
{report_text}
"""

### Example inputs
text1 = "The patient has shown significant improvement and is being discharged with a prescription for antibiotics and follow-up in 7 days."

text2 = "This letter is to refer Mr. John Smith to your clinic for further investigation of recurring chest pain.
"

### Expected outputs
output1
{
  "classification": "Discharge",
  "justification": "The report mentions that the patient is being discharged and includes follow-up instructions, which are typical features of a discharge note."
}

output2
{
  "classification": "Referral",
  "justification": "The report explicitly states it is a referral and includes a request for further investigation by another clinic."
}


### Exlanation of the prompt
- Clear task and constrained classes: Model is given with limited and constrained categories to classify the given medical report.

- Role-based: Giving a role to the model improves its focus and performance.

- Structured output format: By requiring specific JSON structure, we ensure consistency and easier parsing for future work.

## Task 2: Python Function for Sensitive Term Redaction
My Full code:
```
import re

def redact_sensitive_terms(text: str, terms: list[str]) -> str:
    """Replaces case-insensitive matches of each term with '[REDACTED]'."""
    for term in terms:
        # Create a regex pattern that matches the term case-insensitively with word boundaries
        pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
        text = pattern.sub('[REDACTED]', text)
    return text

assert redact_sensitive_terms("The Patient was seen by Dr. Smith and prescribed Ibuprofen.", ["dr. smith", "ibuprofen"]) == \
       "The Patient was seen by [REDACTED] and prescribed [REDACTED]."

```

We import Python’s built-in re module to use regular expressions, which allow us to search for text patterns (like words, ignoring case or punctuation).

### Failing cases
This approach will fail when sensitive terms appear with no space and no word boundaries. For instance, "Dr.Smith" (no space) or "ibuprofen," (with punctuation immediately attached).

### Potential solution to this case
Using a more sophisticated tokenizer or NLP-based entity recognition (maybe with spaCy) to recognize terms regardless of surrounding punctuation or spacing.


## Task 3: Reasoning for AI in Healthcare Systems

1. What are two potential benefits of using AI to redact sensitive medical content?
Answer:
  - Efficiency: AI can automatically go through the thousands of the reports faster then manual review and save a huge time of clinicians.
  - Consistency and scalability: AI ensures consistent redaction of sensitive data, reduce human errors and can scaled to large volumes of the data

2. What are two risks or challenges?
Answer:
  - False negative or missed redaction: AI is not 100% can detect all the sensitive information and this sometime will lead to missed redaction. This will lead to the problem with privacy and data protection
  - False positives or over redaction: Sometimes AI can redact nonsensitive data which can affect to care quality and future processing.

3. What would you do to reduce one of those risks?
Answer:
  - Mitigate Human in validation: combine AI and human manual review on high-risk documents or sampled subsets to ensure quality.