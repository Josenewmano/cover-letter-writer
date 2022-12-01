import cover_letter


class TestCoverLetter:
    def test_returns_string(self):
        cl = cover_letter.CoverLetter()
        assert cl.write('') == ''
