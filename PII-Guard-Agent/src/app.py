from pathlib import Path
from pii_guard.detector import detect_pii
from pii_guard.redactor import redact_text
from pii_guard.report import generate_markdown_report


def main() -> None:
    sample_path = Path(__file__).resolve().parents[1] / "examples" / "sample_input.txt"
    text = sample_path.read_text(encoding="utf-8")

    findings = detect_pii(text)
    redacted = redact_text(text, findings)
    report = generate_markdown_report(findings)

    print("=== Redacted Text ===")
    print(redacted)
    print()
    print("=== Report ===")
    print(report)


if __name__ == "__main__":
    main()
