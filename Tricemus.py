def TricemusСode(word,word_for_code):
    alphabet='абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
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
        code_vector[sector0[i]]=sector1[i]
        code_vector[sector1[i]]=sector2[i]
        code_vector[sector2[i]]=sector3[i]
        code_vector[sector3[i]]=sector0[i]

    return "".join([code_vector[sym] for sym in word_for_code ])


    for i in range(len(word_for_code)):
        word_for_code[i]
    


    return  sector0,sector1,sector2,sector3

print(TricemusСode("бандероль",'чемодан'))