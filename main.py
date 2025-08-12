import streamlit as st
import random

# MBTI 데이터
MBTI_DATA = {
    "INTJ": {"emoji": "🧠", "title": "마스터 전략가", "desc": "냉철한 계획가 - 큰 그림과 시스템 설계에 능해요."},
    "INTP": {"emoji": "🔬", "title": "논리 탐구자", "desc": "아이디어 실험실 - 이론과 개념을 파헤치길 좋아해요."},
    "ENTJ": {"emoji": "🏳️", "title": "카리스마 리더", "desc": "목표 지향적 리더 - 팀을 끌고 결과를 만들어내요."},
    "ENTP": {"emoji": "💡", "title": "아이디어 폭발가", "desc": "토론과 창의적 발상으로 분위기를 띄워요."},
    "INFJ": {"emoji": "💭", "title": "꿈꾸는 철학자", "desc": "깊은 통찰과 공감으로 의미를 찾는 타입이에요."},
    "INFP": {"emoji": "🌱", "title": "이상주의자", "desc": "가치 중심의 감성가 - 자신만의 세계관을 소중히 해요."},
    "ENFJ": {"emoji": "🌟", "title": "매력적인 촉진자", "desc": "사람을 돕고 동기를 부여하는데 능해요."},
    "ENFP": {"emoji": "⚡", "title": "에너지 뿜뿜", "desc": "호기심 많고 열정적인 사람 - 가능성을 즐겨 찾아요."},
    "ISTJ": {"emoji": "📏", "title": "완벽주의자", "desc": "신중하고 책임감이 강한, 규칙을 잘 지키는 타입이에요."},
    "ISFJ": {"emoji": "🛡️", "title": "다정한 수호자", "desc": "섬세하고 헌신적 - 주변을 돌보는 일을 잘해요."},
    "ESTJ": {"emoji": "⚖️", "title": "실무 관리자", "desc": "조직을 운영하고 효율을 만드는 데 능숙해요."},
    "ESFJ": {"emoji": "🤝", "title": "따뜻한 조력자", "desc": "사교적이고 배려심 많아 사람들과의 연결을 중요시해요."},
    "ISTP": {"emoji": "🔧", "title": "현장 해결사", "desc": "실용적이고 즉흥적 - 문제를 손으로 해결하는 걸 좋아해요."},
    "ISFP": {"emoji": "🎨", "title": "감성의 예술가", "desc": "예술적이고 현재를 즐기는 감각적인 사람입니다."},
    "ESTP": {"emoji": "🌍", "title": "모험가", "desc": "행동파 현실주의자 - 도전과 속도감을 즐깁니다."},
    "ESFP": {"emoji": "🎉", "title": "파티의 주인공", "desc": "밝고 사교적 - 분위기를 살리는 재주가 있어요."}
}

st.set_page_config(page_title="MBTI 추천", page_icon="🔍", layout="centered")

st.title("😎 나의 MBTI 캐릭터 찾기")

# 선택 버튼
selected = st.radio("MBTI를 선택하세요:", list(MBTI_DATA.keys()), horizontal=True)

if st.button("랜덤 선택 🎲"):
    selected = random.choice(list(MBTI_DATA.keys()))
    st.session_state["selected"] = selected

if selected:
    data = MBTI_DATA[selected]
    st.markdown(f"## {data['emoji']} {selected} - {data['title']}")
    st.write(data['desc'])

    if st.button("📋 결과 복사"):
        st.code(f"{selected} {data['emoji']} {data['title']} - {data['desc']}")
        st.success("복사할 내용을 위에 표시했습니다. 수동으로 복사하세요.")
else:
    st.info("MBTI를 선택하거나 랜덤 버튼을 눌러주세요!")
