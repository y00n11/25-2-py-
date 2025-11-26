a={100,200,300,400,500}
b={400,500,600,700,800}

a.intersection_update(b)
print('in_up:', a)

#a값 고정
a={100,200,300,400,500}
a.difference_update(b)
print('di_up:', a)

#a값 고정
a={100,200,300,400,500}
a.symmetric_difference_update(b)
print('sy_up:', a)



