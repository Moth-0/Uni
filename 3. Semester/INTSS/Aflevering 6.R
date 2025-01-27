# Data
x <- c(0.93, 0.47, 0.26, 0.16, 0.97, 0.74, 0.93, 0.36, 0.48, 0.49, 0.84, 0.77)
y <- c(8.56, 5.98, 6.83, 5.26, 9.78, 7.51, 8.41, 6.72, 6.82, 5.14, 7.56, 6.64)
sigma = 1

# Calculate means
x_mean <- mean(x)
y_mean <- mean(y)

# Calculate s_xy and s_xx
s_xy <- sum((x - x_mean) * (y - y_mean))
s_xx <- sum((x - x_mean)^2)

# Calculate beta_1 (slope) and beta_0 (intercept)
beta_1 <- s_xy / s_xx
beta_0 <- y_mean - beta_1 * x_mean

# Calculate predicted values and residuals
y_pred <- beta_0 + beta_1 * x
residuals <- y - y_pred

# Variance of beta_1
mse <- sigma / s_xx


# Print results
s_xx
s_xy
beta_1
beta_0
mse
