super_set = set(map(int, input().split()))
N = int(input())
sets = []
do_need_to_print = True
for i in range(N):
    sets.append(set(map(int, input().split())))
    if sets[-1].difference(super_set) or not super_set.difference(sets[-1]):
        print("False")
        do_need_to_print = False
        break
if do_need_to_print:
    print("True")
