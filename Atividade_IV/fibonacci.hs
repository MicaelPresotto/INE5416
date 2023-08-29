fibonacci :: Int -> Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci x = fibonacci(x-2) + fibonacci(x-1)
main :: IO ()
main = do
    xis <- getLine
    let x = read xis :: Int
    print (fibonacci x)
