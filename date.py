class Date :
    
    #Init Date == 1582년.10월.15일 금요일 -> 그레고리력 시작일
    
    totalDate = 0
    
    date = 0
    month = 0
    year = 0
    
    def __init__(self) -> None:
        pass
    
    def CalculateDate(self):
        #Calcdate With total date
        pass 
    
    def CalculateTotalDate(self):
        #Calculate totalDate with date
        pass
    
    def SetDate(self, totalDate):
        self.totalDate = totalDate
        self.CalculateDate()
        
    def SetDate(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year
        