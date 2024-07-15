set(0,'DefaultFigureColor',[1 1 1])
set(0, 'defaultaxesfontsize', 15)
set(0, 'defaultlinelinewidth', 2)
set(0,'DefaultTextInterpreter', 'latex')
set(0,'defaultAxesTickLabelInterpreter','latex');
set(0, 'defaultLegendInterpreter','latex')
set(0,'DefaultAxesColorOrder',brewermap(NaN,'Set2'))

territory=56.5;
ne=60;
K=32.6; 
k=0.09;
beta_v=0.77;
beta_h=0.70;
tau=4.5;
omega_v=2.5;
g=4.5;
lv=1/2.5;
H=62.5;

t_interval = linspace(1,365,365);
init_cond = [10000,0,0,0]';

[solt, soly] = ode45(@(t,Y) odefcn(t,Y,ne,K) , linspace(1,365,365) , init_cond);
solv=soly(:,4)/territory;

time_points=linspace(1,335,335);
solt_d=solt(time_points);
solv_d=solv(time_points);

fun = @(x)sseval(x,solt_d,solv_d); 
x0 = [600, 110, 20000,60,2.718];
options = optimset('MaxFunEvals',1000);
bestx = fminsearch(fun,x0,options);

tdata1=linspace(1,3*365,3*365+1);
fit=(bestx(1)*bestx(5).^((-(1/bestx(3)).*(solt_d-bestx(2)).^2)).*(1+erf((1/bestx(4))*(solt_d-bestx(2)))));


t=linspace(1,365,366);

RVH=k*beta_h./mv(t);
RHV=k*beta_v*g*(lv./(lv+mv(t))).*(bestx(1)*bestx(5).^((-(1/bestx(3)).*(t-bestx(2)).^2)).*(1+erf((1/bestx(4))*(t-bestx(2)))))/H;
R0=RVH.*RHV;
IER=(RHV.*RVH-1)./(RHV.*RVH+RVH);
IER=max(0,IER);

dom = [0 365];
 
N = chebop(@(x,u,v,w) [diff(u)-(k*beta_v*(bestx(1)*bestx(5).^((-(1/bestx(3)).*(x-bestx(2)).^2)).*(1+erf((1/bestx(4))*(x-bestx(2)))))/H).*(u-1).*v-(1/tau).*u; 
     diff(v)-(1/omega_v).*(v-w)-((0.031+95820*exp((13.51711126-12.65781793*cos((2*pi*x/365)+12.37433899+(2*pi*90/365)))-50.4))).*v;
     diff(w)-(k*beta_h).*u.*(w-1)-((0.031+95820*exp((13.51711126-12.65781793*cos((2*pi*x/365)+12.37433899+(2*pi*90/365)))-50.4))).*w], dom);

rhs = [0;0;0];

N.bc = @(x,u, v, w) [u(0)-u(365); v(0)-v(365); w(0)-w(365)];

x = chebfun(@(x) x, dom); 
u_init = 0.3651;
v_init = 0.3651;
w_init = 0.3651;
N.init = [u_init; v_init; w_init];

options = cheboppref();
options.display = 'iter';
options.bvpTol = 5e-16;
options.damping = false; 
options.discretization = 'values';

tinitmat=linspace(0,730,25);

[u, v, w] = solvebvp(N, rhs, options);

CER=u(0:365);
save('CERFeltre2015.mat','CER','IER','t','solt','solv','fit','R0')



function sse = sseval(x,tdata,ydata)
A = x(1);
B = x(2);
C = x(3);
D = x(4);
E = x(5);
sse = sum((ydata -(A*E.^((-(1/C).*(tdata-B).^2)).*(1+erf((1/D)*(tdata-B))))).^2);
end

function dYdt = odefcn(t,Y,ne,K)
dYdt = [ ne*dv(t)*Y(4)-(me(t)+de(t))*Y(1);
         de(t)*Y(1)-ml(t)*(1+(Y(2)/K))*Y(2)-dl(t)*Y(2);
         dl(t)*Y(2)-(mp(t)+dp(t))*Y(3);
         0.5*dp(t)*Y(3)-mv(t)*Y(4)];
end

function T=T(t)

    T=13.51711126-12.65781793*cos((2*pi*t/365)+12.37433899+(2*pi*90/365));
   
end

function de=de(t)

    de=(6.9-4*exp(-((T(t)-20)/4.1)^2))^-1;
      

end

function dl=dl(t)

    dl=(0.12*T(t)^2-6.6*T(t)+98)^-1;

end

function dp=dp(t)

    dp=(0.027*T(t)^2-1.7*T(t)+27.7)^-1;

end

function dv=dv(t)

    dv=(0.046*T(t)^2-2.77*T(t)+45.3)^-1;

end

function me=me(t)

    me=506-506*exp(-((T(t)-25)/27.3)^6);

end

function ml=ml(t)

    ml=0.029+858*exp(T(t)-43.4);

end

function mp=mp(t)

    mp=0.021+37*exp(T(t)-36.8);

end

function mv=mv(t)

    mv=0.031+95820*exp(T(t)-50.4);

end
