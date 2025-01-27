from sympy import * 
#Differation og integration 
a, v, t = symbols('a,v,t')

x0 = 0

x = x0 + v*t+1/2*a*t**2

dx = diff(x,t)
print(dx)
dx2 = diff(x,t,t)
print(dx2)

xdt = integrate(x,t)
xdt_2 = integrate(x, (t, 0, t))
print(xdt)



plot(x.subs(v,10).subs(a,1), dx2.subs(a,1), (t,0, 10))

#Differentialligninger
α, β, t = symbols("α, β, t")

v = Function("v")
diff_eq = Eq(v(t).diff(t), α*v(t)+β)

v1 = dsolve(diff_eq)
print(v1)

v2 = dsolve(diff_eq, ics={v(0):0})
print(v2)

#Plot 2 funktioner som funktion af t
x1 = 10*cos(1/6*pi)*t
y1 = 10*sin(1/6*pi)*t-(5*t**2)
plot_parametric((x1,y1), (t, 0, 1))