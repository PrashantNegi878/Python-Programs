stack=[]

def push():
    element=input("Enter the element = ")
    stack.append(element)
    print(stack)

def pop_element():
    if len(stack)==0:
        print("Stack is empty")
    else:
        stack.pop()
    print(stack)

while True:
    choice=int(input("Enter your choice :"
          "1.Push 2.Pop 3.Quit  "))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct choice")
