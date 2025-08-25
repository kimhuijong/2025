import streamlit as st
import random
import streamlit as st
import random

st.title("오늘의 운세 앱")

# 메뉴 선택
menu = st.radio(
    "원하는 기능을 선택하세요:",
    ["점수 뽑기", "주의사항 보기", "행운 아이템 보기"]
)

# 데이터 준비
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

# 점수 랜덤 생성 (모든 기능에서 동일하게 쓰도록 session_state 활용)
if "score" not in st.session_state:
    st.session_state.score = random.randint(0, 100)

if "warning_msg" not in st.session_state:
    st.session_state.warning_msg = random.choice(warnings)

if "lucky_item" not in st.session_state:
    st.session_state.lucky_item = random.choice(lucky_items)


# 기능별 실행
if menu == "점수 뽑기":
    st.write(f"오늘의 점수는 {st.session_state.score}점 입니다.")
    if st.session_state.score > 80:
        st.success("오늘은 대박입니다!")
    elif st.session_state.score > 50:
        st.info("무난한 하루일 듯합니다.")
    else:
        st.warning("조심조심 하루 보내세요.")

elif menu == "주의사항 보기":
    st.write(f"오늘의 주의사항: {st.session_state.warning_msg}")

elif menu == "행운 아이템 보기":
    st.write(f"오늘의 행운 아이템: {st.session_state.lucky_item}")

   
    
