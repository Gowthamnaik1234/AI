class VacuumCleaner:
    def __init__(self):
        self.location = 0  # Initial location of the vacuum cleaner (0: A, 1: B)
        self.environment = [0, 0]  # Environment state (0: Clean, 1: Dirty)
        self.actions = []  # List to store the actions taken

    def sense(self):
        return self.environment[self.location]

    def clean(self):
        self.environment[self.location] = 0
        self.actions.append(f"Cleaned {chr(65 + self.location)}")

    def move(self, location):
        self.location = location
        self.actions.append(f"Moved to {chr(65 + self.location)}")

    def act(self):
        if self.sense() == 1:
            self.clean()
        else:
            self.move(1 - self.location)

    def run(self):
        while 1 in self.environment:
            self.act()
        print("Actions:")
        for action in self.actions:
            print(action)


if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.environment = [1, 0]  # Set the initial environment (e.g., A is dirty, B is clean)
    print("Initial Environment:")
    print(f"Location: {chr(65 + vacuum.location)}")
    print(f"State: {'Dirty' if vacuum.sense() == 1 else 'Clean'}")

    vacuum.run()
