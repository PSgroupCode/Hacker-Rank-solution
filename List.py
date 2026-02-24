if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        command= input().split()
        action=command[0]
        if action=="insert":
            list1.insert(int(command[1]),int(command[2]))
        elif action=="print":
            print(list1)
        elif action =="remove":
            list1.remove(int(command[1]))
        elif action=="append":
            list1.append(int(command[1]))
        elif action=="sort":
            list1.sort()
        elif action=="pop":
            list1.pop()
        elif action=="reverse":
            list1.reverse()
            
