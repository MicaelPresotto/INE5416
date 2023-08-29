ehDivisivel :: Int -> Int -> String
ehDivisivel a b
    | a `mod` b == 0 = "Sim"
    | otherwise = "Nao"

main = do
    input <- getLine
    let [a,b] = map read (words input) :: [Int]
    print(ehDivisivel a b)