no_of_pages = int(input("Enter the number of pages in the list: "))
capacity = int(input("Enter the number of frames: "))

# Taking pages sequence as input
pages = list(map(int, input("Enter pages sequence: ").split()))

# Initializing an empty list to simulate frames
frames = []
page_faults = 0

for page in pages:
    if page not in frames:
        if len(frames) == capacity:
            # If frames are full, remove the least recently used page (first page in the list)
            frames.pop(0)
        frames.append(page)
        page_faults += 1
    else:
        # If page is already in frames, remove it from its current position and append it at the end
        frames.remove(page)
        frames.append(page)

print(f"PageFault Ratio: {page_faults / no_of_pages}")
print(f"No Of PageFaults: {page_faults}")
print(f"PageHit Ratio: {1 - (page_faults / no_of_pages)}")
