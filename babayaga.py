import streamlit as st

st.set_page_config(
    page_title="babayaga",
    page_icon="Images/favicon.ico",
    layout="centered",
)

with open("style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

st.title("Baba Yaga 🧙‍♀️ Баба Яга")

st.write(
    """***Baba Yaga*** signifie « Sorcière » en russe.
         
L'idée m'est venue de tester Streamlit en créant une minuscule application de translittération.
En plus de me former au sciences des données, je suis chanteur lyrique et je commence à 🎶 chanter le répertoire russe 🎶.

L'application transforme les caractères *cyrilliques* en caractères *latins*.

Essayez en copiant-collant la cellule suivante ! ⤵️"""
)

st.code(
    """Это приложение транслитерации все еще рудиментарно! 
Причина его существования - любопытство.
Я быстро закодировал его, чтобы познакомиться со Streamlit 🚀.
Он будет развиваться вместе с моими открытиями в области искусственного интеллекта и моим пристрастием к обработке естественного языка (NLP).
Я также пойду дальше, научившись использовать FastApi и кодировать кириллическую клавиатуру 😉.
У меня много идей...

Переведено с помощью www.DeepL.com/Translator (бесплатная версия)"""
)

st.markdown("[📚    traduction  ⁉️](https://link.infini.fr/translation_for_the_curious)")

with st.form("my_form", clear_on_submit=True):
    txt = st.text_area(
        "Texte russe à translittérer :",
        placeholder="Здравствуй мир!",
        key="russian_text",
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button(
        "🪄", help="translittérer / effacer la translittération"
    )

genre = st.radio(
    "Type de translittération :", ("ISO 9", "sans diacritiques"), horizontal=True
)


def translitteration(text: str, genre: str) -> str:
    """Transliterates Russian text with Latin characters

    Args:
        text (str): text on which transliteration is applied
        genre (str): type of transliteration

    Returns:
        str: transliterated text
    """
    cyrillic_alphabet = (
        "абвгдеёжзийклмнопрстуфхцчшщыюяъьэАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЮЯЪЬЭ"
    )
    # ISO 9 version :
    latin_translitteration = (
        "abvgdeëžzijklmnoprstufhcčšŝyûâʺʹèABVGDEËŽZIJKLMNOPRSTUFHCČŠŜYÛÂʺʹÈ"
    )
    # lowercase version whitout diacritics :
    simple_lower = "a b v g d ié io j z i ï k l m n o p r s t ou f kh ts tch ch chtch y iou ia ʺ ʹ è".split(
        " "
    )
    # Capitalized version whitout diacritics :
    simple_capitalized = list(map(lambda phoneme: phoneme.capitalize(), simple_lower))

    simple_latin = simple_lower + simple_capitalized

    # transliteration dictionnary :
    trans_dic = {
        key: {"ISO 9": value1, "sans diacritiques": value2}
        for key, value1, value2 in zip(
            cyrillic_alphabet, latin_translitteration, simple_latin
        )
    }

    # replace cyrillic characters:
    for character in text:
        if character in trans_dic:
            text = text.replace(character, trans_dic[character][genre])

    return text


texte_latin = translitteration(txt, genre)

if txt:
    st.download_button(
        "Télécharger :",
        texte_latin,
        help="La translittération sera téléchargée au format texte.",
    )
    st.code(texte_latin, language=None)
