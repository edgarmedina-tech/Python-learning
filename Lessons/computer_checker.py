import json
from pathlib import Path

requirements_path = Path(__file__).with_name("requirements.json")

try:
    with open(requirements_path, "r") as file:
        requirements = json.load(file)
except FileNotFoundError:
    print("Error: requirements.json was not found")
    raise SystemExit
except json.JSONDecodeError:
    print("Error: requirements.json contains invalid JSON")
    raise SystemExit

required_keys = [
    "ram_minimum",
    "ram_excellent",
    "storage_minimum",
    "storage_excellent"
]
missing_keys = []

for key in required_keys:
    if key not in requirements:
        missing_keys.append(key)

if missing_keys:
        print("Configuration error!")
        print("Missing keys:")

        for key in missing_keys:
            print("-", key)
                
        raise SystemExit

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

computers = []
count = get_number("How many computers would you like to add? ", 1, 99)
for i in range(count):
    computer = create_computer()
    computers.append(computer)

lowest_ram = computers[0]["ram"]
lowest_ram_computer = computers[0]["brand"]
for computer in computers:
    computer_ram = computer["ram"]
    computer_ram_brand = computer["brand"]
    if computer_ram < lowest_ram:
        lowest_ram = computer_ram
        lowest_ram_computer = computer_ram_brand

lowest_storage = computers[0]["storage"]
lowest_storage_computer = computers[0]["brand"]
for computer in computers:
    computer_storage = computer["storage"]
    computer_storage_brand = computer["brand"]
    if computer_storage < lowest_storage:
        lowest_storage = computer_storage
        lowest_storage_computer = computer_storage_brand

upgrade_computers =  []
for computer in computers:
    rating, reason = check_computer(
        computer["ram"],
        computer["storage"],
        requirements
    )
    computer["rating"] = rating
    computer["reason"] = reason

    if rating == "Needs Upgrade":
        upgrade_computers.append(computer)

upgrade_count = 0
excellent_count = 0
good_count = 0
for computer in computers:
    rating = computer["rating"]
    reason = computer["reason"]
    if rating == "Needs Upgrade":
        upgrade_count += 1
    elif rating == "Excellent":
        excellent_count += 1
    elif rating == "Good":
        good_count += 1
    print(computer["brand"], "=", rating, "-", reason)
print("Summary:")
print("Excellent computers:", excellent_count)
print("Good computers:", good_count)
print("Computers needing upgrades:", upgrade_count)

for computer in upgrade_computers:
    print(
        computer["brand"], "-",
        "RAM:", computer["ram"], "GB",
        "-",
        "Storage:", computer["storage"], "GB",
        "-",
        "Needs:", computer["reason"]
        )