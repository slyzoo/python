email_1 = input("Enter your email : ")
index = email_1.index("@")

username_1 = email_1[:index]
domain_1 = email_1[index + 1:]

print(f"your username is {username_1} and domain is {domain_1}")

# and a shorter version of this is 

email_2 = input("Enter your email : ")

username_2 = email_2[:email_2.index("@")]
domain_2 = email_2[email_2.index("@") + 1:]

print(f"your username is {username_2} and domain is {domain_2}")
