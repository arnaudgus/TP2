L=100;
Ttot=50;
dx=1;
dt=0.1;
D=5; //quand on passe de 4 à 6 on a de gros problèmes
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

//Numerical simulation of the diffusion process (explicit Euler method)
tic();
for n=1:T-1
    for i=2:L-1
        U(i,n+1)=U(i,n)+F*(U(i+1,n)-2*U(i,n)+U(i-1,n));
    end
end
calctime=toc();

figure
set(gca(),"auto_clear","off");

tgraph=1:(T/10-1):T;

for i=1:11
    plot((1:L)',U(:,tgraph(i)))
end

xstring(75,8,string(calctime));
set(gca(),"auto_clear","on");
