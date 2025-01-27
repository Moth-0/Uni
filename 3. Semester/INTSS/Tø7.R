P = matrix(c(0.5,0.4,0.1,0.2,0.5,0.3,0.1,0.3,0.6), nrow=3, ncol=3, byrow=TRUE)
A = t(P)-diag(1,3)
A[3,] = 1
b = matrix(c(0,0,1), nrow=3, ncol=1, byrow=TRUE)
A
solve(A,b)