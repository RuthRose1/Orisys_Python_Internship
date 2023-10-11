'''
List -> []
Tuple -> ()
Set -> {}
Dictionary -> {key:value}; NO INDEX[remaining has index]
'''
def sum_mark(lst, l):
    Sum = 0
    for i in range(l):
        Sum += lst[i]
    return Sum

def avg_mark(l, s):
    avg = s/l
    print("Average:", avg)
    
def percent(l, s):
    tot = l*100
    p = (s/tot)*100
    print("Percentage:", p, "%")

highest_mark = [23, 45, 62, 99, 88, 69]
max = highest_mark[0]
l = len(highest_mark)
for i in range(1, l):
    if(max < highest_mark[i]):
        max = highest_mark[i]
    else:
        pass
print("Maximum:", max)
Sum = sum_mark(highest_mark, l)
print('Sum:', Sum)
avg_mark(l, Sum)
percent(l, Sum)