def findOptimal(weight, calories, foodItems):
    originCal = calories
    if weight > sum(foodItems):
        return sum(originCal)
    calories = minimize(calories , foodItems)
    res = 0
    arr = findMaxCalorie(calories,foodItems)
    maxC = arr[0]
    foodMax = arr[1]
    calories.remove(maxC)
    foodItems.remove(foodMax)

    while weight > 0:
        if foodMax/weight < 1:
            weight = weight - foodMax
            res += maxC *foodMax
            arr = findMaxCalorie(calories,foodItems)
            maxC = arr[0]
            foodMax = arr[1]
        else:
            res += maxC * weight
            weight = 0
    return res
def findMaxCalorie(calories,foodItems):
        maxC = max(calories)
        maxIndex = calories.index(maxC)
        foodMax = foodItems[maxIndex]
        return maxC,foodMax
def minimize(calories, foodItems):
    for i in range(len(calories)):
        calories[i] = calories[i]/ foodItems[i]
    return calories

print findOptimal(2,[2000,1200,4000],[1 ,2,5])

#1000,2000,600
