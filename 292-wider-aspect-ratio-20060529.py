def get_wider_aspect_ratio(a, b):
    w1, h1 = map(int, a.split('x'))
    w2, h2 = map(int, b.split('x'))

    if w1 * h2 >= w2 * h1:
        w, h = w1, h1
    else:
        w, h = w2, h2

    # Berechne den größten gemeinsamen Teiler (GGT) von Breite und Höhe
    # mit dem euklidischen Algorithmus, damit das Seitenverhältnis
    # anschließend auf die kleinsten ganzen Zahlen gekürzt werden kann.
    a, b = w, h
    while b != 0:
        rest = a % b
        a = b
        b = rest
        
    ggt = a

    return f"{w // ggt}:{h // ggt}"

print(get_wider_aspect_ratio("1920x1080", "800x600"))

"""
Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height ratio.

The given strings will be in the format "WxH", for example, "1920x1080".
The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces to "16:9".
Return a string in format "W:H", for example, "16:9".
Tests:
Passed:1. get_wider_aspect_ratio("1920x1080", "800x600") should return "16:9".
Passed:2. get_wider_aspect_ratio("1080x1350", "2048x1536") should return "4:3".
Passed:3. get_wider_aspect_ratio("640x480", "2440x1220") should return "2:1".
Passed:4. get_wider_aspect_ratio("360x640", "1080x1920") should return "9:16".
Passed:5. get_wider_aspect_ratio("3440x1440", "2048x858") should return "43:18".
Passed:6. get_wider_aspect_ratio("12345x61234", "12534x51234") should return "2089:8539".
"""
