function [b] = classify(XTrain_fName, yTrain_fName, XTest_fName)
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
k = 8;
% ------ REPLACE WITH YOUR CODE ------
% Filler code - replace with your code
nTest = size(XTest,1);
b = zeros(nTest, 1);

%D = knn(XTrain, XTest, k);
DD = zeros(nTest,k);

% Filler code - replace with your code
nTest = size(XTest,1);
nTrain = size(XTrain,1);
tmpResult = zeros(nTest, 1);


%tmpResult = zeros(nTest,nTrain)
D = zeros(nTest,k);


%tmpResult = XTest * XTrain';
for i = 1 : nTest
    tmpXTest = XTest(i, :);
    for j = 1 : nTrain
        v = tmpXTest - XTrain(j, :);
        tmpResult(j) = (v * v');
    end
    [~,index] = sort(tmpResult);
    D(i, :) = index(1:k) ; 
end

for i = 1: nTest
    for j = 1 : k
        DD(i,j) = yTrain(D(i,j));
    end
    b(i) = mode(DD(i,:)) - 1;
end



end


