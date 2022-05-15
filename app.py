import streamlit as st
import pandas as pd

from urllib.error import URLError
st.set_page_config(page_title="อีซี่ฉันท์", page_icon="https://i.ibb.co/qxXxXxq/logo.png")
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@500&display=swap');

			html, body, [class*="css"]  {
			font-family: 'IBM Plex Sans Thai', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.title("อีซี่ฉันท์")
st.caption("เพราะการแต่งฉันท์มันยาก อีซี่ฉันท์จึงช่วยหาคำที่ตรงตามฉันทลักษณ์ให้คุณ")

df = pd.read_csv("word-rhythm.csv").drop(columns=["Unnamed: 0"])

rhythms = st.multiselect(
    "เลือกลำดับคำ ครุ-ลหุ ที่ต้องการ", ['ครุ','ครุ','ครุ','ครุ','ลหุ','ลหุ','ลหุ','ลหุ'] , ["ลหุ", "ครุ", "ครุ"]
)
if not rhythms:
    st.error("เลือกลำดับคำ ครุ-ลหุ ที่ต้องการอย่างน้อย 1 คำ")
else:
    pattern = ''.join(rhythms)
    pattern = pattern.replace('ครุ', '-')
    pattern = pattern.replace('ลหุ', '.')
    data = df[df['rhythm'] == (pattern)]
    st.write("### รายการคำ", data.sort_values(by=['frequency'], ascending=False).drop(columns=['rhythm','pronunciation'], axis=1).reset_index(drop=True))


