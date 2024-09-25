def validate(email):
    wrong = "Email is invalid"

    #Check if the email contains just one "@" and at least a dot
    if email.count("@") != 1 or email.count(".") == 0:
        return wrong
    
    #Split the email in three parts (username, domain and top-level domain)
    username = email.split("@")[0]
    domain = email.split("@")[1].split(".")[0]
    toplevel = email.split("@")[1].split(".")[1]
    special = [".", "_"]
    hyphen = "-"
    toplevel_names = ["com", "net", "org", "tech", "es"]

    #Check if the username and the domain have an appropriate length and only contain allowed characters
    if len(username) < 3 or len(username) > 24 or username[0] in special or username[-1] in special:
        return wrong
    for l in username:
        if not l.isalnum() and l not in special:
            return wrong
    if len(domain) < 3 or len(domain) > 12:
        return wrong
    for c in domain:
        if not c.isalnum() and c != hyphen:
            return wrong
    if toplevel not in toplevel_names:
        return wrong
    
    #If the address passes all the filters, it returns "Email is valid"
    return "Email is valid"

def main():
    email = input("Enter email:\n")
    print(validate(email))

if __name__ == "__main__":
    main()
