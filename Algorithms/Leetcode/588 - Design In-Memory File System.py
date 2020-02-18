class FileSystem(object):

    def __init__(self):
        self.root = {}
        

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        temp = path.split('/')
        curr = self.go_to(temp[1:])
        if type(curr) == unicode:
            return [temp[-1]]
        return sorted(list(curr.keys()))

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        curr = self.root
        split_path = path.split('/')[1:]
        
        for directory in split_path:
            if directory not in curr:
                curr[directory] = {}

            curr = curr[directory]
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        temp = filePath.split('/')
        curr = self.go_to(temp[1:-1])
        if temp[-1] not in curr:
            curr[temp[-1]] = ''
        curr[temp[-1]] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        temp = filePath.split('/')
        curr = self.go_to(temp[1:-1])
        return curr[temp[-1]]
    
    def go_to(self, path):
        if len(path) == 1 and path[0] == '':
            return self.root
        
        curr = self.root
        for directory in path:
            curr = curr[directory]
        return curr

# 
