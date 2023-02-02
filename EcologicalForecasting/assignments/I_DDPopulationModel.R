# Density-dependent population model
# Difference equation for logistic growth:
# N_(t+1) = N_t + rN_t(1 - N_t/K)

# N = population size (at time t)
# r = population growth rate (r=1 indicates doubling of population at each gen.)
# K = population limit

library(dplyr)

# 1. assume r and K values...
r = 1.15
K = 300

# 2. create 'time' vector (i.e. number of generations)
time = seq(1,100)
head(time)
tail(time)

# 3. create vector of empty N values and assign starting population value
N <- c(0) %>%
  rep(len = length(time))
N[1] = 10

# 4. create logistic growth function
log_growth <- function(r, K, N){
  NextN = N + r*N*(1 - N/K)
  return(NextN)
}

# 5. calculate population (N) at each generation (t) using for() loop
for (t in 2:length(time)){
  N[t] = log_growth(r=r, K=K, N=N[t-1])
}

# 6. plot population growth with plot()
plot(time, N, type = "b")

# identify time (t) at which population capacity (K) is reached
t_lim <- which.max(N >= K)
sprintf("Time at which K pop. limit is reached = %d", t_lim)

