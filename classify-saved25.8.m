function [c] = classify(XTrain_fName, yTrain_fName, XTest_fName)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

XTrain = csvread(XTrain_fName);
XTest = csvread(XTest_fName);
yTrain = csvread(yTrain_fName);
   


% ------ REPLACE WITH YOUR CODE ------;
n = (max(yTrain))+1;
m = length(yTrain);
probs = zeros(n,1);

for i = 1:m
probs(yTrain(i)+1)++;
end

probs = probs./m;

[a,b] = size(XTrain);
r = [];
for i = 1:b
for j = 1:n
for k = 1:a
if (yTrain(k)+1) == j
r = [r,XTrain(k,i)];
end
end
mu(i,j) = mean(r);
sigma(i,j) = var(r);
r = [];
end
end

nTest = size(XTest,1);
c = zeros(nTest,1);
[p,q] = size(XTest);
for i = 1:p
signal = 1;
max = 0;
for j = 1:n
pcf = probs(j);
for k = 1:q
pcf = pcf * normpdf(XTest(i,k), mu(k,j),sqrt(sigma(k,j)));
end
if pcf > max
max = pcf;
signal = j;
end
end
c(i) = signal;
end

end


