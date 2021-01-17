age = 25
retirement = 60
income = 90000

def budgetData():
    incomePoints = []
    for x in range(age, retirement):
        incomePoints.insert(x-age, (x-age)*income)

    return incomePoints

def budgetLabels():
    labels = []
    for x in range(age, retirement):
        labels.insert(x-age, x)
    
    return labels

