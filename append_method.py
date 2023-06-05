# A helpful method called append adds an element to the end of a list.
fruits = ["Oranges", "Avocado", "Quavas", "Kiwi", "Mango"]
fruits.append("Banana")
print(fruits)

names = ["Carol", "Albert", "Ben", "Donna"]
print("&".join(sorted(names)))

majina = ["Carol", "Albert", "Ben", "Donna"]
majina.append("Eugenia")
print(sorted(majina))

# TUPLE
tuple_a = 1, 2
tuple_b = (1, 2)
print(tuple_a == tuple_b)
print(tuple_a[1])

# SETS
fruit = {"apple", "banana", "orange", "grapefruit"}
print("watermelon" in fruit)
print(fruit)
# Add an element
fruit.add("watermelon")
print(fruit)
# remove a random element
print(fruit.pop())

x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
y = set(x)
print(len(x) - len(y))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
