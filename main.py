import os
import streamlit as st
import time
from langchain_community.chat_models import ChatOpenAI  # langchain_community에서 ChatOpenAI를 가져옵니다.

# API 키 가져오기 및 ChatOpenAI 인스턴스 생성
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일 또는 Streamlit Secrets를 확인하세요.")
chat_model = ChatOpenAI(openai_api_key=api_key)

# Streamlit UI 구성
st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시해주세요")

if st.button("시 작성 요청하기"):
    # 스피너 표시
    with st.spinner("시를 작성하고 있습니다..."):
        # 모델에 입력값을 전달하고 결과를 가져오기
        response = chat_model.invoke(f"{content}에 대한 시를 써줘")
        time.sleep(5)  # 실제 처리 시간 시뮬레이션 (선택 사항)

    # 응답이 완료되었음을 표시
    st.success("작성 완료!")
    st.subheader("작성된 시")
    st.write(response.content)

    # 전체 응답 보기 (선택 사항)
    with st.expander("전체 응답 보기"):
        st.json(response.__dict__)
