def censore(sentence):
	words = open('input1.txt','r').read().lower().split() #открываем файл и записываем все слова в список
	for word in words: #проходимся по всем словам в списке
		sentence = sentence.replace(word, '*'*len(word)) #если слово встречается в предложении, то заменяем его
	return sentence
print(censore(input())) #выводим предложение с замененными словами