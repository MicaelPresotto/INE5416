media :: Float -> Float -> Float -> String
media x y z = if (x+y+z)/3 >= 6 then "Aprovado" else "Reprovado"

main = do
    xis <- getLine
    let x = read xis :: Float
    yu <- getLine
    let y = read yu :: Float
    zi <- getLine
    let z = read zi :: Float
    print (media x y z)
