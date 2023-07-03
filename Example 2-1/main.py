# Build a list of Unicode code points from string

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)