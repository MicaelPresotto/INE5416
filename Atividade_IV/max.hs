maximumCustom :: Float -> Float -> Float -> Float
maximumCustom a b c
    | a >= b && a >= c = a
    | b >= a && b >= c = b
    | otherwise = c

main = do
    input <- getLine
    let [a, b, c] = map read (words input) :: [Float]
    print(maximumCustom a b c)