class FileSystem(object):

    def __init__(self):
        self.root = {} 
        

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path == '/':
            return sorted([key for key in self.root.keys()])
            
        p = path.split('/')
        curr = self.root
        for path in p[1:]:
            curr = curr[path]
            
        if 'file' not in curr:
            return sorted([key for key in curr.keys()])
        else:
            return [p[-1]]
        
    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        p = path.split('/')
        curr = self.root 
        for folder in p[1:]:
            if folder not in curr:
                curr[folder] = {}
            curr = curr[folder] 
            
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        filePath = filePath.split('/')
        curr = self.root
        
        for path in filePath[1:]:
            if path not in curr:
                curr[path] = {}
            curr = curr[path] 
            
        if 'file' not in curr:
            curr['file'] = [content]
        else:
            curr['file'].append(content)
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        filePath = filePath.split('/')
        curr = self.root 
        
        for path in filePath[1:]:
            curr = curr[path]
        return ''.join(curr['file'])

        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
