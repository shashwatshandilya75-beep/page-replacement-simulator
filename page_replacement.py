def _fmt(frames):
    return [p for p in frames]

def fifo(reference, num_frames):
    frames = [None]*num_frames
    ptr = 0                      # next slot to replace (oldest page)
    faults = hits = 0
    trace = []
    for step, page in enumerate(reference, 1):
        replaced = None
        if page in frames:
            hits += 1; status = "Hit"
        else:
            faults += 1; status = "Fault"
            if None in frames:
                frames[frames.index(None)] = page
            else:
                replaced = frames[ptr]
                frames[ptr] = page
                ptr = (ptr + 1) % num_frames
        trace.append((step, page, list(frames), status, replaced))
    return faults, hits, trace

def lru(reference, num_frames):
    frames = [None]*num_frames
    last_used = {}               # page -> last time it was referenced
    faults = hits = 0
    trace = []
    for step, page in enumerate(reference, 1):
        replaced = None
        if page in frames:
            hits += 1; status = "Hit"
        else:
            faults += 1; status = "Fault"
            if None in frames:
                frames[frames.index(None)] = page
            else:
                victim = min(frames, key=lambda p: last_used[p])
                replaced = victim
                frames[frames.index(victim)] = page
        last_used[page] = step
        trace.append((step, page, list(frames), status, replaced))
    return faults, hits, trace

def optimal(reference, num_frames):
    frames = [None]*num_frames
    faults = hits = 0
    trace = []
    n = len(reference)
    for i, page in enumerate(reference):
        step = i + 1
        replaced = None
        if page in frames:
            hits += 1; status = "Hit"
        else:
            faults += 1; status = "Fault"
            if None in frames:
                frames[frames.index(None)] = page
            else:
                best_slot, best_dist = 0, -1
                for slot, p in enumerate(frames):        # slots scanned in order -> ties pick first
                    if p in reference[i+1:]:
                        dist = reference[i+1:].index(p)
                    else:
                        dist = n + 1                      # never used again
                    if dist > best_dist:
                        best_slot, best_dist = slot, dist
                replaced = frames[best_slot]
                frames[best_slot] = page
        trace.append((step, page, list(frames), status, replaced))
    return faults, hits, trace

def read_input():
    """Read reference string and frame count from the user; reject invalid input."""
    raw = input("Enter page reference string (comma or space separated): ").strip()
    tokens = raw.replace(",", " ").split()
    if not tokens:
        raise ValueError("Reference string is empty.")
    reference = []
    for t in tokens:
        if not t.lstrip("-").isdigit():
            raise ValueError(f"Invalid page '{t}': pages must be integers.")
        if int(t) < 0:
            raise ValueError(f"Invalid page '{t}': pages cannot be negative.")
        reference.append(int(t))

    f = input("Enter number of frames: ").strip()
    if not f.lstrip("-").isdigit():
        raise ValueError(f"Invalid frame count '{f}': must be an integer.")
    num_frames = int(f)
    if num_frames < 1:
        raise ValueError("Number of frames must be at least 1.")
    return reference, num_frames
def print_trace(name, reference, num_frames, result):
    faults, hits, trace = result
    total = len(reference)
    print(f"\n{'=' * 64}\n{name}  (frames = {num_frames})\n{'=' * 64}")
    header = f"{'Step':<6}{'Page':<6}" + "".join(f"{'F' + str(i+1):<5}" for i in range(num_frames)) + f"{'Result':<8}{'Replaced':<9}"
    print(header)
    print("-" * len(header))
    for step, page, frames, status, replaced in trace:
        cells_ = "".join(f"{('-' if p is None else p)!s:<5}" for p in frames)
        rep = "-" if replaced is None else replaced
        print(f"{step:<6}{page:<6}{cells_}{status:<8}{rep!s:<9}")
    print(f"\nTotal Faults: {faults} | Total Hits: {hits} | "
          f"Hit Ratio: {hits/total*100:.2f}% | Fault Ratio: {faults/total*100:.2f}%")

def print_comparison(reference, results):
    total = len(reference)
    print(f"\n{'=' * 64}\nCOMPARISON\n{'=' * 64}")
    print(f"{'Algorithm':<12}{'Faults':<9}{'Hits':<7}{'Hit Ratio':<12}{'Fault Ratio':<12}")
    print("-" * 52)
    for name, (faults, hits, _) in results.items():
        print(f"{name:<12}{faults:<9}{hits:<7}{hits/total*100:>6.2f}%     {faults/total*100:>6.2f}%")
try:
    reference, num_frames = read_input()
    results = {
        "FIFO": fifo(reference, num_frames),
        "LRU": lru(reference, num_frames),
        "Optimal": optimal(reference, num_frames),
    }
    for name, res in results.items():
        print_trace(name, reference, num_frames, res)
    print_comparison(reference, results)
except ValueError as e:
    print("Error:", e)