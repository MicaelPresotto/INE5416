main = do
    xis <- getLine
    let x = read xis :: Int
    print(abs(x))