#38 Напишите программу, удаляющую из текста все слова содержащие "абв". 

text = 'Всё дабвц зависит цвабв от нас самих! ыкабв Ничего в мире уцфыабв нет такого, что дллаовылаабв не подвластно было б нам!'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(text)
print(my_text)
