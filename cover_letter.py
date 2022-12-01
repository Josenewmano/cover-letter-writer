class CoverLetter:
    def __init__(self):
        pass

    def write(self, param):
        if param == '':
            return ''
        message = 'DISCLAIMER: If this reads like it was written by a computer, that is because it is. ' \
               'But all of the below is true, and I wrote the code that wrote it!' \
               'Check GitHub for the source code: https://github.com/Josenewmano/cover-letter-writer \n'
        if param == 'Ruby':
            message += 'I love the usability of Ruby, and it\'s the language that I wrote many of my early projects in'
        else:
            message += 'I think that Python is the future, and hopefully my future - Python wrote this for me after ' \
                             'all! '
        return message
