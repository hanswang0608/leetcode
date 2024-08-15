from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            localName, domainName = email.split('@')
            localNameChars = []
            for c in list(localName):
                if c == '+':
                    break
                elif c == '.':
                    continue
                else:
                    localNameChars.append(c)
            localName = ''.join(localNameChars)
            uniqueEmails.add(localName + '@' + domainName)
        return len(uniqueEmails)