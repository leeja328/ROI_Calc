# def numba(num):
#     new = []
#     new2 = []
#     if num == -1:
#         return 0
#     for x in range(num):
#         new.append(x)
#     for x in new:
#         if x % 3 == 0 and x % 5 == 0:
#             new2.append(x)
#         elif x % 3 == 0:
#             new2.append(x)
#         elif x % 5 == 0:
#             new2.append(x)
#         else:
#             new2.append(0)
    
#     return sum(new2)

# print(numba(7000))




# print(numba(6))



# def likes(names):
#     if names == []:
#         return "no one likes this"
#     elif len(names) == 1:
#         return (names[0] + " likes this")
#     elif len(names) == 2:
#         return (f"{names[0]} and {names[1]} like this")
#     elif len(names) == 3:
#         return (f"{names[0]}, {names[1]} and {names[2]} like this")
#     elif len(names) >= 4:
#         return (f"{names[0]}, {names[1]} and {len(names)-2} others like this")

# print(likes(['James', 'Victoria', 'Daisy', 'Izzy']))


# from venv import create


# def create_phone_number(n):
#     return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# def find_it(seq):
#     nums = {}
#     for x in seq:
#         nums[x] = 1
#         if x in nums:
#             nums[x] += 1

#     return(nums)

# print(find_it([1,2,1,1,1,1,1,1,1,1]))


# def get_middle(s):
#     x = len(s)
#     if x % 2 != 0:
#         return s[int((x/2)-0.5)]
#     else:
#         return f"{s[int((x/2)-1)]}{s[int(x/2)]}"

# print(get_middle('testing'))




# def array_diff(a, b):
#     z = []
#     if b == []:
#         return a
#     for num in b:
#         for num1 in a:
#             if num != num1:
#                 z.append(num)
#     return z

# print(array_diff([1,2,2,3], [1,2]))


# def array_diff(a, b):
#     y = set(a)
#     q = set(b)
#     i = y - q
#     w = []
#     for num in i:
#         w.append(num)
#     return w

# print(array_diff([1,2,2], [1]))


# x = [1,2,3]
# z = [2,3]
# y = set(x)
# q = set(z)
# i = y - q
# w = []
# for num in i:
#     w.append(num)
    
# print(w)



# def alphabet_position(text):
#     1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'

#     print(z)

# alphabet_position()
    


from ast import Num

num = 2
z = []
if len(num) == 1:
    print(num)
else:
    while len(num) > 1:
        for x in str(num):
            z.append(int(x))
        for q in str(z):
            
    