
x = csvread('C:\Users\alex\Documents\MeasurementGit\BMRdrying\Python\data\Laser\01.16.18_031_laser_open.csv',1,2);
num = 5; %number of legender polynomials we use
x = x(:,1);
len = length(x);

t = linspace(0, len, len);
p = zeros(len, num);
for kk = 1:num
    p(:, kk) = t.^(kk-1);%exp(-t.^(kk-1));
end

e = p;
q = zeros(len,num);

np1 = p(:,1)'*p(:,1)/len;
q1 = p(:,1)/sqrt(np1);
q(:,1) = q1;

for i = 2:num
    for j = 1:i-1
        e(:,i)=e(:,i) - p(:,i)'*q(:,j)/len*q(:,j);
    end
    nei = sqrt(e(:,i)'*e(:,i)/len)
    q(:,i) = e(:,i)/nei;
end

figure(1)
plot(t,q)
title('Legendre Polynomials')

%part b
%x = (exp(-t))';
a = zeros(num,1); %a is for Legandre approximation
for i = 1:num
   a(i) =x' * q(:,i) / len; 
end

g = zeros(num);
for i=1:num
   for j=1:num
      g(i,j) = q(:,i)' * q(:,j)/len; 
   end
end

c = (g^-1)*a;

figure(2)
plot(t,x,'b',t,(c'*q'),'rx')
title('Legandre Approximation')