mdc :: Float -> Float -> Float
mdc a b 
    | a == b = a
    | a > b = mdc (a-b) b
    | otherwise = mdc a (b-a)

main = do
    input <- getLine
    let [a,b] = map read (words input) :: [Float]
    print (a * b / mdc a b)
