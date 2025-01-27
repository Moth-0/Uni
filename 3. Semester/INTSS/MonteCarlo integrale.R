# Antal simuleringer
n = 10000000  

# Generer n tilfældige punkter i intervallet [0, 1.5]
x = runif(n, min = -2, max = 3)

# Funktion at integrere: log(1 + sin(x))
f = x*sqrt(x+2)

# Approksimer integralet som gennemsnittet af f(x) gange intervallets længde
i = mean(f) * 5  

# Udskriv resultatet
i
