# problem: second lowest scores vale students ke name print karna
students=[]
    for _ in range(int(input())):
       
        name = input()
        score = float(input())
        students.append([name,score])
scores=sorted(list(set([row[1] for row in students])))
second_lowest=scores[1]
result_names=sorted([x[0] for x in students if x[1]==second_lowest])
for i in result_names:
    
    print(i)
