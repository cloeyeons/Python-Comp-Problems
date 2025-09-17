quarters = int(input())
first_machine = int(input())
second_machine = int(input())
third_machine = int(input())    
plays = 0   

while quarters > 0:
    quarters = quarters - 1
    if plays % 3 == 0:
        first_machine = first_machine + 1
        if first_machine % 35 ==0:
            quarters = quarters + 30
            first_machine = 0   
    elif plays % 3 == 1:
        second_machine = second_machine + 1 
        if second_machine % 100 == 0:
            quarters = quarters + 60
            second_machine = 0  
    elif plays % 3 == 2: 
        third_machine = third_machine + 1       
        if third_machine % 10 == 0:
            quarters = quarters + 9
            third_machine = 0   
    plays = plays + 1

print ("Martha plays", plays, "times before going broke.")