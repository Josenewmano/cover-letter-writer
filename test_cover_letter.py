from cover_letter import CoverLetter


class TestCoverLetter:
    def test_empty_string_returns_empty_string(self):
        cl = CoverLetter()
        assert cl.write('') == ''

    def test_ruby_returns_ruby_and_disclaimer(self):
        cl = CoverLetter()
        assert cl.write(
            'Ruby') == 'DISCLAIMER: If this reads like it was written by a computer, that is because it is. ' \
                       'But all of the below is true, and I wrote the code that wrote it!' \
                       'Check GitHub for the source code: https://github.com/Josenewmano/cover-letter-writer \n' \
                       'I love the usability of Ruby, and it\'s the language that I wrote many of my early projects in'

    def test_python_returns_python_and_disclaimer(self):
        cl = CoverLetter()
        assert cl.write(
            'Python') == 'DISCLAIMER: If this reads like it was written by a computer, that is because it is. ' \
                         'But all of the below is true, and I wrote the code that wrote it!' \
                         'Check GitHub for the source code: https://github.com/Josenewmano/cover-letter-writer \n' \
                         'I think that Python is the future, and hopefully my future - Python wrote this for me after '\
                         'all! '
