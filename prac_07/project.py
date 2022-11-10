import datetime


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = datetime.datetime.strftime(start_date, '%d/%m/%y')
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percent_complete}"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.percent_complete == 100
