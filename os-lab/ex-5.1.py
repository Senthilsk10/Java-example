from queue import Queue

def pageFaults(pages, n, capacity):
    s = set()
    indexes = Queue()
    page_faults = 0
    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
        else:
            if pages[i] not in s:
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
    return page_faults

pages = []
n = int(input("Enter No.Of Pages:"))
pages = list(map(int, input("Enter Pages:").split()))
capacity = int(input("Enter No.Of Frames Available:"))
pagefaults = pageFaults(pages, n, capacity)
print(f"No.Of Pagefaults: {pagefaults}")
print(f"PageFaults ratio: {pagefaults/n}")
PageHit = 1 - (pagefaults/n)
print(f"PageHit ratio: {PageHit}")
