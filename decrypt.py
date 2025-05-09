import hashlib

def find_matching_wordlist_entry(wordlist_file, target_sha1):
    found = False

    with open(wordlist_file, "r", encoding="utf-8") as f, \
         open("found.txt", "w", encoding="utf-8") as found_file, \
         open("not_found.txt", "w", encoding="utf-8") as not_found_file:

        for line in f:
            word = line.strip()
            hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()

            if hashed_word.lower() == target_sha1.lower():
                print(f"[EŞLEŞME] {word} -> {hashed_word}")
                found_file.write(f"{word} -> {hashed_word}\n")
                found = True
            else:
                not_found_file.write(f"{word} -> {hashed_word}\n")

    if not found:
        print("Hiçbir eşleşme bulunamadı.")
    else:
        print("Eşleşmeler 'found.txt' dosyasına, diğerleri 'not_found.txt' dosyasına yazıldı.")

# Örnek kullanım:
# find_matching_wordlist_entry("sifreler.txt", "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")

find_matching_wordlist_entry("4haneli.txt", "0c2eafac73156d508bb28e3bedba57d6cbe7482e")
