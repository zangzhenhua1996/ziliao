TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。



```python
import string
import random
import math
letters=string.ascii_letters+string.digits  #获取的是62个英文字母加数字
full_tiny={}  #以长url为键以短url为值
tiny_full={} #以短url为键,以长url为值
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        def short_addr():
            ans=''
            tmp=''
            for i in range(6):
                tmp=letters[random.randint(0,61)] #随机的得到一个字符,这个地方一定要注意的是一定注意的是randint返回的之是0-61  恰好是62个.是包含最后一位的
                ans+=tmp
            return ans
        if longUrl  in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]  #返回编码后的短的Url
        else:
            suffix=short_addr() #得到一个六位的字符串
            full_tiny[longUrl] = suffix  #更新长转短
            tiny_full[suffix] = longUrl  #更新短转长
            return "http://tinyurl.com/" + suffix  #返回短Url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl=shortUrl.split('/')[-1]  #将短Url按照 '/' 进行分成列表并取最后一个元素
        if shortUrl  in tiny_full:  #如果这个短Url在字典中就返回
            return tiny_full[shortUrl]
        else: #反则就返回NOne
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```
