def replace_word():
    str = 'Hola Juan Carlos, cómo estas chupapija, te voy a matar cuando vengas'
    word_to_replace = input('Ingresa la palabra a reemplazar: ')
    new_word = input('Ingresa la palabra nueva: ')
    print(str.replace(word_to_replace, new_word))
    

replace_word()