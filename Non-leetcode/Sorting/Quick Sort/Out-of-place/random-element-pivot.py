import random

class Sort:
    def quickSort(self, array):
        if len(array) <= 1:
            return array
        
        pivot_element = array[random.randint(0, len(array) - 1)]
        less_than = [i for i in array if i < pivot_element]
        equal_to = [i for i in array if i == pivot_element]
        greater_than = [i for i in array if i > pivot_element]

        return self.quickSort(less_than) + equal_to + self.quickSort(greater_than)

# Test
nums = [5, 2, 8, 1, 3]
print(Sort().quickSort(nums))