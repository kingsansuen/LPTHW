class Lexicon(object):
    def scan(self, userinput):
        datas = userinput.split()
        output = []
        for item in datas:
            result = self.label(item)
            output.append(result)
        return[]

    def label(self, item):
        if item in ['norht' , 'south', 'east']:
            return ('direction', item)
        elif item in ['go' , 'kill', 'eat']:
            return ('verb', item)
        elif item in ['the' , 'in', 'of']:
            return ('stop', item)
        elif itmm in ['bear', 'princess']:
            return ('noun', item)
        else:
            try:
                number = int("item")
                return ('number', number)
            except ValueError:  ##type the error that you are expecting
                return ('error', item)
            
lexicon = Lexicon()
