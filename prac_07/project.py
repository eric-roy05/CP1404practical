class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __lt__(self, other):
        """Define comparison based on priority for sorting."""
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"
