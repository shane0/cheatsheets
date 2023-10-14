# basics

## Reverse a string.

```python
def reverse_string(string):
  """Reverses a string.

  Args:
    string: A string.

  Returns:
    A reversed string.
  """

  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string

# Example usage:

print(reverse_string("Hello World"))
```

Output:

```
dlroW olleH
```

## Find the factorial of a number.

```python
def factorial(number):
  """Finds the factorial of a number.

  Args:
    number: A number.

  Returns:
    The factorial of the number.
  """

  factorial = 1
  for i in range(1, number + 1):
    factorial *= i
  return factorial

# Example usage:

print(factorial(5))
```

Output:

```
120
```

The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial of 0 is 1, according to the convention for an empty product.

For example, 5! is equal to 120, since 120 is the product of 1, 2, 3, 4, and 5.

Factorials are used in many areas of mathematics, including combinatorics, probability, and statistics. They are also used in some areas of computer science, such as algorithm design and cryptography.

Here is a mathematical definition of factorial:

```
n! = 1 * 2 * 3 * ... * n
```

where n is a non-negative integer.

Here is a recursive definition of factorial:

```
0! = 1
n! = n * (n - 1)!
```

for n > 0.

Factorials can also be represented using the gamma function, which is a generalization of the factorial function to non-integer values.

Factorials are used in many areas of mathematics, including combinatorics, probability, and statistics. They are also used in some areas of computer science, such as algorithm design and cryptography.

Here are some specific examples of how factorials are used:

* **Combinatorics:** Factorials are used to count the number of ways to arrange a set of objects. For example, there are 5! (120) ways to arrange 5 distinct objects in a row.
* **Probability:** Factorials are used to calculate probabilities of events. For example, the probability of getting 5 heads in a row when flipping a coin is 1/32, which can be calculated using factorials.
* **Statistics:** Factorials are used in some statistical tests, such as the chi-squared test.
* **Computer science:** Factorials are used in some algorithms, such as the quicksort algorithm and the traveling salesman problem.
* **Cryptography:** Factorials are used in some cryptographic algorithms, such as the RSA cryptosystem.

In addition to these specific examples, factorials are also used in many other areas of mathematics and science. For example, they are used in the study of number theory, graph theory, and differential equations.

Factorials are a powerful and versatile mathematical tool with many applications in the real world. Understanding factorials can help you to better understand many different areas of mathematics and science.

## Check if a number is prime.

```python
def is_prime(number):
  """Checks if a number is prime.

  Args:
    number: A number.

  Returns:
    True if the number is prime, False otherwise.
  """

  if number <= 1:
    return False

  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False

  return True

# Example usage:

print(is_prime(7))
print(is_prime(9))
```

Output:

```
True
False
```

## Find the greatest common divisor of two numbers.

```python
def gcd(a, b):
  """Finds the greatest common divisor of two numbers.

  Args:
    a: A number.
    b: A number.

  Returns:
    The greatest common divisor of the two numbers.
  """

  while b != 0:
    a, b = b, a % b

  return a

# Example usage:

print(gcd(12, 18))
```

Output:

```
6
```

## Find the least common multiple of two numbers.

```python
def lcm(a, b):
  """Finds the least common multiple of two numbers.

  Args:
    a: A number.
    b: A number.

  Returns:
    The least common multiple of the two numbers.
  """

  return (a * b) // gcd(a, b)

# Example usage:

print(lcm(12, 18))
```

Output:

```
36
```
