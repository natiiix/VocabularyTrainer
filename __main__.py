ROMAJI_HIRAGANA_TABLE = \
    [
        ("a", u"\u3042"),
        ("i", u"\u3044"),
        ("u", u"\u3046"),
        ("e", u"\u3048"),
        ("o", u"\u304A"),

        ("ka", u"\u304B"),
        ("ki", u"\u304D"),
        ("ku", u"\u304F"),
        ("ke", u"\u3051"),
        ("ko", u"\u3053"),

        ("sa", u"\u3055"),
        ("shi", u"\u3057"),
        ("su", u"\u3059"),
        ("se", u"\u305B"),
        ("so", u"\u305D"),

        ("ta", u"\u305F"),
        ("chi", u"\u3061"),
        ("tsu", u"\u3064"),
        ("te", u"\u3066"),
        ("to", u"\u3068"),

        ("na", u"\u306A"),
        ("ni", u"\u306B"),
        ("nu", u"\u306C"),
        ("ne", u"\u306D"),
        ("no", u"\u306E"),

        ("ha", u"\u306F"),
        ("hi", u"\u3072"),
        ("fu", u"\u3075"),
        ("he", u"\u3078"),
        ("ho", u"\u307B"),

        ("ma", u"\u307E"),
        ("mi", u"\u307F"),
        ("mu", u"\u3080"),
        ("me", u"\u3081"),
        ("mo", u"\u3082"),

        ("ya", u"\u3084"),
        ("yu", u"\u3086"),
        ("yo", u"\u3088"),

        ("ra", u"\u3089"),
        ("ri", u"\u308A"),
        ("ru", u"\u308B"),
        ("re", u"\u308C"),
        ("ro", u"\u308D"),

        ("n", u"\u3093"),

        ("ga", u"\u304C"),
        ("gi", u"\u304E"),
        ("gu", u"\u3050"),
        ("ge", u"\u3052"),
        ("go", u"\u3054"),

        ("za", u"\u3056"),
        ("zi", u"\u3058"),
        ("zu", u"\u305A"),
        ("ze", u"\u305C"),
        ("zo", u"\u305E"),

        ("da", u"\u3060"),
        ("di", u"\u3062"),
        ("du", u"\u3065"),
        ("de", u"\u3067"),
        ("do", u"\u3069"),

        ("ba", u"\u3070"),
        ("bi", u"\u3073"),
        ("bu", u"\u3076"),
        ("be", u"\u3079"),
        ("bo", u"\u307C"),

        ("pa", u"\u3071"),
        ("pi", u"\u3074"),
        ("pu", u"\u3077"),
        ("pe", u"\u307A"),
        ("po", u"\u307D")
    ]

def replace_symbols(text, source_idx, target_idx):
    result = []

    while text:
        symbol = None
        length = 0

        for x in ROMAJI_HIRAGANA_TABLE:
            x_len = len(x[source_idx])
            if x_len > length and text.startswith(x[source_idx]):
                symbol = x[target_idx]
                length = x_len

        if not symbol:
            symbol = text[0]
            length = 1

        result.append(symbol)
        text = text[length:]

    return u"".join(result)

def romaji_to_hiragana(romaji_text):
    return replace_symbols(romaji_text, 0, 1)

def hiragana_to_romaji(hiragana_text):
    return replace_symbols(hiragana_text, 1, 0)

if __name__ == "__main__":
    print(hiragana_to_romaji(u"ひらがな"))
    print(romaji_to_hiragana("hiragana"))
