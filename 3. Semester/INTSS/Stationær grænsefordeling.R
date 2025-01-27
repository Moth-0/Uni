n = 3
P = matrix(c(
  0.9, 0.075, 0.025,
  0.15, 0.80, 0.05, 
  0.25, 0.25, 0.50
), nrow=n, ncol=n, byrow=TRUE)
A = t(P)-diag(1,n)
A[n,] = 1
b = rep(0,n-1)
b = c(b,1)
A
solve(A,b)