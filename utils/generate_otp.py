import secrets

def generate_otp(length=6):
    """
    Generate a secure OTP (One-Time Password) of specified length.
    
    Args:
        length (int): The length of the OTP to generate. Default is 6.

    Returns:
        str: A string representation of the OTP.
    """
    otp = ''.join([str(secrets.randbelow(10)) for _ in range(length)])
    return otp
