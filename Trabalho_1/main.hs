import Data.Maybe
import Debug.Trace


matrizComparacao :: [[Int]]

matrizComparacao =[[-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1], [0, 1, 1, -1], [1, 0, 1, 0], [1, -1, 0, 1], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 1, 0], [1, 1, 0, -1], [0, 1, 0, 0], [0, -1, 0, 0], [0, 1, -1, -1], [0, 0, -1, 0], [1, -1, -1, 1], [1, 1, -1, -1], [0, 1, -1, 0], [0, -1, -1, 0], [1, 0, -1, -1], [1, 1, -1, 1], [1, -1, -1, 0], [-1, 0, 1, -1], [-1, 1, 0, 1], [-1, -1, 0, 0], [-1, 1, 1, -1], [-1, 1, 0, 0], [-1, -1, 0, 0], [-1, 0, 0, -1], [-1, 1, 1, 1], [-1, -1, 0, 0], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 1, 0], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 0, 0], [1, 1, 0, -1], [0, 0, 0, 0], [1, -1, 1, 1], [1, 0, -1, -1], [0, 1, -1, 1], [0, -1, -1, 0], [1, 0, -1, -1], [0, 1, -1, 1], [1, -1, -1, 0], [1, 1, -1, -1], [1, 1, -1, 0], [0, -1, -1, 0], [-1, 1, 0, -1], [-1, 1, 0, 0], [-1, -1, 0, 0], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1], [-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [1, 1, 1, -1], [1, 0, 1, 0], [1, -1, 1, 1], [1, 1, 0, -1], [0, 0, 0, 0], [0, -1, 0, 1], [0, 0, 0, -1], [1, 0, 0, 1], [1, -1, 0, 1], [0, 0, -1, -1], [0, 1, -1, 1], [0, -1, -1, 0], [1, 1, -1, -1], [1, 1, -1, 0], [1, -1, -1, 0], [1, 0, -1, -1], [1, 0, -1, 1], [1, -1, -1, 1]]


matrizPossibilidades :: [[Int]]

matrizPossibilidades =
    [ [(head (limite i [] 1)) .. (10 - head (limite i [] 0))]
    | i <- [0..80]
    ]


trocaElemento :: Int -> a -> [a] -> [a]

trocaElemento posicao elemento lista =
    take posicao lista ++ [elemento] ++ drop (posicao + 1) lista


for :: Int -> Int -> [Int] -> [[Int]] -> Maybe [Int]

for indice posicao solucao possibilidades
    | indice < 0 = Nothing
    | otherwise = do
        let tentativa_atual = resolve ((possibilidades !! posicao) !! indice) posicao solucao possibilidades
        case tentativa_atual of
            Just tentativa -> Just tentativa
            Nothing -> for (indice - 1) posicao solucao possibilidades


resolve :: Int -> Int -> [Int] -> [[Int]] -> Maybe [Int]

resolve elemento posicao solucao possibilidades
    | elemento `elem` obtemLinha (posicao `div` 9) solucao = Nothing
    | elemento `elem` obtemColuna (posicao `mod` 9) solucao = Nothing
    | elemento `elem` obtemRegiao (posicao `div` 27) ((posicao `mod` 9) `div` 3) solucao = Nothing
    | not (compara elemento posicao solucao) = Nothing
    | posicao == 80 = Just (trocaElemento 80 elemento solucao)
    | otherwise =
        let
            solucao_atual = trocaElemento posicao elemento solucao
            tentativa_for = for (length (possibilidades !! (posicao + 1))-1) (posicao + 1) solucao_atual possibilidades
        in
            tentativa_for

compara :: Int -> Int -> [Int] -> Bool

compara elemento posicao matriz =
    let
        acima = posicao - 9
        direita = posicao + 1
        abaixo = posicao + 9
        esquerda = posicao - 1
        comparaPosicao c p =
            case c of
                1 -> ((matriz!!p) == 0) || (matriz!!p < elemento)
                0 -> ((matriz!!p) == 0) || (matriz!!p > elemento)
                _ -> True
    in
        comparaPosicao (head (matrizComparacao !! posicao)) acima &&
        comparaPosicao (matrizComparacao !! posicao !! 1) direita &&
        comparaPosicao (matrizComparacao !! posicao !! 2) abaixo &&
        comparaPosicao (matrizComparacao !! posicao !! 3) esquerda


obtemLinha :: Int -> [Int] -> [Int]
obtemLinha linha matriz =
    [matriz!!i | i <- [linha*9 .. ((linha+1)*9)-1]]


obtemColuna :: Int -> [Int] -> [Int]
obtemColuna coluna matriz =
    [matriz!!i | i <- [coluna, coluna+9 .. coluna+72]]


obtemRegiao :: Int -> Int -> [Int] -> [Int]
obtemRegiao x_regiao y_regiao matriz =
    [matriz!!(((x_regiao*27)+(i*9))+(y_regiao*3)+j)|i<-[0..2],j<-[0..2]]


limite :: Int -> [Int] -> Int -> [Int]
limite posicao visitados comp
    | posicao `elem` visitados = 0:visitados
    | otherwise =
        let
            novos_visitados = posicao : visitados
            acima = posicao - 9
            direita = posicao + 1
            abaixo = posicao + 9
            esquerda = posicao - 1
            resAcima = if head (matrizComparacao !! posicao) == comp then limite acima novos_visitados comp else 0 : novos_visitados
            resDireita = if matrizComparacao !! posicao !! 1 == comp then limite direita (drop 1 resAcima) comp else 0 : drop 1 resAcima
            resAbaixo = if matrizComparacao !! posicao !! 2 == comp then limite abaixo (drop 1 resDireita) comp else 0 : drop 1 resDireita
            resEsquerda = if matrizComparacao !! posicao !! 3 == comp then limite esquerda (drop 1 resAbaixo) comp else 0 : drop 1 resAbaixo
        in
            (1 + head resAcima + head resDireita + head resAbaixo + head resEsquerda): drop 1 resEsquerda


mostrarSudokuFormatado :: [Int] -> String
mostrarSudokuFormatado solucao = concat [formatarLinha i | i <- [0..80]]
  where
    formatarLinha i
      | i > 0 && i `mod` 27 == 0 = "\n\n" ++ formatarElemento i
      | i > 0 && i `mod` 9 == 0  = "\n" ++ formatarElemento i
      | i > 0 && i `mod` 3 == 0  = "   " ++ formatarElemento i
      | otherwise                = formatarElemento i
      where
        formatarElemento i' = show (solucao !! i') ++ " "


main :: IO ()
main = do
    let solucao = replicate 81 0
    let possibilidades = matrizPossibilidades
    let resultado = for (length (head possibilidades)-1) 0 solucao possibilidades
    case resultado of
        Just res -> putStrLn (mostrarSudokuFormatado res)
        Nothing -> putStrLn "Não há solução."