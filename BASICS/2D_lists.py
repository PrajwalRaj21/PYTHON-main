number_grid = [
   [1,2,3,4,5],
   [5.6,7,8],
   [0]
]




print(number_grid[0], [1])
print(number_grid[1])
print(number_grid[2])


#nested for loop

for row in number_grid:
   for col in row:
      print(col)