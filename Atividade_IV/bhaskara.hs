bhaskara :: Double -> Double -> Double -> (Double, Double)
bhaskara a b c = ((-b + sqrt (b^2 - 4*a*c)) / (2*a), (-b - sqrt (b^2 - 4*a*c)) / (2*a))

main :: IO ()
main = do
    x <- getLine
    let a = read x :: Double

    y <- getLine
    let b = read y :: Double

    z <- getLine
    let c = read z :: Double

    let (raiz1, raiz2) = bhaskara a b c
    print raiz1
    print raiz2
