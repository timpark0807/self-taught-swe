def cash_flow_30_year(self, income_growth, expense_growth):
        
    year_list = []
    cash_flow_list = []
    annual_income = (self.rent) * 12
    annual_expense = (self.operating_expense() * 12)
    annual_debt_service = self.mortgage_payment() * 12

    for i in range(1, 31):
        annual_income = (annual_income * income_growth)
        annual_vacancy  = (annual_income * self.vacancy)
        annual_gross_income = annual_income - annual_vacancy
        annual_expense = annual_expense * expense_growth
        cash_flow = round(annual_gross_income - annual_expense - annual_debt_service)
        year_list.append(i)
        cash_flow_list.append(cash_flow)
        
    return year_list, cash_flow_list
