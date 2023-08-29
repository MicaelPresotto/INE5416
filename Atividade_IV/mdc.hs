mdc :: Int -> Int -> Int
mdc a b 
    | a == b = a
    | a > b = mdc (a-b) b
    | otherwise = mdc a (b-a)

main = do
    input <- getLine
    let [a,b] = map read (words input) :: [Int]
    print(mdc a b)