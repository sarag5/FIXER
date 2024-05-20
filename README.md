# FIXER
AI-powered chatbot designed to provide helpful and accurate answers to code analysis and scan analysis.


<img width="667" alt="Screenshot 2024-05-20 at 5 09 21 PM" src="https://github.com/sarag5/FIXER/assets/94899972/ff688224-e457-48e1-8d99-2cc3a52d58a6">

## Introduction

Fixer utilizes the powerful language model Meta-LLama2 through the "LlamaCpp" library. This allows it to respond to your questions in a coherent and relevant manner. Please make sure to keep your queries in English and adhere to the provided guidelines to get the best results from Fixer.


## Features
- **Local AI:** Use llama which ever version you like
- ** Code Analysis:** It thoroughly examines the source code without executing it, identifying potential vulnerabilities, coding errors, and security issues.
- **Vulnerability Analysis:** Performs a comprehensive vulnerability analysis using the provided scan code or log file. It identifies and assesses security weaknesses, misconfigurations, and potential exploits present in the target system or network.
- CWE_analysis : Find if there is any CWE in the code

## How it looks
### Using Llama


The prompt for the model usage looks like this:
```prompt
f"[INST] <<SYS>> {instructions}<</SYS>> Data to be analyzed: {data} [/INST]"
```
The instructions looks like this:
```prompt
You are a security researcher, expert in detecting security vulnerabilities. Provide response only in following format: vulnerability: < YES or NO> I vulnerability type: <CWE ID> | vulnerability name: <CWE NAME> | explanation: <explanation for prediction›. Use N/A in other fields if there are no vulnerabilities. Do not include anything else in response.
```

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/sarag5/FIXER.git
cd FIXER
```

### Step 2: Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 3: Download the AI Model

```bash
python3 fixer.py
```

The first time you run FIXER, it will check for the AI model required for the chatbot.

## Chat:

### Test code

```python
user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
execute_query(query)  # This can be exploited
```

### CWE Check

<img width="993" alt="Screenshot 2024-05-20 at 4 49 49 PM" src="https://github.com/sarag5/FIXER/assets/94899972/9eec98f8-b66b-430f-b8e1-7ddb858b11ea">

### Vulnerability Analysis

<img width="993" alt="Screenshot 2024-05-20 at 4 51 48 PM" src="https://github.com/sarag5/FIXER/assets/94899972/79de7134-0b79-49ca-883c-d19cb18b7dfb">

### Code Analysis

<img width="993" alt="Screenshot 2024-05-20 at 4 54 24 PM" src="https://github.com/sarag5/FIXER/assets/94899972/56d300d5-c1df-4a24-a294-5f7949c6f7b1">


## Contact

For any questions, feedback, or inquiries related to FIXER, feel free to contact:

- Email: mail2sabarinathan@yahoo.com
- LinkedIn: [sabarinathan raghupathi](https://www.linkedin.com/in/sabarinathan-raghupathi/)
