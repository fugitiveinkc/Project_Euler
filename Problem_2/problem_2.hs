-- Problem title: Even Fibonacci Numbers
-- Summary: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

-- Steps:
-- 1) Fib sequence generator (function)
-- 2) Remove all odd numbers (same function as above)
-- 3) Sum (add based from function above)

fibonacci :: Int -> Int
fibonacci 1 = 1
fibonacci 2 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

fibonaccisum = [fibonacci y | y <- [1..]] --Something tricky here
