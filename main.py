import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from latta import Latta
LATTE_API_KEY = os.getenv("LATTE_API_KEY", None)

if LATTE_API_KEY is None:
    raise Exception("LATTE_API_KEY env. variable is not defined")

latta = Latta(LATTE_API_KEY)

@latta.wrap
def divide(x, y):
    return x / y

if __name__ == "__main__":
    print(divide(10, 5))