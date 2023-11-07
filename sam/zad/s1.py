def main():
    with open("words.txt", encoding="utf8") as file:
        text = file.read()
        words = text.split()
        word_count = {word: words.count(word) for word in set(words)}
        max_count = max(word_count, key=word_count.get)

    print(f"Самое частое слово: {max_count}, количество: {word_count[max_count]}")

if __name__ == "__main__":
    main()

