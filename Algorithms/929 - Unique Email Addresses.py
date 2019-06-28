def numUniqueEmails(emails):
    local = ""
    domain = []
    unique = []
    for email in emails:
        local = email.split("@")[0]
        domain.append(email.split("@")[1])
        if "." in local:
            local = local.replace(".", "")
        if "+" in local:
            local = local.split("+")[0]
        unique.append(local)

    result = []
    
    for l, d in zip(unique, domain):
        new = l + "@" + d
        result.append(new)
    
    print(len(set(result)))


numUniqueEmails(["test.email+alex@leetcode.com",
                 "test.e.mail+bob.cathy@leetcode.com",
                 "testemail+david@lee.tcode.com"])
