mdc :: Int -> Int -> Int
mdc a b 
    | a == b = a
    | a > b = mdc (a-b) b
    | otherwise = mdc a (b-a)
coprimos :: Int -> String
coprimos a
    | a == 1 = "Sao coprimos"

    | otherwise = "Nao sao coprimos"

main = do
    input <- getLine
    let [a,b] = map read (words input) :: [Int]
    let mdc1 = mdc a b
    print(coprimos mdc1)
