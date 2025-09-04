## 
## VitaBot - 비타민 & 영양 전문 챗봇
## API를 숨기기 위한 설정
## 01. 해당 작업 폴더 내에 '.streamlit'라는 폴더를 만든다.
## 02. 해당 폴더 내에 'secrets.toml'이라는 파일을 만든다.
## 03. secrets.toml 파일에 아래와 같이 작성한다.
## [openai]
## API_KEY = "sk-..." # 본인의 API 키를 입력한다.

import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(
    page_title="VitaBot 🌱 - 비타민 & 영양 전문 챗봇",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 메인 타이틀
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="color: #2E7D32; font-size: 3em; margin: 0;">
        🌱 VitaBot 🐞
    </h1>
</div>
""", unsafe_allow_html=True)

# 녹색 테마 및 유기농 건강식품 애니메이션 CSS 스타일
green_theme_css = """
<style>
/* 전체 배경과 테마 설정 */
.stApp {
    background: linear-gradient(135deg, #E8F5E8 0%, #F1F8E9 50%, #E8F5E8 100%);
}

/* 사이드바 스타일링 */
.css-1d391kg {
    background-color: #C8E6C9;
}

/* 메인 컨테이너 */
.main .block-container {
    padding-top: 2rem;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(76, 175, 80, 0.1);
    margin: 20px;
}

/* 로딩 애니메이션 컨테이너 */
.vita-loading-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 150px;
    margin: 20px 0;
    background: linear-gradient(45deg, #E8F5E8, #F1F8E9);
    border-radius: 20px;
    border: 2px solid #A5D6A7;
    position: relative;
    overflow: hidden;
}

/* 배경 식물 장식 */
.vita-loading-container::before {
    content: "🌿🌱🍃";
    position: absolute;
    top: 10px;
    left: 20px;
    font-size: 20px;
    opacity: 0.3;
    animation: sway 3s ease-in-out infinite;
}

.vita-loading-container::after {
    content: "🌿🌾🌱";
    position: absolute;
    bottom: 10px;
    right: 20px;
    font-size: 20px;
    opacity: 0.3;
    animation: sway 3s ease-in-out infinite reverse;
}

/* 무당벌레 애니메이션 */
.ladybug {
    width: 80px;
    height: 80px;
    position: relative;
    animation: crawl 3s ease-in-out infinite;
}

.ladybug::before {
    content: "🐞";
    font-size: 50px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    animation: wiggle 1.5s ease-in-out infinite;
}

/* 식물 요소들 */
.plants {
    display: flex;
    justify-content: space-around;
    width: 200px;
    margin-top: 10px;
}

.plant {
    font-size: 25px;
    animation: grow 2s ease-in-out infinite;
}

.plant:nth-child(1) { animation-delay: 0s; }
.plant:nth-child(2) { animation-delay: 0.5s; }
.plant:nth-child(3) { animation-delay: 1s; }

/* 키프레임 애니메이션들 */
@keyframes crawl {
    0%, 100% { transform: translateX(-30px); }
    50% { transform: translateX(30px); }
}

@keyframes wiggle {
    0%, 100% { transform: translate(-50%, -50%) rotate(-3deg); }
    50% { transform: translate(-50%, -50%) rotate(3deg); }
}

@keyframes grow {
    0%, 100% { transform: scale(1) translateY(0px); }
    50% { transform: scale(1.1) translateY(-5px); }
}

@keyframes sway {
    0%, 100% { transform: rotate(-2deg); }
    50% { transform: rotate(2deg); }
}

/* 로딩 텍스트 */
.loading-text {
    text-align: center;
    font-size: 18px;
    color: #2E7D32;
    margin-top: 15px;
    font-weight: 600;
    animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.7; color: #2E7D32; }
    50% { opacity: 1; color: #4CAF50; }
}

/* 채팅 메시지 스타일링 */
.chat-message {
    padding: 15px;
    margin: 10px 0;
    border-radius: 15px;
    border-left: 4px solid #4CAF50;
    background: linear-gradient(135deg, #F1F8E9 0%, #E8F5E8 100%);
    box-shadow: 0 2px 10px rgba(76, 175, 80, 0.1);
}

/* 버튼 스타일링 */
.stButton > button {
    background: linear-gradient(135deg, #4CAF50 0%, #66BB6A 100%);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 25px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #388E3C 0%, #4CAF50 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
}

/* 입력 필드 스타일링 */
.stTextInput > div > div > input {
    border: 2px solid #A5D6A7;
    border-radius: 15px;
    padding: 10px 15px;
    background-color: rgba(255, 255, 255, 0.9);
    color: #000000 !important;
}

.stTextInput > div > div > input:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
    color: #000000 !important;
}

.stTextInput > div > div > input::placeholder {
    color: #666666 !important;
}

/* 헤더 장식 요소 */
.header-decoration {
    text-align: center;
    font-size: 2em;
    margin: 20px 0;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}
</style>
"""

# CSS 스타일 적용
st.markdown(green_theme_css, unsafe_allow_html=True)

# 헤더 장식 요소 추가

# 사이드바 설정
st.sidebar.markdown("""
<div style="text-align: center; padding: 10px;">
    <h2 style="color: #2E7D32;">🌱 VitaBot 설정</h2>
    <p style="color: #4CAF50; font-size: 14px;">건강한 삶을 위한 영양 상담</p>
</div>
""", unsafe_allow_html=True)

openai_api_key = st.sidebar.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 사이드바에 비타민 정보 추가
st.sidebar.markdown("""
---
### 🌿 주요 비타민 정보
- **비타민 A** 🥕: 시력, 면역력
- **비타민 B** 🌾: 에너지 대사
- **비타민 C** 🍊: 항산화, 면역력
- **비타민 D** ☀️: 뼈 건강
- **비타민 E** 🌰: 항산화 작용
- **비타민 K** 🥬: 혈액 응고

### 🐞 건강 팁
- 균형잡힌 식단 섭취
- 규칙적인 운동
- 충분한 수면
- 스트레스 관리
""")

if not openai_api_key:
    st.sidebar.warning("OpenAI 키를 입력해주세요.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

# 초기 대화 상태 설정
if "messages" not in st.session_state:
    st.session_state.messages = [  
        { "role": "system", 
          "content": """당신은 VitaBot, 전문적인 비타민 및 영양 상담 챗봇입니다. 🌱

**주요 역할:**
- 비타민, 미네랄, 영양소에 대한 전문적인 정보 제공
- 개인의 건강 상태와 생활 패턴에 맞는 영양 조언
- 유기농 건강식품, 자연 식품에 대한 가이드
- 영양 결핍 증상 및 해결 방안 상담
- 건강한 식단 계획 및 영양 밸런스 조언

**답변 스타일:**
- 기본적으로 한국어로 친근하고 전문적으로 답변
- 복잡한 의학 용어는 쉽게 설명
- 구체적인 예시와 실용적인 조언 제공
- 필요시 영양성분표나 권장량 정보 포함
- 의료적 진단이 필요한 경우 전문의 상담 권유

**제한사항:**
- 의학적 진단은 하지 않음
- 처방약에 대한 조언은 하지 않음
- 모르는 내용은 솔직하게 모른다고 답변
- 개인차가 있을 수 있음을 항상 언급

건강하고 활기찬 삶을 위해 최선을 다해 도움드리겠습니다! 🐞🌿"""
        }  
    ]

# 환영 메시지
if len(st.session_state.messages) == 1:  # 시스템 메시지만 있을 때
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #E8F5E8, #F1F8E9); 
                border-radius: 20px; margin: 20px 0; border: 2px solid #A5D6A7;">
        <h3 style="color: #2E7D32; margin-bottom: 15px;">🌱 VitaBot에 오신 것을 환영합니다! 🐞</h3>
        <p style="color: #4CAF50; font-size: 16px; line-height: 1.6;">
            안녕하세요! 저는 여러분의 건강한 삶을 위한 비타민 & 영양 전문 상담사입니다.<br>
            비타민, 미네랄, 영양소에 대한 궁금한 점이나 건강한 식단에 대해 무엇이든 물어보세요!
        </p>
        <div style="margin-top: 20px;">
            <span style="font-size: 24px;">🥕 🥬 🍊 🥜 🍓 🥑 🌾 🍇</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 폼을 사용하여 엔터키 입력 시 자동 전송 구현
with st.form(key="chat_form", clear_on_submit=True):
    # 텍스트 입력창과 버튼들을 한 줄에 배치
    col1, col2, col3 = st.columns([6, 1.5, 1.5])
    
    with col1:
        user_input = st.text_input("🌱 영양 상담:", key="user_input", 
                                  placeholder="비타민이나 영양에 대해 궁금한 점을 물어보세요... (예: 비타민 D 부족 증상이 뭔가요?)",
                                  label_visibility="collapsed")
    
    with col2:
        submitted = st.form_submit_button("💬 질문하기", use_container_width=True)
    
    with col3:
        reset_chat = st.form_submit_button("🔄 초기화", use_container_width=True)

# 대화 초기화 처리
if reset_chat:
    st.session_state.messages = [st.session_state.messages[0]]  # 시스템 메시지만 유지
    st.rerun()

# 폼이 제출되었거나 전송 버튼이 클릭되었을 때 처리
if submitted and user_input.strip():
    # 사용자 메시지 추가
    st.session_state.messages.append({ "role": "user", 
                                       "content": user_input.strip()})

    # 로딩 애니메이션 표시
    loading_placeholder = st.empty()
    with loading_placeholder.container():
        st.markdown("""
        <div class="vita-loading-container">
            <div class="ladybug"></div>
            <div class="plants">
                <div class="plant">🌱</div>
                <div class="plant">🌿</div>
                <div class="plant">🍃</div>
            </div>
        </div>
        <div class="loading-text">🌱 영양 정보를 분석하고 있습니다... 🐞</div>
        """, unsafe_allow_html=True)

    try:
        # OpenAI API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # gpt-4o-mini로 변경
            messages=st.session_state.messages
        )

        # OpenAI 응답 추가
        response_message = response.choices[0].message.content
        st.session_state.messages.append({ "role": "assistant", 
                                           "content": response_message})
        
        # 로딩 애니메이션 제거
        loading_placeholder.empty()
        
        # 페이지 새로고침으로 최신 대화 내용 표시
        st.rerun()
        
    except Exception as e:
        # 오류 발생 시 로딩 애니메이션 제거하고 오류 메시지 표시
        loading_placeholder.empty()
        st.error(f"오류가 발생했습니다: {str(e)}")
        # 오류 발생 시 사용자 메시지 제거
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
            st.session_state.messages.pop()

# 대화 내용 표시
for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    if message["role"] == "user":
        # 사용자 메시지
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; margin: 15px 0;">
            <div style="background: linear-gradient(135deg, #4CAF50, #66BB6A); 
                        color: white; padding: 15px 20px; border-radius: 20px 20px 5px 20px; 
                        max-width: 70%; box-shadow: 0 2px 10px rgba(76, 175, 80, 0.3);">
                <strong>👤 You:</strong><br>{message['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # VitaBot 응답
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-start; margin: 15px 0;">
            <div style="background: linear-gradient(135deg, #E8F5E8, #F1F8E9); 
                        color: #2E7D32; padding: 15px 20px; border-radius: 20px 20px 20px 5px; 
                        max-width: 70%; border-left: 4px solid #4CAF50;
                        box-shadow: 0 2px 10px rgba(76, 175, 80, 0.1);">
                <strong>🌱 VitaBot 🐞:</strong><br>{message['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# 푸터 추가
st.markdown("""
---
<div style="text-align: center; padding: 20px; color: #4CAF50; font-size: 14px;">
    <p>⚠️ <em>본 정보는 일반적인 영양 상담이며, 개인차가 있을 수 있습니다. 질병이나 특별한 건강 상태가 있으신 경우 전문의와 상담하세요.</em></p>
    <div style="margin-top: 15px;">
        <span style="font-size: 20px;">🌿 🐝 🌱 🦋 🍃 🐞 🌾 🦗 🌿</span>
    </div>
</div>
""", unsafe_allow_html=True)
