class Company:
    def __init__(self, name, industry_sector, ceo, headquarters, number_of_employees, yearly_income):
        self.name = name
        self.industry_sector = industry_sector
        self.ceo = ceo
        self.headquarters = headquarters
        self.number_of_employees = number_of_employees
        self.yearly_income = yearly_income

    def change_ceo(self, new_ceo):
        self.ceo = new_ceo

    def hire_employees(self, new_employees):
        self.number_of_employees += new_employees

    def is_profitable(self, expanses):
        if self.yearly_income > expanses:
            print(f"{self.name} is a profitable company, profit is {self.yearly_income - expanses}$.")
        else:
            print(f"{self.name} is not a profitable company.")

    def company_info_card(self):
        print(f"""INFO CARD
    Company name: {self.name}
    Industry sector: {self.industry_sector}
    Headquarters: {self.headquarters}
    Number of employees: {self.number_of_employees}
    Yearly income: {self.yearly_income}$
    CEO of the company:{self.ceo}""")


apple = Company("Apple", "Technology", "Tim Cook", "Cupertino", 164000, 383_000)
apple.company_info_card()
apple.change_ceo("Ronald McDonald")
apple.hire_employees(100)
apple.company_info_card()
apple.is_profitable(380_000)
