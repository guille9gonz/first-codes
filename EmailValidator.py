def validate(email):
    wrong = "Email is invalid"
    if email.count("@") != 1 or email.count(".") == 0:
        return wrong
    recipient = email.split("@")[0]
    domain = email.split("@")[1].split(".")[0]
    toplevel = email.split("@")[1].split(".")[1]
    special = [".", "_"]
    hyphen = "-"
    toplevel_names = ["com", "net", "org", "tech", "es"]
    if len(recipient) < 3 or len(recipient) > 24 or recipient[0] in special or recipient[-1] in special:
        return wrong
    for l in recipient:
        if not l.isalnum() and l not in special:
            return wrong
    if len(domain) < 3 or len(domain) > 12:
        return wrong
    for c in domain:
        if not c.isalnum() and c != hyphen:
            return wrong
    if toplevel not in toplevel_names:
        return wrong
    return "Email is valid"

def main():
    email = input("Enter email:\n")
    print(validate(email))

if __name__ == "__main__":
    main()