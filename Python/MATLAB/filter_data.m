%% open data file to be filtered
    M = csvread('C:\Users\alex\Documents\MeasurementGit\BMRdrying\Python\data\Laser\01.09.17_025_Laser_open.csv',1,2);
%% Design filter parameters
cf = 1*10^-10;  %Normalized corner frequency (0-pi)
b = cf*sinc(cf*(-15:35));
b = b.*chebwin(51)';  %hamming windown looked like a good option.
% fvtool(b,1)

%% filter
r = conv(b,M);
tmp = r*max(M)/max(r);
figure(1)
plot(tmp(50:end-50))
title('Filtered')
figure(2)
plot(M)
title('Original')
%axis([0 600000 -.006 .002])
drawnow