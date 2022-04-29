A <- 1:4 # 1부터 4까지 정수벡터를 A에 저장
B <- c(3,5,7,9) # 벡터 (3,5,7,9) 를 B에 저장
C <- rep(2, 4) # 2를 4번 반복한 수(벡터)를 C에 저장
x <- data.frame(A, B, C) # A,B,C 세개의 벡터를 열로하는 데이터프레임을 생성

dim(x) # x의 차원(행 및 열의 수)

print(x)

x <- seq(-6, 12, by=0.1) # -6부터 12까지 0.1씩 증가하는 수열을 생성
y <- pnorm(x, mean=3, sd=2) # x값에 대하여 N(3, 4)의 누적분포함수값을 벡터 y로 저장
plot(x, y, type="l", ylab="CDF", main="CDF of N(3, 4)")