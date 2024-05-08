def optimal(pages, frames, c):
    a = []
    for frame in frames:
        try:
            index = pages.index(frame, c)
            a.append(index)
        except ValueError:
            return frame
    max_index = max(a)
    optimal_index = a.index(max_index)
    return optimal_index

no_of_pages = int(input("Enter the number of pages in the list: "))
capacity = int(input("Enter the number of frames: "))
pages = list(map(int, input("Enter pages sequence: ").split()))

frames = []
page_faults = 0
c = 0

for page in pages:
    if page not in frames:
        if len(frames) == capacity:
            o = optimal(pages, frames, c)
            frames[o] = page
        else:
            frames.append(page)
        page_faults += 1
    else:
        frames.remove(page)
        frames.append(page)
    c += 1

print(f"PageFault Ratio: {page_faults / no_of_pages}")
print(f"No Of PageFaults: {page_faults}")
print(f"PageHit Ratio: {1 - (page_faults / no_of_pages)}")
