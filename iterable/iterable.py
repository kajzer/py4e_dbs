import random
# Using class
print("=========Class=========")
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
            
for c in Counter(3, 8):
    print(c)

# using generator
print("=======Generator=========")
def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1
        
for c in counter(3, 8):
    print(c)
    
# using generator
print("=======Generator v.2=========")
def my_gen(text):
    for char in text:
        yield char.upper()
        
for char in my_gen('abcdefg'):
    print(char)
    
# using generator expression
print("=======Generator expression=========")
def my_genexp(text):
    return (char.upper() for char in text)
    
for char in my_genexp('abcdefg'):
    print(char)

# iterator class
print("=======Class v.2=========")
class my_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

for char in my_iter('abcdef'):
    print(char)

    
# getitem method
print("=======Getitem method=========")
class my_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result
        
for char in my_getitem('abcd'):
    print(char)
    
print("=======Getting every second number=========")

print("=======Generator=========")
def even_gen():
    result = 0
    while True:
        yield result
        result += 2
        
limit = random.randint(10, 26)
count = 0
for even in even_gen():
    print(even)
    count += 1
    if count >= limit : break
        
print("=======Generator expression=========")
def even_genexp():
    return (num for num in even_gen())
    
count = 0
for even in even_genexp():
    print(even)
    count += 1
    if count >= limit : break

print("=======Class=========")
class even_iter():
    def __init__(self):
        self.value = 0
    def __iter__(self):
        return self
    def __next__(self):
        next_value = self.value
        self.value += 2
        return next_value
        
count = 0
for even in even_iter():
    print(even)
    count += 1
    if count >= limit : break

print("=======Getitem method=========")
class even_getitem():
    def __getitem__(self, index):
        return index * 2
        
count = 0
for even in even_getitem():
    print(even)
    count += 1
    if count >= limit : break