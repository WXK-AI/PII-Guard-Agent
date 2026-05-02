from typing import List
from .detector import Finding


def redact_text(text: str, findings: List[Finding]) -> str:
    """Replace PII spans with label tags."""
    output = []
    last_index = 0

    for finding in sorted(findings, key=lambda item: item.start):
        output.append(text[last_index:finding.start])
        output.append(f"[{finding.label}]")
        last_index = finding.end

    output.append(text[last_index:])
    return "".join(output)
