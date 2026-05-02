from pii_guard.detector import detect_pii
from pii_guard.redactor import redact_text


def test_detect_email_phone_student_id():
    text = "Email alex@example.com, phone +60 12-345 6789, ID TP078888."
    findings = detect_pii(text)
    labels = [item.label for item in findings]

    assert "EMAIL" in labels
    assert "PHONE" in labels
    assert "STUDENT_ID" in labels


def test_redaction():
    text = "Contact alex@example.com"
    findings = detect_pii(text)
    redacted = redact_text(text, findings)

    assert "alex@example.com" not in redacted
    assert "[EMAIL]" in redacted
