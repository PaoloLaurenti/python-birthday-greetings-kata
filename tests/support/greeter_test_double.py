from birthday_greeter.greeter import Greeter


class GreeterTestDouble(Greeter):
    def __init__(self):
        self.run_calls = 0

    def run(self):
        self.run_calls += 1

    def spied_run_calls(self):
        return self.run_calls
