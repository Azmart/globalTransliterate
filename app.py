import streamlit as st
import streamlit.components.v1 as components

from logger import logger
from languages import supported_languages
from transliterator import detect_source_language, transliterate

def main():
    """Entry point"""

    st.set_page_config(page_title="howdoiwrite.ai", page_icon=":studio_microphone:")

    main_container = st.container()
    left_column, right_column = main_container.columns(2)
    
    st.sidebar.title("ट्रान्सफार्मर स्थापत्यमा आधारित भाषा अव्याख्याणिक मोडेल: ३० भन्दा बढि भाषामा।")
    st.sidebar.title("Lipi 1.1: Transformer Based Architecture For Language Transliteration: In Over 30 languages")
    st.sidebar.title("基于变压器的架构 对于语言音译： 支援 30 多種語言")

    left_column.title("How do I write...")

    source_text = left_column.text_area(
        "Text",
        placeholder="Type your text here...",
        max_chars=1000,
        key="source_text",
        label_visibility="hidden",
    )

    st.session_state.source_lang = detect_source_language(source_text)

    left_column.write(f"**Detected source language**: {st.session_state.source_lang} :thumbsup:")

    right_column.title("Transliterate")

    destination_language = right_column.selectbox(
        "Select Language",
        sorted(list(supported_languages.keys())[1:]),
        key="target_lang",
        label_visibility="hidden",
    )

    logger.debug(f"Selected destination language as {destination_language}")

    right_column.button("Transliterate", on_click=transliterate, type="primary", use_container_width=True)

    right_column.divider()

    if "transliteration" not in st.session_state:
        st.session_state.transliteration = ""

    right_column.markdown(f"**{st.session_state.transliteration}**")

    if st.session_state.transliteration:
        right_column.audio("transliteration.mp3", format="audio/mp3")
        st.divider()

        # footer_left, footer_right = st.columns(2)
        # footer_left.markdown(
        #     "**You can find the code on my [GitHub](https://github.com/coskundeniz) page.**"
        # )

        # with footer_right:
        #     footer_right.write("**If you like this app, please consider to**")
        #     components.html(
        #         '<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="coskundeniz" data-color="#ff7800" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#FFDD00" ></script>'
        #     )

if __name__ == "__main__":
    main()
