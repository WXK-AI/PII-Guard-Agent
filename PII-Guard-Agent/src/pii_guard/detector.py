import re
from dataclasses import dataclass
from typing import List


@dataclass
class Finding:
    label: str
    value: str
    start: int
    end: int
    risk: str


PATTERNS = {
    "EMAIL": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "PHONE": re.compile(r"(?:\+?60|0)?\s?1[0-9][-\s]?\d{3}[-\s]?\d{4}"),
    "STUDENT_ID": re.compile(r"\b(?:TP|tp)\d{6}\b"),
}


RISK_BY_LABEL = {
    "EMAIL": "medium",
    "PHONE": "high",
    "STUDENT_ID": "medium",
}


def detect_pii(text: str) -> List[Finding]:
    """Detect common PII using deterministic patterns.

    This is a prototype layer. A production version should add:
    - multilingual name/address detection
    - LLM context review
    - better country-specific ID validation
    - test coverage for edge cases
    """
    findings: List[Finding] = []
    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    label=label,
                    value=match.group(0),
                    start=match.start(),
                    end=match.end(),
                    risk=RISK_BY_LABEL.get(label, "low"),
                )
            )
    return sorted(findings, key=lambda item: item.start)
