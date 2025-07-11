#Linear Search

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Target number is 20
target = 10

def find_number(numbers, target):
    
    print('numbers', numbers)
    print('target', target)
    position = 0

    while position < len(numbers):
        #print('position' ,position)

        if numbers[position] == target:
            print("Eureka position found is", position)
        
        position += 1

        if position == len(numbers):

            print(" list complete, no numbers found")


find_number(numbers, target)
