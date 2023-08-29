meuxor :: Bool -> Bool -> Bool
meuxor x y = if x == y then False else True

main = do
    xis <- getLine
    let x = read xis == 1
    yu <- getLine
    let y = read yu == 1  
    print (meuxor x y)
