#Implementation of Tower Of Hanoi problem for 'n' no. of disks by Python

#using recursive function
def towerOfHanoi(n, source, destination, auxilliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    
    towerOfHanoi(n-1, source, auxilliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)

    towerOfHanoi(n-1, auxilliary, destination, source)

n = 5
towerOfHanoi(n, 'A', 'B', 'C')

    