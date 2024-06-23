"""
A while loop and if/else to make a
sideways pyramid
*
**
***
****
*****
****
***
**
*
"""

# create a variable for the * symbol
ast = "*"

# iterate through a loop to reach a half pyramid
# by adding one * until "i" is 4 + 1 to print 5 *
# then iterate through again and slice the last *
# each time until 10 steps has been met (step 11 is non-inclusive)
# leaving 1 * remaining
# for i in range(0, 11):
#     if i < 4:
#         print(ast)
#         ast = ast + "*"
#     else:
#         if i > 5:
#             print(ast)
#             ast = ast[:-1]


# star = "*"
# for i in range(10):
#     if i >= 5:
#         star = star[:-2]
#         print(star)
#         star += "*"


for i in range(11):
    print(ast)
    if i < 4:
        ast += "*"
    else:
        ast = ast[:-1]
