
## Joseph Rice

from statistics import mean

file_object = open('chocodata.txt','r')
lines = file_object.readlines()

Data = [map(int,x.split()) for x in lines]
#print(Data(1,0))

X = []
Y = []
for x,y in Data:
    X.append(x)
    Y.append(y)
    
#print(Y)
#print(X)


def Incrament_learner(X_value, Y_value, learn_rate,iterations):
    eta = learn_rate
    
    W0 = 5
    W1 = 0
    yhat = [0]*200
    for i in range(0,iterations):
        for k in range(0,len(X_value)):
            
            yhat[k] = W0 + W1*X_value[k]
            ##print(yhat)
            delta = Y_value[k] - yhat[k]
            ##print(delta)
            W0 = W0 + eta*delta*X_value[k]
            ##print(W0)
            W1 = W1 + eta*delta*X_value[k]
            ##print(W1)        
    
    
    
    
    return W0,W1,eta,iterations
    
    
w0,w1,eta,Times= Incrament_learner(X,Y,0.00001,5000)


### validation part
file_object = open('chocovalid.txt','r')
lines2 = file_object.readlines()

Data2 = [map(int,x.split()) for x in lines2]

X1 = []
Y1 = []
Y_hat1 = []

for x,y in Data2:
    X1.append(x)
    Y1.append(y)
    Y_hat1.append((w0+w1*x))
    
SSE = 0
SSS = 0
for i in range(0, len(Y1)):
    SSE += (Y1[i] - Y_hat1[i])**2
    SSS += Y1[i]**2
SST = SSS - len(Y1)*mean(Y1)
R2 = 1 - (SSE)/(SST)

file_object1 = open("learner1output.txt",'w')
file_object1.write("CS-5001: HW#1\n")
file_object1.write("Programer: Joseph Rice\n")
file_object1.write("\n")
file_object1.write("TRAINING:\n")
file_object1.write("Using learning rate eta = " + str(eta)+"\n")
file_object1.write("Using " + str(Times) + " iterations.\n")
file_object1.write("\n")
file_object1.write("OUTPUT:\n")
file_object1.write("w0 = " + str(w0)+"\n")
file_object1.write("w1 = "+ str(w1)+'\n')
file_object1.write("\n")
file_object1.write("VALIDATION\n")
file_object1.write("Sum-of-Squares Error = " + str(SSE) +"\n")
##file_object1.write("R2 = " + str(R2))
