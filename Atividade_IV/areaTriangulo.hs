areaTriangulo :: Float -> Float -> Float
areaTriangulo x y = (x * y)/2
main :: IO ()
main = do
    x <- readLn :: IO Float
    y <- readLn :: IO Float
    print(areaTriangulo x y)