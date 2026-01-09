# Task 1 – Prompt Engineering Evaluation

This task focuses on evaluating different prompt designs for extracting structured sentiment information from customer reviews using a Large Language Model (LLM).

The goal is to compare multiple prompt versions and measure:
- Accuracy of predicted star ratings
- Valid JSON output rate

---

## 📁 Files in This Folder

- `task1_prompt_evaluation.ipynb`  
  Jupyter Notebook that runs prompt experiments and computes metrics.

- `prompt_comparison.csv`  
  Dataset containing:
  - Customer reviews
  - Ground truth star ratings

- `README.md`  
  This file.

---

## 🎯 Objective

Given a customer review, the LLM must return:

```json
{
  "predicted_stars": <1-5>,
  "explanation": "<short explanation>"
}
