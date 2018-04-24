x <- read.table("lab2in.dat")
l <- c()
i <- 1
while(i<=512){
l[[i]] <- mean(x$V1[(6114*(i-1)+1):(6114*i)])
i = i + 1}
plot(l)
qqnorm(l)
hist(l)