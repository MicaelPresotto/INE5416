operador :: String -> Float -> Float -> Float
operador operador x y 
    | operador == "+" = x + y
    | operador == "-" = x - y
    | operador == "/" = x/y
    | otherwise = x*y

main :: IO ()
main = do
    op <- getLine
    vars <- getLine
    let [x,y] = map read (words vars) :: [Float]
    print(operador op x y)

    
    