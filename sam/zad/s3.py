def main():
    filename = 'input.txt'
    letters, words, lines = 0, 0, 0
    with open(filename, 'r') as file:
        for line in file:
            letters += len(line)
            words += len(line.split())
            lines += 1
    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')

if __name__ == '__main__':
    main()