def merge_sorted_lists(A, B):
    if A:
        a = A.pop(0)
    if B:
        b = B.pop(0)
    C = []
    while A and B:
        print("a: " + str(a))
        print("b: " + str(b))
        if a <= b:
            C.append(a)
            a = A.pop(0)
        if b <= a:
            C.append(b)
            b = B.pop(0)
    if A:
        C.extend(A)
    if B:
        C.extend(B)
    return C

def test_merge_sorted_list():
    A = [1,2,4,8,16,99,100000]
    B = [-10, 3, 8, 99, 100, 200, 200, 200, 200, 200]
    print(merge_sorted_lists(A, B))
    assert(merge_sorted_lists(A, B) == sorted(A + B))
    print('passed test')

test_merge_sorted_list()
