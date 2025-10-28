def generate_fibonacci(n): 
    """Generate first n Fibonacci numbers.""" 
    if n <= 0: 
        return [] 
    elif n == 1: 
        return [0] 
    elif n == 2: 
        return [0, 1] 
     
    fib = [0, 1] 
    for i in range(2, n): 
        fib.append(fib[i-1] + fib[i-2]) 
     
    return fib 
 
def generate_primes(limit): 
    """Generate prime numbers up to limit using Sieve of Eratosthenes.""" 
    if limit < 2: 
        return [] 
     
    # Initialize sieve 
    sieve = [True] * (limit + 1) 
    sieve[0] = sieve[1] = False 
     
    for i in range(2, int(limit**0.5) + 1): 
        if sieve[i]: 
            for j in range(i*i, limit + 1, i): 
                sieve[j] = False 
     
    return [i for i in range(2, limit + 1) if sieve[i]] 
 
def generate_perfect_numbers(limit): 
    """Find perfect numbers up to limit.""" 
    def is_perfect(n): 
        if n <= 1: 
            return False 
        divisors = [1]  # 1 is always a divisor 
        for i in range(2, int(n**0.5) + 1): 
            if n % i == 0: 
                divisors.append(i) 
                if i != n // i:  # Avoid adding square root twice 
                    divisors.append(n // i) 
        return sum(divisors) == n 
     
    return [n for n in range(2, limit + 1) if is_perfect(n)] 
 
def analyze_number_properties(numbers): 
    """Analyze properties of a list of numbers.""" 
    if not numbers: 
        return {} 
     
    return { 
        "count": len(numbers), 
        "sum": sum(numbers), 
        "average": sum(numbers) / len(numbers), 
        "minimum": min(numbers), 
        "maximum": max(numbers), 
        "range": max(numbers) - min(numbers), 
        "even_count": len([n for n in numbers if n % 2 == 0]), 
        "odd_count": len([n for n in numbers if n % 2 == 1]), 
        "sorted_ascending": sorted(numbers), 
        "sorted_descending": sorted(numbers, reverse=True) 
    } 
 
def find_number_patterns(numbers): 
    """Identify patterns in a sequence of numbers.""" 
    if len(numbers) < 3: 
        return "Not enough numbers to identify patterns" 
     
    patterns = [] 
     
    # Check for arithmetic progression 
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)
1)] 
    if len(set(differences)) == 1: 
        patterns.append(f"Arithmetic sequence with common difference: 
{differences[0]}") 
     
    # Check for geometric progression 
    if all(n != 0 for n in numbers[:-1]): 
        ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1)] 
        if all(abs(r - ratios[0]) < 0.001 for r in ratios):  # Account for 
floating point errors 
            patterns.append(f"Geometric sequence with common ratio: 
{ratios[0]:.3f}") 
     
    # Check for squares 
    squares = [i*i for i in range(1, 20)] 
    if all(n in squares for n in numbers): 
        patterns.append("Perfect squares sequence") 
     
    # Check for Fibonacci-like 
    if len(numbers) >= 3: 
        is_fibonacci_like = True 
        for i in range(2, len(numbers)): 
            if numbers[i] != numbers[i-1] + numbers[i-2]: 
                is_fibonacci_like = False 
                break 
        if is_fibonacci_like: 
            patterns.append("Fibonacci-like sequence") 
     
    return patterns if patterns else ["No clear patterns detected"] 
 
def main(): 
    print("Number Pattern Generator and Analyzer") 
    print("="*50) 
     
    while True: 
        print("\nOptions:") 
        print("1. Generate Fibonacci sequence") 
        print("2. Generate prime numbers") 
        print("3. Find perfect numbers") 
        print("4. Analyze custom number sequence") 
        print("5. Find patterns in custom sequence") 
        print("0. Exit") 
         
        choice = input("\nEnter your choice: ") 
         
        if choice == '0': 
            print("Goodbye!") 
            break 
         
        elif choice == '1': 
            try: 
                n = int(input("How many Fibonacci numbers to generate? ")) 
                fib_sequence = generate_fibonacci(n) 
                print(f"First {n} Fibonacci numbers: {fib_sequence}") 
                 
                if fib_sequence: 
                    analysis = analyze_number_properties(fib_sequence) 
                    print(f"Sum: {analysis['sum']}") 
                    print(f"Average: {analysis['average']:.2f}") 
            except ValueError: 
                print("Please enter a valid number.") 
         
        elif choice == '2': 
            try: 
                limit = int(input("Find primes up to what number? ")) 
                primes = generate_primes(limit) 
                print(f"Prime numbers up to {limit}: {primes}") 
                print(f"Found {len(primes)} prime numbers") 
            except ValueError: 
                print("Please enter a valid number.") 
         
        elif choice == '3': 
            try: 
                limit = int(input("Find perfect numbers up to what number? 
")) 
                perfect = generate_perfect_numbers(limit) 
                if perfect: 
                    print(f"Perfect numbers up to {limit}: {perfect}") 
                else: 
                    print(f"No perfect numbers found up to {limit}") 
            except ValueError: 
print("Please enter a valid number.") 
elif choice == '4': 
try: 
numbers_str = input("Enter numbers separated by spaces: ") 
numbers = [int(x) for x in numbers_str.split()] 
analysis = analyze_number_properties(numbers) 
print(f"\nAnalysis of {numbers}:") 
print(f"Count: {analysis['count']}") 
print(f"Sum: {analysis['sum']}") 
print(f"Average: {analysis['average']:.2f}") 
print(f"Range: {analysis['minimum']} to 
{analysis['maximum']}") 
print(f"Even numbers: {analysis['even_count']}") 
print(f"Odd numbers: {analysis['odd_count']}") 
except ValueError: 
print("Please enter valid numbers separated by spaces.") 
elif choice == '5': 
try: 
numbers_str = input("Enter numbers separated by spaces: ") 
numbers = [int(x) for x in numbers_str.split()] 
patterns = find_number_patterns(numbers) 
print(f"\nPatterns found in {numbers}:") 
for pattern in patterns: 
print(f"- {pattern}") 
except ValueError: 
print("Please enter valid numbers separated by spaces.") 
else: 
print("Invalid choice. Please try again.") 
if __name__ == "__main__": 
main()