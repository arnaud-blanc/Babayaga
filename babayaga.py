import streamlit as st

with open('style.css') as style:
    st.markdown(f"<style>{style.read()}</style>",unsafe_allow_html=True)

st.title('Baba Yaga -  Баба Яга')

txt = st.text_area("texte à utiliser")

genre = st.radio(
     "Type de translittération :",
     ('ISO 9', 'sans diacritiques'), horizontal=True)

def translitteration(text: str, genre: str)->str:
    """Transliterates Russian text with Latin characters

    Args:
        text (str): text on which transliteration is applied
        genre (str): type of transliteration

    Returns:
        str: transliterated text
    """
    cyrillic_alphabet = "абвгдеёжзийклмнопрстуфхцчшщыюяъьэАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЮЯЪЬЭ"
    latin_translitteration = "abvgdeëžzijklmnoprstufhcčšŝyûâʺʹèABVGDEËŽZIJKLMNOPRSTUFHCČŠŜYÛÂʺʹÈ"
    simple_lower = "a b v g d ié io j z i ï k l m n o p r s t ou f kh ts tch ch chtch y iou ia ʺ ʹ è"
    latin_simple = " ".join([simple_lower, simple_lower.upper()]).split(" ")
    
    trans_dic = {key: {"ISO 9": value1, 'sans diacritiques': value2} for key, value1, value2 in zip(cyrillic_alphabet, latin_translitteration, latin_simple)}

    for character in text:
        if character in trans_dic:
            text = text.replace(character, trans_dic[character][genre])
    
    return text


texte_latin = translitteration(txt, genre)

st.download_button('Télécharger :', texte_latin)
result = st.text(texte_latin) 

#"""
#Жил, был король когда-то
#При нём блоха жила
#Блоха ! Блоха !
#Милей родного брата
#Она ему была
#Блоха, ха, ха, ха, ха, ха. Блоха
#Ха, ха, ха, ха, ха. Блоха !
#
#Зовёт король портного
#— Послушай, ты, чурбан
#Для друга дорогого
#Сшей бархатный кафтан !
#Блохе кафтан ? Ха, ха, ха, ха, ха, ха
#Блохе ? Ха, ха, ха, ха, ха. Кафтан !
#Ха, ха, ха, ха, ха. Ха, ха, ха, ха, ха
#Блохе кафтан?
#Чтоб жарко и парко блоха моя жила
#И полная свобода ей при дворе дана
#При дворе хе-хе-хе-хе-хе блохе ха-ха-ха
#Ха-ха-ха-ха-ха-ха блохе
#
#Король ей сан министра и с ним звезду даёт
#И с нею и другие пошли все блохи в ход а-ха
#И самой Королеве и фрейлинам ея
#От блох не стало мочи, не стало и житья ха-ха
#
#И тронуть-то боятся не то чтобы их бить
#А мы, кто стал кусаться, тотчас давай душить
#Ха-ха-ха-ха-ха ха-ха-ха
#Ха-ха-ха-ха-ха ха-ха-ха-ха
#А а-ха-ха ха-ха
#"""

#print(translitteration(text))
#wprint(translitteration("Блохе кафтан?").split(' '))