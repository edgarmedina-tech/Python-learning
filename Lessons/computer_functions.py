def check_computer(ram, storage, requirements):
    if ram >= requirements["ram_excellent"] and storage >= requirements["storage_excellent"]:
        return "Excellent", "Meets requirements"
    elif ram >= requirements["ram_minimum"] and storage >= requirements["storage_minimum"]:
        return "Good", "Meets minimum requirements"
    elif ram < requirements["ram_minimum"] and storage < requirements["storage_minimum"]:
        return "Needs Upgrade", "RAM and Storage"
    elif ram < requirements["ram_minimum"]:
        return "Needs Upgrade", "RAM"
    else:
        return "Needs Upgrade", "Storage"

def create_computer():
    brand = input("What is the brand of the computer? ")
    ram = get_number("How much RAM does the computer have? ", 4, 256)
    storage = get_number("How much storage does the computer have? ", 128, 8192)

    computer = {
        "brand": brand,
        "ram": ram,
        "storage": storage
    }
    return computer

def get_number(question, minimum, maximum):
    while True:
        try:
            number = int(input(question))
            if number < minimum or number > maximum:
                print("Please enter a number between", minimum, "and", maximum)
                continue
            return number
        except ValueError:
            print("Please enter a number")

def validate_computer(computer):
    required_keys = ["brand", "ram", "storage"]

    for key in required_keys:
        if key not in computer:
            return False
    
    if type(computer["brand"]) is not str:
        return False
    if computer["brand"].strip() == "":
        return False
    
    if type(computer["ram"]) is not int:
        return False
    if computer["ram"] <= 0:
        return False
    
    if type(computer["storage"]) is not int:
        return False
    if computer["storage"] <= 0:
        return False
    
    return True