likeli.plot = function(y,n)
{
    L = function(p) dbinom(y,n,p)
    mle = optimize(L, interval=c(0,1), maximum=TRUE)$max
    p = (1:100)/100
    par(mfrow=c(2,1))
    plot(p, L(p), type='l')
    abline(v=mle)
    plot(p, log(L(p)), type='l')
    abline(v=mle)
    mle
}
likeli.plot(8,20)