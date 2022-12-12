import Ex58 as a

def test_compression():
    assert a.compression(a.decompression('ab3cd')) == 'ab3cd'
    assert a.compression(a.decompression('ab3c2d4efgh')) == 'ab3c2d4efgh'
    assert a.compression(a.decompression('abcdefg')) == 'abcdefg'
    assert a.compression(a.decompression('abcd2c')) == 'abcd2c'

def test_decompression():
    assert a.decompression('ab3cd') == "abcccd"
    assert a.decompression('ab3c2d4efgh') == 'abcccddeeeefgh'
    assert a.decompression('abcdefg') == 'abcdefg'
    assert a.decompression('abcd2c') == 'abcdcc'
