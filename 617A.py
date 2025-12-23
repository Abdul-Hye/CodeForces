x = int(input())
 
# Step 1
steps_of_5 = x // 5
 
# Step 2
remaining_distance = x % 5
 
# Step 3
if remaining_distance == 0:
    print(steps_of_5)
else:
    # Step 4
    steps_of_5 += 1 
    print(steps_of_5)