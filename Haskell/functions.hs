
doubleMe x = x + x

doubleUs x y = doubleMe x + doubleMe y


getFithElement x = (if length x > 5 then x !! 4 else -1)

concatenate x y = x ++ y

prime x = (if any (\x -> x) [x `mod` i == 0 | i <- [2..x-1]] then False else True)


listSubtract :: [Integer] -> [Integer] -> [Integer]
listSubtract (x:xs) (y:ys) = (x-y) : listSubtract xs ys
listSubtract [] [] = []
listSubtract _ _ = error "Lists are not the same length"

