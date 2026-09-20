def tower_of_hanoi(n, source, helper, destination,count):

    if n == 1:
        print(f"Move disk 1 from {source} -> {destination}")
        return

    
    # move from source to destination with the help of helper but here destination is helper to move disk to helper our end tower  
    count+=1
    tower_of_hanoi(n - 1, source, destination, helper,count)

    # Move largest disk from source to destination
    print(f"Move disk {n} from {source} -> {destination}")

    # move from source to destination but here our source will be helper and helper will be source to move to destination 
    count+=1
    tower_of_hanoi(n - 1, helper, source, destination,count)

count=0
tower_of_hanoi(5, "A", "B", "C",count)
print(count)