#Rule Book for Big O
#  1. Worst case
#  2. Remove constants
#  3. Different terms for input
# 4. Drop non dominants

# Rule 2
def print_first_item_then_first_half_then_say_hi_100_times(items):
    # Print the first item
    print(items[0])

    # Calculate the middle index
    middle_index = len(items) // 2
    index = 0

    # Print the first half of the items
    while index < middle_index:
        print(items[index])
        index += 1

    # Say 'hi' 100 times
    for i in range(100):
        print('hi')
