potencia :: Int -> Int -> Int
potencia x y = x ^ y
main = do
    xis <- getLine
    let x = read xis :: Int
    yu <- getLine
    let y = read yu :: Int
    print (potencia x y)