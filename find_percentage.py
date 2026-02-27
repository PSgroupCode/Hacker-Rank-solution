# problem: given dic count avg two point decimal when giving name
n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mark_list=student_marks[query_name]
    avg=sum(mark_list)/len(mark_list)
    print(f"{avg:.2f}")
