#进行单次试验并画出散点图
n <- 1000
p <- 0.3
coin <- sample(c("H", "T"), size = n, replace = TRUE, prob=c(p,1-p))
count <- cumsum(coin == "H")
freq <- count / (1:n)
plot(1:n, freq, type = "p", col = "blue",
     xlab = "掷硬币次数", ylab = "正面频率", main = "掷硬币模拟散点图")
#进行多次试验并画出直方图
m <- 100
counts <- vector()
for(i in 1:m){
  n<-1000
  p<-0.3
  coin<-sample(c("H","T"),size=n,replace=TRUE,prob=c(p,1-p))
  counts[i]<-sum(coin=="H")
}
hist(counts,breaks=20,freq=FALSE,xlab="正面向上次数",ylab="密度",main="连续模拟的正面向上次数分布图")
