t = 0:0.01:(2-0.01);
x = sin(t.*(4*pi) + pi/2);
figure;
plot(t,x);
title('First sample func- Q2');
xlabel('time(s)');
ylabel('sample');

t1 = 0:1/3:(2-0.01);
x1 = sin(t1.*(4*pi) + pi/2);
figure;
plot(t1,x1);
title('Second sample func - Q2');
xlabel('time(s)');
ylabel('sample');

t2 = 0:0.01:2;	
x2 = sin(t2.*(8*pi) + pi/4);
figure;
plot(t2,x2);
title('First sample func - Q3');
xlabel('time(s)');
ylabel('sample');
t3 = 0:1/3:(2-0.01);
x3 = sin(t3.*(4*pi) + pi/2);
figure;
plot(t3,x3);
title('Second sample func - Q3');
xlabel('time(s)');
ylabel('sample');


