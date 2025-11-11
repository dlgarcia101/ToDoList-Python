

#todo list in python
entryOptions= ['A','D','L']
toDoList = ['take out the trash']

#function to add and validate userInput into the List
def taskUserFunction(taskType,userTaskInput):
    while True:
        userTaskType = input(taskType).strip().upper()
        
        if(userTaskType in entryOptions):
            if(userTaskType == 'A'):
                userInput = input(userTaskInput).strip().lower()
                if(userInput in toDoList):
                    print('task already in To-Do-List')
                elif(userInput != ''):
                    toDoList.append(userInput)
            elif(userTaskType == 'D'):
                userInput = input(userTaskInput).strip().lower()
                if(userInput != '' and userInput in toDoList):
                    toDoList.remove(userInput)
                    print(userInput.upper()  + ' has been deleted from list')
                else: print('Task not in To-Do-List')
            elif(userTaskType == 'L'):
                    print(toDoList)
        else: print("Enter valid task type:(A: Add, D: Delete , L: See List)")




userTaskEntry = taskUserFunction('Type of task: ','Please enter task:')

















#text pattens practice below 
def isPhoneNumber(numb):
    if len(numb) !=12:
        return False
    for i in range(0,3):
        if not numb[i].isdecimal():
            return False
    if numb[3] != '-':
        return False    
    for i in range(4,7):
         if not numb[i].isdecimal():
            return False
    if numb[7] != '-':
        return False
    for i in range(8,12):
        if not numb[i].isdecimal():
            return False
    
    return True

print(isPhoneNumber('813-997-9099'))
print(isPhoneNumber('120043-1'))


