import itertools
import string

def generate_combinations(base_word, num_suffix_chars, output_file="combinations.txt"):
    charset = string.ascii_letters + string.digits + string.punctuation
    with open(output_file, "w", encoding="utf-8") as f:
        total = len(charset) ** num_suffix_chars
        print(f"Toplam {total} kombinasyon üretilecek. Lütfen bekleyin...")

        for suffix in itertools.product(charset, repeat=num_suffix_chars):
            word = base_word + ''.join(suffix)
            f.write(word + '\n')

    print(f"Tüm kombinasyonlar '{output_file}' dosyasına yazıldı.")

generate_combinations("41gel", 5, "5haneli.txt")
