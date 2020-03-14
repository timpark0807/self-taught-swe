import secrets 

class Codec:
       
    """

    long2short = {url:hash}

    short2long = {hash:url} 

    long_url = https://leetcode.com/problems/design-tinyurl
    short_url = http://tinyurl.com/4e9iAk

    1. Take long url 
        ex: https://leetcode.com/problems/design-tinyurl

    2. Create a hash, associate that hash with the long url 
        ex: 4e9iAk

    3. 

    """
    def __init__(self):
        self.short2long = {}
        self.long2short = {} 
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        hashed_value = self.get_hashed_value(longUrl)
        self.short2long[hashed_value] = longUrl
        return "http://tinyurl.com/" + hashed_value 
    
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        hashed_value = shortUrl.split('/')[-1]
        return self.short2long[hashed_value]
        
    def get_hashed_value(self, longUrl):
        return secrets.token_hex(6)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
