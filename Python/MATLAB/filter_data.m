%% open data file to be filtered
x = csvread('C:\Users\alex\Documents\MeasurementGit\BMR\Python\data\Laser\01.16.18_031_laser_open.csv',1,2);
M = x(:,1);
%% Design filter parameters
cf = .05;  %Normalized corner frequency (0-pi)
b = cf*sinc(cf*(-75:75));
b = b.*hamming(151)';  %hamming window looked like a good option.
%fvtool(b,1)

%% filter
r = conv(b,M);
%tmp = r*max(M)/max(r);
figure()
plot(r(150:end-150))
hold on
plot(M)
hold off
title('Filtered vs Original')
legend('Filtered','Original')
xlabel('Samples')
ylabel('Laser (mm)')