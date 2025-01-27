# Data
x <- c(8.17, 8.31, 4.11, 6.51, 3.94, 7.22, 8.18, 6.06, 6.52, 7.16)
y <- c(28.01, 24.21, 16.80, 23.10, 12.28, 24.20, 24.85, 17.95, 23.07, 22.86)
sigma = 0.5

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
x_mean
y_mean
s_xx
s_xy
beta_1
beta_0
mse
