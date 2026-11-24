from config.settings import settings


def normalize_email(email: str) -> str:
    return email.strip().lower()


def is_company_email(email: str) -> bool:
    return email.endswith(
        f"@{settings.company_email_domain}"
    )