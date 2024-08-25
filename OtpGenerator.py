import random
import string

def gen_otp(length=6):
    chtr = string.digits
    otp = ''.join(random.choice(chtr) for _ in range(length))
    return otp

otp = gen_otp()
print(f"Your OTP is: {otp}")