def is_equal_string(utf8_string, utf16_string):
    try:
        # Decode utf8_string and utf16_string to Unicode strings
        unicode_utf8 = utf8_string.decode('utf-8')
        unicode_utf16 = utf16_string.decode('utf-16')

        # Compare the Unicode strings
        return unicode_utf8 == unicode_utf16
    except UnicodeDecodeError:
        # Handle decoding errors (e.g., invalid encoding)
        return False

# Example usage:
utf8_str = b'This is a utf-8 string'
utf16_str = b'\xff\xfeT\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00a\x00 \x00u\x00t\x00f\x00-\x008\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00\x00\x00'

result = is_equal_string(utf8_str, utf16_str)
print(result)
