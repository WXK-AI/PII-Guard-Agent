# PII-Guard-Agent

A practical AI-agent project for **PII detection, anonymization, and compliance review** in student documents, logs, and application data.

This package is designed as a high-quality project proposal/submission kit for an AI token-plan application form. It contains:

- A ready-to-paste Chinese form answer under `submission/form_answer_chinese.md`
- A longer project description under `submission/project_details.md`
- Architecture and workflow diagrams under `docs/architecture.md`
- A milestone/token usage plan under `docs/token_usage_plan.md`
- A small prototype skeleton under `src/`
- A demo input and expected output under `examples/`

> Important: Replace all placeholders marked `TODO` with your real project details before submitting. Do not claim production deployment, team size, or metrics unless they are true.

## Core idea

Build an AI-powered agent that reviews text or CSV/JSON records, detects personally identifiable information, explains the risk, redacts the content, and generates a safe audit report.

## Main use cases

1. Student assignment / report privacy cleanup before sharing.
2. Dataset preparation for PII model training.
3. Web/app log sanitization before sending logs to external tools.
4. Compliance review assistant for small teams.

## Selected tools/models for the form

Suggested options based on your screenshot:

- Agent tools: `Claude Code`, `Codex`, `Hermes Agent`
- Model series: `Claude`, `Gemini`, `GPT`, `MiMo`, `MiniMax`

## How to use this package

1. Open `submission/form_answer_chinese.md`.
2. Replace the placeholders:
   - `TODO: your current progress`
   - `TODO: real metrics if any`
   - `TODO: your expected daily/monthly token need`
3. Paste the final Chinese answer into the application form.
4. Keep `docs/token_usage_plan.md` for backup if reviewers ask for more detail.

## Prototype structure

```text
src/
  pii_guard/
    detector.py       # Regex + LLM-review placeholder interface
    redactor.py       # Redaction utilities
    report.py         # Report generation
  app.py              # CLI demo
examples/
  sample_input.txt
  expected_output.md
```

## Ethics and privacy

The project is intended to **remove or protect sensitive personal data**, not to collect, expose, or exploit it.
