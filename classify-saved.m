function [p] = classify(XTrain_fName, yTrain_fName, XTest_fName)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

XTrain = csvread(XTrain_fName);
XTest = csvread(XTest_fName);
yTrain = csvread(yTrain_fName);

for i = 1:size(yTrain,1)
    yTrain(i) = yTrain(i) + 1;
end    


% ------ REPLACE WITH YOUR CODE ------
%c = zeros(size(XTest,1),1);
k = 4;
[m,f] = size(XTest);
n = size(XTrain,1);
D = zeros(m,k);
E = zeros(n,1);

for a = 1:m
E = zeros(n,1);
for b = 1:n
z = 0;
for c = 1:f
z = z + (XTest(a,c)-XTrain(b,c))^2;
end
E(b) = sqrt(z);
end
for b = 1:k
y = 1;
for c = 2:n
if ((E(y)<0) || ((E(c)>=0) && (E(c)<E(y))))
y = c;
end
end
D(a,b) = y;
E(y) = -1;
end
end

p = zeros(m, 1);
cc = max(yTrain);
for i = 1:m
count = zeros(cc, 1);
for j = 1:k
count(yTrain(D(i,j))) = count(yTrain(D(i,j))) + 1;
end
y = 1;
for l = 1:cc
if count(l)>count(y)
y=l;
end
end
p(i)=y-1;
end

end


