import twttr
from twttr import shorten
import sys
def main():
    test_str()


def test_str():
    try:
        assert shorten("twitter") == "twttr"
        assert shorten('TWITTER') == "TWTTR"
        assert shorten("Hello, World!") == "Hll, Wrld!"
        assert shorten("The quick brown fox jumps over the lazy dog") == "Th qck brwn fx jmps vr th lzy dg"
        assert shorten("aeiou") == ""
        assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
        assert shorten("12345abcd") == "12345bcd"
        assert shorten("This is a test!") == "Ths s  tst!"
    except AssertionError:
        sys.exit(1)
if __name__ == "__main__":
    main()


