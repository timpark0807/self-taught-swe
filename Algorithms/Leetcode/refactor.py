def numUniqueEmails(emails):
    seen = set()
    for email in emails:
        local, domain = email.split("@")
        if "+" in local:
            local = local[:local.index("+")]
        seen.add(local.replace('.', '') + "@" + domain)            
    return print(len(seen))


numUniqueEmails(["test.email+alex@leetcode.com",
                 "test.e.mail+bob.cathy@leetcode.com",
                 "testemail+david@lee.tcode.com"])
