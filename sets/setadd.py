# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
s = set()
for x in range(n):
    s.add(raw_input())
print len(s)