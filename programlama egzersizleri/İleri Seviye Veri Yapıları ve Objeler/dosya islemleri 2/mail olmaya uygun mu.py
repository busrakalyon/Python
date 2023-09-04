liste = list()


def check_gmail(email):
    return email.strip().lower().endswith("@gmail.com") or email.strip().lower().endswith("@hotmail.com") or email.strip().lower().endswith("@example.com") or email.strip().lower().endswith("@outlook.com") or email.strip().lower().endswith("@yahoo.com")

with open("mailler.txt", "r+", encoding="utf-8") as file:

    for satir in file:
        email = satir.strip()
        if check_gmail(email):
            liste.append(email)


for i in liste:
    print(i)
