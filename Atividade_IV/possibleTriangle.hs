trianguloPossible :: Int -> Int -> Int -> String
trianguloPossible x y z = if (abs(y-z) < x && x < (y+z)) && (abs(x-z) < y && y < (x+z)) && (abs(x-y) < z && z < (x+y)) then "Possivel" else "Nao eh possivel"

main :: IO ()
main = do
    xis <- getLine
    let x = read xis :: Int
    yu <- getLine
    let y = read yu :: Int
    zi <- getLine
    let z = read zi :: Int
    print (trianguloPossible x y z)
