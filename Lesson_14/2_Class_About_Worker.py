class Worker:

    def __init__(self, name, age, experience, position):
        self.name = name
        self.age = age
        self.experience = experience
        self.position = position
        self.base_salary = 1000
        self.yearly_rise = 200
        self.past_jobs = {}

    def get_wages(self):
        salary = self.base_salary + int(self.experience) * self.yearly_rise
        print(f"{self.name} has a salary of {salary}$.")

    def promotion(self, new_position):
        self.position = new_position

    def add_past_jobs(self, company_name, job_description):
        self.past_jobs[company_name] = job_description

    def info_card(self):
        print(f"Name:{self.name}\nAge: {self.age}\nExperience: {self.experience}\nPosition:{self.position}")
        print("Previous jobs:")
        for item in self.past_jobs:
            print(f"{item}: {self.past_jobs[item]}")


tim = Worker("Tim Allen", 27, 0.5, "Trainee")
tim.get_wages()
tim.promotion("Junior")
tim.add_past_jobs("Microsoft", "Worked as an accountant")
tim.add_past_jobs("General Motors", "Worked as a controls engineer")
tim.info_card()
