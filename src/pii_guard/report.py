from typing import List
from .detector import Finding


def generate_markdown_report(findings: List[Finding]) -> str:
    """Generate a simple Markdown audit report."""
    lines = ["# PII Audit Report", "", f"Total findings: {len(findings)}", ""]
    lines.append("| Label | Risk | Start | End | Value |")
    lines.append("|---|---|---:|---:|---|")

    for item in findings:
        safe_value = item.value.replace("|", "\\|")
        lines.append(
            f"| {item.label} | {item.risk} | {item.start} | {item.end} | `{safe_value}` |"
        )

    return "\n".join(lines)
