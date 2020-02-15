class Solution(object):
    def __init__(self):
        self.singles = {'0':'', '1': 'One', '2': 'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight','9':'Nine'}
        self.teens = {'10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19':'Nineteen'}
        self.tens = {'0':'', '2':'Twenty', '3':'Thirty', '4':'Forty','5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
        self.place = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        string_num = str(num)
        chunks = self.get_chunks(string_num)   # Breaks numbers into chunks of 3 
        text_chunks = []
        for chunk in chunks: 
            text_chunk = self.get_text_chunk(chunk)
            text_chunks.append(text_chunk)
        
        retval_temp = self.insert_placeholder(text_chunks)
        retval = self.clean(retval_temp)
        return ' '.join(retval)

    def clean(self, retval):
        temp = ' '.join(retval)
        temp = temp.split(' ')
        ans = []
        for word in temp:
            if word != '':
                ans.append(word)
        return ans
        
    def insert_placeholder(self, text_chunks):        
        arr = []
        
        for index, chunk in enumerate(text_chunks):
            if chunk == [' ']:
                continue
            curr = ' '.join(chunk) + ' ' + self.place[index]
            arr.append(curr)
        return arr[::-1]
    
    def get_chunks(self, string_num):
        temp = ''
        arr = []
        
        for letter in string_num[::-1]:
            temp = letter + temp
            if len(temp) == 3:
                arr.append(temp)
                temp = ''
        if temp != '':
            arr.append(temp)
        return arr
    
    def get_text_chunk(self, chunk):
        """
        '87'
         ^ 
        
         temp = ['twenty', 'three']
        """
        temp = []
        print(chunk)

        if len(chunk) == 1:
            return [self.singles[chunk]]

        elif len(chunk) == 2:
            if chunk[0] == '1':
                return [self.teens[chunk]]
            teen = self.tens[chunk[0]]
            single = self.singles[chunk[1]]
            temp.append(teen)
            temp.append(single)

        elif len(chunk) == 3:
            if chunk[0] != '0':
                temp.append(self.singles[chunk[0]] + ' Hundred')
            if chunk[1] == '1':
                temp.append(self.teens[chunk[1:]])
            else:
                teen = self.tens[chunk[1]]
                single = self.singles[chunk[2]]
                temp.append(teen + ' ' + single)
        return temp 
    
