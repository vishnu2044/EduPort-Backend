import secrets

def generate_otp(length=6):
    """
    Generate a secure OTP (One-Time Password) of 6 digit length.
    """
    otp = ''.join([str(secrets.randbelow(10)) for _ in range(length)])
    return otp
