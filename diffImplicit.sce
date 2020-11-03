L=100;
Ttot=50;
dx=1;
dt=0.1;
D=6;
T=round(Ttot/dt);

//initial gaussian spatial distribution 
x0=L/2;
d=5;
A=10;
x=1:L;
init=A*exp(-(x-x0).^2/(2*d^2));

U=zeros(L,T);
U(:,1)=init';

F=D*dt/dx^2;

//Numerical simulation of the diffusion process (implicit Euler method)
//Building the diffusion matrix
A=zeros(L,L);
A(1,1)=1;
A(L,L)=1;
for i=2:(L-1)
    A(i,i-1)=-F;
    A(i,i)=1+2*F;
    A(i,i+1)=-F;
end
iA=inv(A);

for n=1:T-1
    b=U(:,n);
    U(:,n+1)=iA*b;
end

figure
set(gca(),"auto_clear","off");

tgraph=1:(T/10-1):T;

for i=1:11
    plot((1:L)',U(:,tgraph(i)))
end
set(gca(),"auto_clear","on");

