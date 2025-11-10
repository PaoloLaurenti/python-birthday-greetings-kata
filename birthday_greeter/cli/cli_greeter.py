class CliGreeter:
    def __init__(self, greeter):
        self.greeter = greeter

    def run(self):
        print("Sending birthday greetings...")
        self.greeter.run()
        print("Birthday Greetings sent.")
        return 0
