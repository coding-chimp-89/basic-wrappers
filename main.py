from latta import Latta

latta = Latta('6057d68e93993a5a91b44ba43972aba36fb35400b51c91d7e67c3cad4ee11b18ac6533b967a41a3c2c56b771131b41bfcd924d62aa9f7cda24f5a8456c12c2b9')

@latta.wrap
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    print(divide(10, 5))