import hashlib
import hmac
import secrets

from config.settings import settings


def generate_otp() -> str:
    return f"{secrets.randbelow(1_000_000):06d}"


def hash_otp(otp: str) -> str:
    return hmac.new(
        settings.otp_hmac_secret.encode(),
        otp.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_otp(otp: str, stored_hash: str) -> bool:
    calculated_hash = hash_otp(otp)

    return hmac.compare_digest(
        calculated_hash,
        stored_hash
    )