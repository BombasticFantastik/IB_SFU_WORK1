def TricemusСode(word,word_for_code):

    word=word.lower()
    word_for_code=word_for_code.lower()
    #print(word,word_for_code)

    alphabet='абвгдежзийклмнопрстуфхцчшщъыьэюя'

    #проверка на алфавит
    for symb in word:
        if symb not in alphabet:
            return "Для кодирования допускаются слова состоящие только из букв русского алфавита"
        
    for symb in word_for_code:
        if symb not in alphabet:
            return "Для кодирования допускаются слова состоящие только из букв русского алфавита"

    
    #деление на символы
    new_word=''
    new_word=[symb for symb in word if symb not in new_word]
    

    #удаление букв из алфавита
    for symb in new_word:
        alphabet=alphabet.replace(symb,'')
        
    #создание массивов букв
    new_word=''.join(new_word)+alphabet
    sector0=new_word[0:8]
    sector1=new_word[8:16]
    sector2=new_word[16:24]
    sector3=new_word[24:32]

    #создание  словаря 
    code_vector={}
    for i in range(8):
        code_vector[sector0[i]]=sector1[i]
        code_vector[sector1[i]]=sector2[i]
        code_vector[sector2[i]]=sector3[i]
        code_vector[sector3[i]]=sector0[i]

    return "".join([code_vector[sym] for sym in word_for_code ])



#тоже самое но обратная функция
def BackTricemusСode(word,word_for_code):
    word=word.lower()
    word_for_code=word_for_code.lower()

    alphabet='абвгдежзийклмнопрстуфхцчшщъыьэюя'

    #проверка на алфавит
    for symb in word:
        if symb not in alphabet:
            return "Для кодирования допускаются слова состоящие только из букв русского алфавита"
        
    for symb in word_for_code:
        if symb not in alphabet:
            return "Для кодирования допускаются слова состоящие только из букв русского алфавита"
    
    new_word=''
    new_word=[symb for symb in word if symb not in new_word]
    

    
    for symb in new_word:
        alphabet=alphabet.replace(symb,'')
    
    new_word=''.join(new_word)+alphabet

    sector0=new_word[0:8]
    sector1=new_word[8:16]
    sector2=new_word[16:24]
    sector3=new_word[24:32]

    code_vector={}
    for i in range(8):
        code_vector[sector0[i]]=sector3[i]
        code_vector[sector1[i]]=sector0[i]
        code_vector[sector2[i]]=sector1[i]
        code_vector[sector3[i]]=sector2[i]

    return "".join([code_vector[sym] for sym in word_for_code ])