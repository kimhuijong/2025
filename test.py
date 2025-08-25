import streamlit as st
import random
import streamlit as st
import random
import time

st.title("오늘의 운세 뽑기기계")

name = st.text_input("이름을 입력하세요")

warnings = [
    "지갑 잃어버리지 않게 조심하세요",
    "말 한마디가 상처가 될 수 있어요",
    "핸드폰 배터리 방전을 주의하세요",
    "과식하지 않도록 조심하세요",
    "중요한 물건을 두고 나오지 않게 확인하세요",
    "길에서 천천히 다니세요",
    "과제 제출을 깜빡하지 않도록 하세요",
]

lucky_items = [
    "파란 펜",
    "사탕",
    "책갈피",
    "물 한 잔",
    "헤드폰",
    "운동화",
    "초콜릿",
    "손수건",
]

if st.button("뽑기 돌리기!"):
    with st.spinner("뽑기기계가 돌아가는 중..."):
        time.sleep(2)  # 2초 기다림(돌아가는 효과)

    score = random.randint(0, 100)
    warning_msg = random.choice(warnings)
    lucky_item = random.choice(lucky_items)

    st.success(f"{name}님의 오늘의 점수는 {score}점 입니다!")

    if score > 80:
        st.write("오늘은 대박입니다!")
    elif score > 50:
        st.write("무난한 하루일 듯합니다.")
    else:
        st.write("조심조심 하루 보내세요.")

    st.write(f"오늘의 주의사항: {warning_msg}")
    st.write(f"오늘의 행운 아이템: {lucky_item}")
