import socket


def generate_omissions(name):
    variants = set()

    for i in range(len(name)):
        typo = name[:i] + name[i+1:]
        variants.add(typo)

    return variants


def generate_repetitions(name):
    variants = set()

    for i in range(len(name)):
        double_letter = name[i] * 2
        typo = name[:i] + double_letter + name[i+1:]
        variants.add(typo)

    return variants


def generate_swaps(name):
    variants = set()

    for i in range(len(name) - 1):
        chars = list(name)
        chars[i], chars[i+1] = chars[i+1], chars[i]
        variants.add("".join(chars))

    return variants


def generate_keyboard_substitutions(name):
    variants = set()

    keyboard_map = {
        'a': ['q', 'w', 's', 'z'],
        'b': ['v', 'g', 'h', 'n'],
        'c': ['x', 'd', 'f', 'v'],
        'd': ['s', 'e', 'r', 'f', 'c', 'x'],
        'e': ['w', 'r', 's', 'd'],
        'f': ['d', 'r', 't', 'g', 'v', 'c'],
        'g': ['f', 't', 'y', 'h', 'b', 'v'],
        'h': ['g', 'y', 'u', 'j', 'n', 'b'],
        'i': ['u', 'o', 'k', 'j'],
        'j': ['h', 'u', 'i', 'k', 'm', 'n'],
        'k': ['j', 'i', 'o', 'l', 'm'],
        'l': ['k', 'o', 'p'],
        'm': ['n', 'j', 'k'],
        'n': ['b', 'h', 'j', 'm'],
        'o': ['i', 'p', 'k', 'l'],
        'p': ['o', 'l'],
        'q': ['w', 'a'],
        'r': ['e', 't', 'd', 'f'],
        's': ['a', 'w', 'e', 'd', 'x', 'z'],
        't': ['r', 'y', 'f', 'g'],
        'u': ['y', 'i', 'h', 'j'],
        'v': ['c', 'f', 'g', 'b'],
        'w': ['q', 'e', 'a', 's'],
        'x': ['z', 's', 'd', 'c'],
        'y': ['t', 'u', 'h', 'g'],
        'z': ['a', 's', 'x']
    }

    for i, char in enumerate(name):
        if char in keyboard_map:
            for neighbour in keyboard_map[char]:
                typo = name[:i] + neighbour + name[i+1:]
                variants.add(typo)

    return variants


def generate_homoglyphs(name):
    variants = set()

    glyph_map = {
        'a': ['а', 'à', 'á'],
        'b': ['Ь', 'ƀ'],
        'c': ['с', 'ċ', 'ç'],
        'd': ['ԁ', 'đ'],
        'e': ['е', 'ė', 'ę'],
        'f': ['f', 'ƒ'],
        'g': ['ց', 'ġ', 'ğ'],
        'h': ['հ', 'ħ'],
        'i': ['і', 'í', 'ï', '1'],
        'j': ['ј', 'ĵ'],
        'k': ['ｋ', 'ķ'],
        'l': ['1', 'ı', 'ł'],
        'm': ['ṃ', 'm̂'],
        'n': ['ո', 'ñ'],
        'o': ['о', 'ȯ', 'ọ', '0'],
        'p': ['р', 'þ'],
        'q': ['ｑ', 'q̇'],
        'r': ['г', 'ŕ', 'ŗ'],
        's': ['ѕ', 'ś', 'ş'],
        't': ['ʇ', 'ţ', 'τ'],
        'u': ['у', 'ú', 'ü'],
        'v': ['ѵ', 'ν'],
        'w': ['ԝ', 'ŵ'],
        'x': ['х', 'ẋ'],
        'y': ['у', 'ý', 'ÿ'],
        'z': ['ʐ', 'ż', 'ž']
    }

    for i, char in enumerate(name):
        if char in glyph_map:
            for twin in glyph_map[char]:
                typo = name[:i] + twin + name[i+1:]
                variants.add(typo)

    return variants


def check_dns(domain):
    try:
        socket.setdefaulttimeout(2)
        ip = socket.gethostbyname(domain)
        return f"ACTIVE (IP: {ip})"
    except socket.error:
        return "INACTIVE"


def main(target, tld="com"):
    print(f"Extracting permutations for: {target}.{tld}\n")

    pool = set()
    pool |= generate_omissions(target)
    pool |= generate_repetitions(target)
    pool |= generate_swaps(target)
    pool |= generate_keyboard_substitutions(target)
    pool |= generate_homoglyphs(target)

    print(f"Total unique variations: {len(pool)}")
    print(f"\n Scanning first 15 results...\n")
    print("-" * 60)

    for variant in sorted(pool)[:15]:
        full_domain = f"{variant}.{tld}"
        status = check_dns(full_domain)
        print(f"{full_domain:<25} | {status}")

    print("-" * 60)


if __name__ == "__main__":
    target = input("Enter domain (without TLD): ")
    main(target)
