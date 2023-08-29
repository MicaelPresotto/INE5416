type Point3D = (Double, Double, Double)
distance :: Point3D -> Point3D -> Double
distance (x1, y1, z1) (x2, y2, z2) = sqrt((x2-x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
main :: IO ()
main = do
    input1 <- getLine
    let [x1, y1, z1] = map read (words input1) :: [Double]

    input2 <- getLine
    let [x2, y2, z2] = map read (words input2) :: [Double]

    let p1 = (x1, y1, z1)
    let p2 = (x2, y2, z2)

    print(distance p1 p2)