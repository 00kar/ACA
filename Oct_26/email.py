def isValid(email):
    value = True
    invalidCharacters = "123457890)(][}{><,?/\:;'\"|~`!#$%^&*-_= "
    for sign in invalidCharacters:
        if sign in email:
            value = False
            break
    if (email.startswith("+")) or (not email.islower())or (email.count("@") != 1):
        value = False
    else:
        domainName = email[email.index("@")+1:]
        if domainName.count(".") < 1:
            value = False
    return value



class Solution:
    def numUniqueEmails(self, emails):
        validEmails = []
        for email in emails:
            if isValid(email):
                localName = email[:email.index("@")]
                domainName = email[email.index("@")+1:]
                if '+' in localName:
                    localName = localName[:localName.index('+')]
                localName = localName.replace(".", "", localName.count('.'))
                email = localName + '@' + domainName
                validEmails.append(email)
        finalEmails = []
        for email in validEmails:
            if email not in finalEmails:
                finalEmails.append(email)
        return len(finalEmails)




length = int(input("Enter count of items in list\t"))
emails = []
for i in range(length):
    emails.append(input())

a = Solution()
count = a.numUniqueEmails(emails)
print(count)