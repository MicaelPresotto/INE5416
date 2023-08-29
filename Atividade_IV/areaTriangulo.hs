areaTriangulo :: Float -> Float -> Float
areaTriangulo x y = (x * y)/2
main = do
    xis <- getLine
    yu <- getLine
    let x = read xis :: Float
    let y = read yu :: Float
    print(areaTriangulo x y)