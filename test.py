import streamlit as st
import random

st.title("🎲 오늘의 운세 점수 앱")

name = st.text_input("이름을 입력하세요")

warnings = [
    "지갑 잃어버리지 않게 조심하세요 💸",
    "말 한마디가 상처가 될 수 있어요 🗣️",
    "핸드폰 배터리 방전 주의! 🔋",
    "과식하지 않도록 조심하세요 🍔",
    "중요한 물건을 두고 나오지 않게 체크하세요 🔑",
    "길에서 천천히 다니세요 🚶",
    "과제 제출 깜빡하지 않게 주의하세요 📚",
]

if st.button("운세 뽑기!"):
    score = random.randint(0, 100)
    warning_msg = random.choice(warnings)

    st.write(f"✨ {name}님의 오늘의 점수는 {score}점 입니다!")
    if score > 80:
        st.success("오늘은 대박! 😎")
    elif score > 50:
        st.info("무난한 하루일 듯해요 🙂")
    else:
        st.warning("조심조심 하루 보내세요 🙏")

    st.write(f"⚠️ 오늘의 주의사항: {warning_msg}")

