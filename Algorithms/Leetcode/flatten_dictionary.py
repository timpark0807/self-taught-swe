class Solution():
  def flatten_dict(self, dictionary):
    if not dictionary:
        return {}
    def flatten(dic):
        ret_dict = {}
        for key, value in dic.items():
          if isinstance(value, dict):
            for child_key, child_value in flatten(dic).items():
              ret_dict['{}.{}'.format(key, child_key)] = child_value
          else:
            ret_dict[key] = value
        return ret_dict
                   
    return flatten(dictionary)

d ={
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    
                }
            }
        }

s= Solution()
print(s.flatten_dict(d))
