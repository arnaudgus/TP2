//Parameters
N=10000;
dt=0.003;
R=4*(%pi)^2;
A=0.1;
x0=1;
y0=0;

//creating the vectors 

t=0:dt:(N-1)*dt
x=zeros(N,1)
y=zeros(N,1)

//initialization
x(1)=x0;
y(1)=y0;

//loop
for i=1:N-1
    x(i+1)=x(i)+y(i)*dt;
    y(i+1)=y(i)-(A*y(i)+R*x(i))*dt;
end


figure;
plot(t',x);


