'''Create a dictionary of students and marks.
Print keys and values separately.
Create a dictionary of squares {1:1, 2:4, 3:9} using a loop.'''

data={'neha':'90','varun':'80','harsh':'70'}
print(data)

keys={'neha','harsh','sidh','uday'}
values={90,80,23,45}
data=dict(zip(keys,values))

squares={}
for i in range(1,6):
    squares[i]=i**2
    print(squares)