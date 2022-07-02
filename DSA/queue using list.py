queue=[]

def enqueue():
    element = int(input("Enter any element"))
    queue.append(element)
    print(element,"added to queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e= queue.pop(0)
        print("Element popped = ",e)

def display():
    print(queue)

while True:
    print("Enter your choice "
          "1.Add 2.Remove 3.Display 4.Quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Choice")
