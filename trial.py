from error_handling import trial_decorator

@trial_decorator
def trial(*args, **kwargs):
    name = args[0]
    print(name)

if __name__ == "__main__":
    trial()
