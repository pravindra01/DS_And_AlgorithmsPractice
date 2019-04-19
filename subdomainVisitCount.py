

class Solution(object):

    def getSubDomainVisitCount(self,countarr):
        _dict = {}
        retList = []
        for item in countarr:
            vals = str(item).split(" ")
            count = int(vals[0])
            domains = ""
            for subDomain in str(vals[1]).split(".")[::-1]:
                domains  = subDomain + domains
                if _dict.get(domains):
                    _dict[domains] += count
                else:
                    _dict[domains] = count
                domains = "." + domains
        for item in _dict.items():
            retList.append("%s %s"%(item[1], item[0]))
        return retList


if __name__ == "__main__":
    test = Solution()
    input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    #[('mail.com', 901), ('yahoo.com', 50), ('wiki.org', 5), ('google.mail.com', 900), ('intel.mail.com', 1), ('org', 5), ('com', 951)]
    #["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    ret = test.getSubDomainVisitCount(input)
    print ret
                