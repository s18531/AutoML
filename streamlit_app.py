import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
#st.balloons() # animowane balony ;)
#st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

st.spinner()
with st.spinner(text='Pracuję...'):
    time.sleep(2)
    st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

#st.title('Zajęcia 1. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

#st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

#st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

#st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

#st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

#st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

#with st.echo():
    #st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

#df = pd.read_csv("cwiczenie_1.csv", sep = ';')
#st.dataframe(df)
# musimy tylko pamiętaćo właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('ENG-GER TRANSLATOR')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Drut kolczasty w gardle translator (GER)"
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

if option == "Drut kolczasty w gardle translator (GER)":
    st.write("Please type your word/sentence in text field. Algorithm tries to translate this to German")
    text = st.text_area(label="Wpisz tekst")
    if text:
        translator = pipeline("translation_en_to_de")
        st.spinner()
        with st.spinner():
            answer = ""
            while len(answer) == 0:
                st.spinner(text="Translation in progress")
                answer = translator(text)
            if 'ValueError' in answer:
                st.error(text = "Something went wrong!")
            else:
                st.success("Translated")
                st.balloons()
                st.write(answer)

st.success("Mateusz Augustyniak s18531")



st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?') #done
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja') #done
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.') 
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
