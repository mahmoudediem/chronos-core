# core uses the v3 API
from shareddep import new_func

def core_run():
    return f"core -> {new_func()}"

if __name__ == "__main__":
    print(core_run())