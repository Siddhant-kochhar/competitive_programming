class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = {"electronics":[], "grocery":[], "pharmacy":[], "restaurant":[]}
        final_result = []

        for i,j,z in zip(code,businessLine,isActive):
            #print(i,j,z)
            if z == True:
                if i and all(ch.isalnum() or ch == "_" for ch in i):

                    if j in ["electronics", "grocery", "pharmacy", "restaurant"]:
                            result[j].append(i)  

        for key,value in result.items():
            if value != []:
                final_result+= sorted(value)

        return ((final_result))