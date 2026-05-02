# Evaluation Plan

## Dataset design

Create a safe evaluation dataset with synthetic examples:

- Realistic emails, phone numbers, student IDs, addresses, and names.
- Negative examples that look similar but are not PII.
- Mixed-language examples, including English, Chinese, and Malay.
- Logs and JSON records.
- Long documents with repeated entities.

## Evaluation labels

Each sample should include:

```json
{
  "text": "Contact me at alex@example.com",
  "entities": [
    {
      "label": "EMAIL",
      "value": "alex@example.com",
      "start": 14,
      "end": 30,
      "risk": "medium"
    }
  ]
}
```

## Metrics

- Precision
- Recall
- F1 score
- False positive rate
- False negative rate
- Redaction correctness
- Report usefulness

## Manual review protocol

1. Run the detector on test samples.
2. Compare detected spans with ground truth labels.
3. Review false positives and false negatives.
4. Update rules/prompts.
5. Re-run regression tests.
