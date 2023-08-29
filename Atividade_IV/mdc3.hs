mdc :: Int -> Int -> Int
mdc a b
    | a == b = a
    | a > b = mdc (a-b) b
    | otherwise = mdc a (b-a)
main = do
    input <- getLine
    let [a,b, c] = map read (words input) :: [Int]
    let mdc1 = mdc a b
    print(mdc mdc1 c)