import sympy as sp
#Differation og integration 
a, v, t = sp.symbols('a,v,t')

x0 = 0

x = x0 + v*t+1/2*a*t**2

dx = sp.diff(x,t)
print(dx)
dx2 = sp.diff(x,t,t)
print(dx2)

xdt = sp.integrate(x,t)
xdt_2 = sp.integrate(x, (t, 0, t))
print(xdt)



sp.plot(x.subs(v,10).subs(a,1), dx2.subs(a,1), (t,0, 10))

#Differentialligninger
α, β, t = sp.symbols("α, β, t") # Definer symboler

v = sp.Function("v") # v er navnet på funktionen
diff_eq = sp.Eq(v(t).diff(t), α*v(t)+β) # skriv funktionen, her står det på formen v'=a*v+b

v1 = sp.dsolve(diff_eq) # Løser differentialligningen ikke fuldstændigt 
print(v1)

v2 = sp.dsolve(diff_eq, ics={v(0):0}) # Løser differentialligningen fuldstændigt, da v(0)=0
print(v2)

#Plot 2 funktioner som funktion af t
x1 = 10*sp.cos(1/6*sp.pi)*t
y1 = 10*sp.sin(1/6*sp.pi)*t-(5*t**2)
sp.plot_parametric((x1,y1), (t, 0, 1))