import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", page_icon="✊", layout="centered")

# 세션 상태 초기화
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "draw_count" not in st.session_state:
    st.session_state.draw_count = 0
if "result_message" not in st.session_state:
    st.session_state.result_message = ""
if "player_choice" not in st.session_state:
    st.session_state.player_choice = ""
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""
if "game_result" not in st.session_state:
    st.session_state.game_result = ""

# 선택지 이모지 매핑
CHOICES = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️",
}

# 승패 판정 함수
def determine_winner(player, computer):
    if player == computer:
        return "draw"
    win_conditions = {
        "가위": "보",
        "바위": "가위",
        "보": "바위",
    }
    if win_conditions[player] == computer:
        return "win"
    return "lose"

# 게임 실행 함수
def play_game(player_choice):
    computer_choice = random.choice(list(CHOICES.keys()))
    result = determine_winner(player_choice, computer_choice)

    st.session_state.player_choice = player_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.game_result = result

    if result == "win":
        st.session_state.player_score += 1
        st.session_state.result_message = "🎉 이겼습니다!"
    elif result == "lose":
        st.session_state.computer_score += 1
        st.session_state.result_message = "😢 졌습니다..."
    else:
        st.session_state.draw_count += 1
        st.session_state.result_message = "🤝 비겼습니다!"

# ─── UI 시작 ───────────────────────────────────────────────

st.title("✊ 가위바위보 게임")
st.markdown("컴퓨터와 가위바위보를 해보세요!")
st.divider()

# 점수판
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🧑 나", st.session_state.player_score)
with col2:
    st.metric("🤝 무승부", st.session_state.draw_count)
with col3:
    st.metric("🤖 컴퓨터", st.session_state.computer_score)

st.divider()

# 선택 버튼
st.subheader("무엇을 낼까요?")
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("✌️ 가위", use_container_width=True):
        play_game("가위")
with btn_col2:
    if st.button("✊ 바위", use_container_width=True):
        play_game("바위")
with btn_col3:
    if st.button("🖐️ 보", use_container_width=True):
        play_game("보")

# 결과 표시
if st.session_state.player_choice:
    st.divider()
    st.subheader("결과")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.markdown(
            f"<div style='text-align:center; font-size:60px;'>{CHOICES[st.session_state.player_choice]}</div>"
            f"<div style='text-align:center; font-size:18px;'>나: {st.session_state.player_choice}</div>",
            unsafe_allow_html=True,
        )
    with res_col2:
        st.markdown(
            f"<div style='text-align:center; font-size:60px;'>{CHOICES[st.session_state.computer_choice]}</div>"
            f"<div style='text-align:center; font-size:18px;'>컴퓨터: {st.session_state.computer_choice}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    game_result = st.session_state.game_result
    if game_result == "win":
        st.success(st.session_state.result_message)
        st.balloons()
    elif game_result == "lose":
        st.error(st.session_state.result_message)
    else:
        st.info(st.session_state.result_message)

st.divider()

# 초기화 버튼
if st.button("🔄 점수 초기화", use_container_width=True):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_count = 0
    st.session_state.result_message = ""
    st.session_state.player_choice = ""
    st.session_state.computer_choice = ""
    st.session_state.game_result = ""
    st.rerun()
