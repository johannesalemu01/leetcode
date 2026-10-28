class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_str=address.replace(".","[.]")
        return new_str
        