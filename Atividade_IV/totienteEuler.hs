loop :: Int -> Int -> Int -> Int
loop current end cont
    | current > end = cont
    | mdc current end == 1 = loop (current + 1) end (cont + 1)
    | otherwise = loop (current + 1) end cont

mdc :: Int -> Int -> Int
mdc a b
    | a == b = a
    | a > b = mdc (a - b) b
    | otherwise = mdc a (b - a)

main :: IO ()
main = do
    inputEnd <- getLine
    let end = read inputEnd :: Int

    let result = loop 1 end 0
    print result
