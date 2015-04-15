--Problem title: Largest prime factor
--Problem summary: What is the largest prime factor of the number 6008511475143

factor::Integer -> [Integer] --factors numbers
factor x = [ y | y <- [2..ceiling (sqrt (fromIntegral x))], (mod x y) == 0]

prime_test::Integer -> Bool --checks to see if number is prime
prime_test x
  | prime_list == [] = True
  | otherwise = False
  where prime_list = [ y | y <- factor x, x `mod` y == 0  ]

highest_prime_factor::Integer -> Integer --calculates highest prime factor
highest_prime_factor x = last [y | y <- factor x, prime_test y == True]
