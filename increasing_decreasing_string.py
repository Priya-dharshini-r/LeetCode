class Solution:
    def sortString(self, s: str) -> str:
        sorted_str = "".join(sorted(s))
        my_dict = {}
        for i in sorted_str:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i] = 1
        empty_str = ""  
        while len(s) != len(empty_str):
            for key, value in my_dict.items():
                if value != 0:
                    empty_str = empty_str + key
                    my_dict[key] = value - 1
        
            for key, value in reversed(my_dict.items()):
                if value != 0:
                    empty_str = empty_str + key
                    my_dict[key] = value - 1
            
        return empty_str
        
