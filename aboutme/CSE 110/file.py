first_name = "unknown"
last_name = "unknown"
email_address = "unknwon"
phone_number = "unknown"
job_title = "unknown"
id_number = "unknown"

print("please enter the following information\n")

first_name = input("first name: ")
last_name = input("last name: ")
email_address = input("email address: ")
phone_number = input("phone number: ")
job_title = input("job title: ")
id_number = input("id number: ")

print()
print("The ID Card is\n")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.capitalize()}")
print(f"id: {id_number}\n")
print(email_address.lower())
print(phone_number)