isPrime :: Int -> String
isPrime n
  | n <= 1 = "Nao eh primo"
  | otherwise = if any (\i -> n `mod` i == 0) [2..floor (sqrt (fromIntegral n))]
                    then "Nao eh primo"
                    else "Eh primo"

main :: IO ()
main = do
    x <- readLn :: IO Int
    print(isPrime x)

