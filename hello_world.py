"""
This is a first program to output Hello World to the console. It will then
be enhanced to ask the user for their name and greet them by name.
Yoav Bierkatz - August 2026
"""

def main() -> None:
    name:str= input("What is your name? ")
    # join with spaces
    print("Hello,",name)
    #string concatenation
    print("Hello, " + name)
    #formatted string - f-string
    print(f"Hello, {name}")
    
    

# main guard
if __name__ == "__main__":
    main()
