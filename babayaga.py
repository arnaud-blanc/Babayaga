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
    simple_lower = "a b v g d ié io j z i ï k l m n o p r s t ou f kh ts tch ch chtch y iou ia ʺ ʹ è".split(' ')
    simple_capitalized = list(map(lambda phoneme: phoneme.capitalize(), simple_lower))
    simple_latin = simple_lower + simple_capitalized
    #latin_simple = " ".join([simple_lower, simple_lower.upper()]).split(" ")
    
    trans_dic = {key: {"ISO 9": value1, 'sans diacritiques': value2} for key, value1, value2 in zip(cyrillic_alphabet, latin_translitteration, simple_latin)}

    for character in text:
        if character in trans_dic:
            text = text.replace(character, trans_dic[character][genre])
    
    return text


texte_latin = translitteration(txt, genre)

st.download_button('Télécharger :', texte_latin)
result = st.text(texte_latin) 

