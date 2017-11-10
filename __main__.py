import random

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

    ("wa", u"\u308F"),
    ("wo", u"\u3092"),
    ("n", u"\u3093"),

    ("ga", u"\u304C"),
    ("gi", u"\u304E"),
    ("gu", u"\u3050"),
    ("ge", u"\u3052"),
    ("go", u"\u3054"),

    ("za", u"\u3056"),
    ("ji", u"\u3058"),
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
    ("po", u"\u307D"),

    ("kya", u"\u304D\u3084"),
    ("sha", u"\u3057\u3084"),
    ("cha", u"\u3061\u3084"),
    ("nya", u"\u306B\u3084"),
    ("hya", u"\u3072\u3084"),
    ("mya", u"\u307F\u3084"),
    ("rya", u"\u308A\u3084"),
    ("gya", u"\u304E\u3084"),
    ("ja", u"\u3058\u3084"),
    ("bya", u"\u3073\u3084"),
    ("pya", u"\u3074\u3084"),

    ("kyu", u"\u304D\u3086"),
    ("shu", u"\u3057\u3086"),
    ("chu", u"\u3061\u3086"),
    ("nyu", u"\u306B\u3086"),
    ("hyu", u"\u3072\u3086"),
    ("myu", u"\u307F\u3086"),
    ("ryu", u"\u308A\u3086"),
    ("gyu", u"\u304E\u3086"),
    ("ju", u"\u3058\u3086"),
    ("byu", u"\u3073\u3086"),
    ("pyu", u"\u3074\u3086"),

    ("kyo", u"\u304D\u3088"),
    ("sho", u"\u3057\u3088"),
    ("cho", u"\u3061\u3088"),
    ("nyo", u"\u306B\u3088"),
    ("hyo", u"\u3072\u3088"),
    ("myo", u"\u307F\u3088"),
    ("ryo", u"\u308A\u3088"),
    ("gyo", u"\u304E\u3088"),
    ("jo", u"\u3058\u3088"),
    ("byo", u"\u3073\u3088"),
    ("pyo", u"\u3074\u3088"),
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

class Word:
    def __init__(self, english, japanese):
        self.english = english.lower()
        self.japanese = romaji_to_hiragana(japanese)

    def compare_english(self, value):
        return value.lower() == self.english

    def compare_japanese(self, value):
        return romaji_to_hiragana(value.lower()) == self.japanese

VOCABULARY = \
[
    Word("one", "ichi"),
    Word("two", "ni"),
    Word("three", "san"),
    Word("four", "yon"),
    Word("six", "roku"),
    Word("seven", "nana"),

    Word("good morning", "ohayou"),
    Word("good afternoon", "konnichiha"),
    Word("goodbye", "sayounara"),

    Word("yes", "hai"),
    Word("no", "iie"),

    Word("i", "watashi"),

    Word("white", "shiro"),
    Word("blue", "ao"),
    Word("red", "aka"),

    Word("dog", "inu"),
    Word("cat", "neko"),
    Word("bird", "tori"),

    Word("like", "suki"),
    Word("read", "yomu"),
    Word("wear", "kiru"),
    Word("drink", "nomu"),
    Word("want", "hoshii"),

    Word("vegetables", "yasai"),
    Word("alcohol", "osake"),
    Word("sweet", "amai"),
    Word("dirty", "kitanai"),

    Word("eye", "me"),
    Word("ear", "mimi"),
    Word("back", "senaka"),

    Word("cloudy", "kumori"),
    Word("sunny", "hare"),
    Word("winter", "fuyu"),
    Word("summer", "natsu"),
    Word("wind", "kaze"),

    Word("daytime", "hiru"),
    Word("night", "yoru"),

    Word("house", "ie"),
    Word("room", "heya"),
    Word("outside", "soto"),
    Word("bank", "ginkou"),

    Word("map", "chizu"),
    Word("bag", "kaban"),
]

def ask_user(question, correct_answer, answer_evaluation_callback):
    print(question, end=": ")

    answer = input()

    if answer:
        if answer_evaluation_callback(answer):
            print("Correct!")
            return True
        else:
            print("Wrong!")

    print("Correct answer:", correct_answer)
    return False

def english_to_japanese(word_obj):
    return ask_user(word_obj.english, word_obj.japanese, word_obj.compare_japanese)

def japanese_to_english(word_obj):
    return ask_user(word_obj.japanese, word_obj.english, word_obj.compare_english)

def use_random_ask_func(word_obj):
    random.choice([english_to_japanese, japanese_to_english])(word_obj)

if __name__ == "__main__":
    print("Available training modes:")
    print("1. English to Japanese")
    print("2. Japanese to English")
    print("\nSelected mode (default = both directions): ", end="")

    choice = input()
    print("")

    ask_func = \
        english_to_japanese if choice == "1" else \
        japanese_to_english if choice == "2" else \
        use_random_ask_func

    while True:
        ask_func(random.choice(VOCABULARY))
        print("")
