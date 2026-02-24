import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.array([10,20,30])
result = arr + arr2
print(result)

# vectorized vs loop example
a=np.array([2,4,6])
b=2
c=a*b
print(c)

arr=np.arange(12)
reshaped=arr.reshape(3, 4)
print(reshaped)

a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)
hstacked=np.hstack((a,b))
print(hstacked)
dstacked=np.dstack((a,b))
print(dstacked)

data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
np.median(data)
np.var(data)
np.std(data)

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))

#task 1
import numpy as np

scores=np.random.randint(50,101 , size=(5,3))
subject_means=scores.mean(axis=0)
centered_scores = scores - subject_means
print("Original Scores (Students x Subjects):")
print(scores)

print("\nMean of Each Subject:")
print(subject_means)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)

#task 2

data=np.arange(24)
reshape_data=data.reshape(4,3,2)
final_data=reshape_data.transpose(0, 2, 1)
print("Final shape:",final_data.shape)
print("Final Array:")
print(final_data)