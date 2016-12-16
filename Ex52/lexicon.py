class Lexicon(object):
    def scan(self, userinput):
        datas = userinput.split()
        output = []
        for item in datas:
            result = self.label(item)
            output.append(result)
        return output

    def label(self, item):
        if item in ['tell' , 'joke', 'telling', 'joking', 'Telling', 'Joking', 'TELLING', 'JOKING', 'TELL', 'JOKE']:
            return ('tell a joke', item)
        elif item in ['shoot', 'shoot!', 'Shoot', 'SHOOT', 'SHOOT!']:
            return ('shoot!', item)
        elif item in ['dodge', 'dodge!', 'Dodge', 'DODGE', 'DODGE!']:
            return ('dodge!', item)
        elif item in ['throw' , 'thorowing', 'Throw', 'THROW']:
            return ('throw the bomb', item)
        elif item in ['slowly', 'Slowly', 'place', 'Place', "SLOWLY", 'PLACE', 'setup', 'SETUP']:
            return ('slowly place the bomb', item)
        else:
            try:
                self.number = int(item)
                return ('number', self.number)
            except ValueError:  ##type the error that you are expecting
                return ('error', item)

    def output(self, userinput):
        result = self.scan(userinput)
        x = 0
        while x<len(result):
            if 'shoot!' in result[x]:
                return 'shoot!'
            elif 'dodge!' in result[x]:
                return 'dodge!'
            elif 'tell a joke' in result[x]:
                return 'tell a joke'
            elif 'slowly place the bomb' in result[x]:
                return 'slowly place the bomb'
            elif 'number' in result[x]:
                return self.number
            x+=1


lexicon = Lexicon()
