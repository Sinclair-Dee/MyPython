x=0:0.01:pi/2;
y=sin(x);
n=length(y);

a1=polyfit(x,y,2);
z1=a1(1)*(x.^2)+a1(2)*(x)+a1(3);
za11=abs(z1-y);
za12=za11.^2;
EW1=max(za11)
E1=sum(za11)/n
D1=sqrt((sum(za12))/n)

a2=polyfit(x,y,3);
z2=a2(1)*(x.^3)+a2(2)*(x.^2)+a2(3)*(x)+a2(4);
za21=abs(z2-y);
za22=za21.^2;
EW2=max(za21)
E2=sum(za21)/n
D2=sqrt((sum(za22))/n)

a3=polyfit(x,y,4);
z3=a3(1)*(x.^4)+a3(2)*(x.^3)+a3(3)*(x.^2)+a3(4)*(x)+a3(5);
za31=abs(z3-y);
za32=za31.^2;
EW3=max(za31)
E3=sum(za31)/n
D3=sqrt((sum(za32))/n)