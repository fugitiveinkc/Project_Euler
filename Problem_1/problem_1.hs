-- Problem title:  Multiples of 3 and 5
-- Summary: Find sum of all the multiples of 3 or 5 below 1000


problem_1 x = sum [x | x <- [1..x-1] , x `mod` 3 == 0 || x `mod` 5 == 0]
