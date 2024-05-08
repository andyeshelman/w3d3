#======= Question 1 =======

def compare_flights(us,them):
    both = us & them
    just_us = us - them
    exclusive = us ^ them
    print(
        "Destinations available from both carriers:", ", ".join(both),
        "Destinations available only from us:", ", ".join(just_us),
        "Destinations exclusive to us or them:", ", ".join(exclusive),
        sep = "\n")
    
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

compare_flights(our_routes, competitor_routes)


#======= Question 2 =======

def strip_dupes(arr):
    # converting to set removes duplicates but loses order
    # order can be recovered by sorting by first appearance in original list
    return sorted(set(arr), key = arr.index)

customer_ids = ["C001", "C002", "C004", "C003", "C002", "C001", "C004"]

print(strip_dupes(customer_ids))