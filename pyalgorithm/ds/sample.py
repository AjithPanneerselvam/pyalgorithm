import queue

obj = queue.Queue()


def s(h,start =1, ls = []):
    if start <= 2:
        ls.append(1)
        print "Hello World"
        s(5, start+1,ls)

    if start == 1:
        return ls

print s(5)

def se():
    return []

print se()
