scores = [143, 456, 890, 533]
average_score = sum(scores)/3    # ==> sum function
print(f"{average_score:.2f}")
print(max(scores))
max_score = 0
for score in scores:
    if score > max_score:  # ==? without using max() fucntion
        max_score = score
print(max_score)