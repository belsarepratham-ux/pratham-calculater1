class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            self.history.append(f"{a} / {b} = Error: Division by zero")
            return "Error: Division by zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Calculate power (a^b)"""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """Calculate square root"""
        if a < 0:
            self.history.append(f"√{a} = Error: Cannot calculate square root of negative number")
            return "Error: Cannot calculate square root of negative number"
        result = a ** 0.5
        self.history.append(f"√{a} = {result}")
        return result
    
    def get_history(self):
        """Get all calculations history"""
        if not self.history:
            return "No history yet!"
        return "\n".join(self.history)
    
    def clear_history(self):
        """Clear all history"""
        self.history = []
        return "History cleared!"


def main():
    calc = Calculator()
    
    print("=" * 50)
    print("  Welcome to Pratham's Calculator!")
    print("=" * 50)
    print("\nOperations available:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
    print("\n" + "=" * 50)
    
    while True:
        print("\nEnter operation (1-9): ", end="")
        choice = input().strip()
        
        if choice == '9':
            print("Thank you for using Pratham's Calculator! Goodbye!")
            break
        
        elif choice == '7':
            print("\nCalculation History:")
            print("-" * 40)
            print(calc.get_history())
            print("-" * 40)
        
        elif choice == '8':
            print(calc.clear_history())
        
        elif choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                elif choice == '4':
                    result = calc.divide(num1, num2)
                elif choice == '5':
                    result = calc.power(num1, num2)
                
                print(f"\nResult: {result}")
            
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        
        elif choice == '6':
            try:
                num = float(input("Enter number: "))
                result = calc.square_root(num)
                print(f"\nResult: {result}")
            
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        else:
            print("Invalid choice! Please enter a number between 1-9.")


if __name__ == "__main__":
    main()
