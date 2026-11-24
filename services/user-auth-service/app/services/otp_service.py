from app.utils.otp import generate_otp, hash_otp, verify_otp


def create_otp():
    otp = generate_otp()
    code_hash = hash_otp(otp)

    return otp, code_hash


def check_otp(otp: str, code_hash: str) -> bool:
    return verify_otp(otp, code_hash)