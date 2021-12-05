import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# https://docs.streamlit.io/
# streamlit run streamlit_foodai.py

# add_selectbox = st.sidebar.selectbox(
#     "유형",
#     ("다이어터", "근육맨", "Mobile phone")
# )
# st.sidebar.write("this")
# st.sidebar.button("Click me!")
#
# add_selectbox2 = st.sidebar.selectbox(
#     "H?",
#     ("Email", "Home phone", "Mobile phone")
# )

st.title('🎉푸드지옥🎉')
st.header('당신만의 푸드설계앱 foodhell😊')

with st.expander('서비스 소개 더보기'):
    st.write("""

모두가 건강에 대해 걱정하지만 관심도가 낮으며, 특히 개별진단/케어 서비스는 있지만,
원포인트/전방위 케어 서비스 부재

만개의레시피DB + 식품영양성분DB 결합
냉부를 부탁해 + 부족한 영양소를 진단하고 영양관리 해주는 서비스 + 영양제 판매/일일 새벽배송

     """)

st.text("\n")
st.text("\n")
st.text("\n")

def basic():
    cat = st.selectbox("추구하는 식단 스타일을 골라 주세요",
                       ("", "고단백", "저칼로리", "고칼로리", "비건", "etc"))
    st.write(cat, "을(를) 선택하셨습니다.")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    values = st.slider(
    '선호하는 조리시간을 선택해 주세요',
    0, 180, (20, 30))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choice = st.selectbox('요리 난이도 선택', ('', '상', '중', '하'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choicetwo = st.selectbox('혹시 오늘은 먹기 싫은 것이 있나요?',
                             ('', '중식 노노해', '한식 질려', '분식 별로'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    options = st.multiselect(
    '활용하고 싶은 재료 - 냉장고에 있는 재료들을 선택해 주세요',
    ['계란', '닭고기', '파', '마늘', '소고기', '양고기', '돼지고기'])
    st.text("\n")
    st.text("\n")
    st.text("\n")

    optionstwo = st.multiselect(
    '혹시 “이건 안 들어갔으면” 하는 재료들도 있나요?',
    ['홍어', '고수', '참치', '초콜릿', '설탕'])
    st.text("\n")
    st.text("\n")

    if st.button('추천음식 보러가기'):
        img = Image.open("./Img_test_omelet.jpg")
        st.image(img, width=300, caption="계란말이(5m, 하) 레시피 보러가기")
        img = Image.open("./Img_test_chicken.jpg")
        st.image(img, width=300, caption="치킨(30m, 상) 레시피 보러가기")

def tandanji():
    height = st.text_input('고객님의 키(cm)를 입력해 주세요', '170')
    st.text("\n")
    st.text("\n")

    activity = st.selectbox("고객님의 활동량을 선택하세요.",
                            ("", "많음", "보통", "적음"))
    st.write(activity, "을(를) 선택하셨습니다.")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # st.subheader('목표 탄단지 비율과 섭취량')
    if activity == '많음':
        cal = (int(height)-100)*0.9*40
    elif activity == '보통':
        cal = (int(height)-100)*0.9*30
    else:
        cal = (int(height)-100)*0.9*25

    st.info(f'고객님의 하루 권장 칼로리 : {cal}kcal')

    tan = cal * 0.4 / 4
    dan = cal * 0.4 / 4
    ji = cal * 0.2 / 9
    st.info(f'고객님의 목표 탄단지 비율(하루 권장 섭취량) : 4({tan:.2f}g):4({dan:.2f}g):2({ji:.2f}g)')
    # st.info(f'{name}님 화이팅!💪')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    values = st.slider(
    '선호하는 조리시간을 선택해 주세요',
    0, 180, (20, 30))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choice = st.selectbox('요리 난이도 선택', ('', '상', '중', '하'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choicetwo = st.selectbox('혹시 오늘은 먹기 싫은 것이 있나요?',
                             ('', '중식 노노해', '한식 질려', '분식 별로'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    options = st.multiselect(
    '활용하고 싶은 재료 - 냉장고에 있는 재료들을 선택해 주세요',
    ['계란', '닭고기', '파', '마늘', '소고기', '양고기', '돼지고기'])
    st.text("\n")
    st.text("\n")
    st.text("\n")

    optionstwo = st.multiselect(
    '혹시 “이건 안 들어갔으면” 하는 재료들도 있나요?',
    ['홍어', '고수', '참치', '초콜릿', '설탕'])
    st.text("\n")
    st.text("\n")

    if st.button('추천음식 보러가기'):
        img = Image.open("./Img_test_omelet.jpg")
        st.image(img, width=300, caption="계란말이(5m, 하) 레시피 보러가기")
        img = Image.open("./Img_test_chicken.jpg")
        st.image(img, width=300, caption="치킨(30m, 상) 레시피 보러가기")

def random():
    st.subheader('푸드월드컵')
    message = st.text_area("불편사항을 알려주세요.")
    if st.button("Click"):
        if message.title():
            st.success("귀하의 소중한 의견은 서비스 개선에 적극 반영하겠습니다. 감사합니다.")
        else:
            st.error("텍스트를 입력해주세요")


# page = st.selectbox('원하는 서비스 선택▼▼▼', ('탄단지 밸런스 식단추천', '칼로리 밸런스 식단추천', '랜덤추천 푸드월드컵'), 0)
# st.text("\n")
# st.text("\n")
# st.text("\n")
# if page == '탄단지 밸런스 식단추천':
#     tandanji()
# elif page == '칼로리 밸런스 식단추천':
#     cal()
# else:
#     random()

page = st.radio(
     "★원하는 서비스 선택★",
    ('유형별 식단추천(basic)', '탄단지 밸런스 식단추천(개인정보必)', '랜덤추천 푸드월드컵'))
st.text("\n")
st.text("\n")
st.text("\n")
if page == '유형별 식단추천(basic)':
    basic()
elif page == '탄단지 밸런스 식단추천(개인정보必)':
    tandanji()
else:
    random()



# name = st.text_input('크루네임 입력', '민정')
# if st.button("Submit"):
#     # if name.title():
#     st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛💛💛')
# st.text("\n")

# bf = st.text_input('아침에 무엇을 드셨습니까?', '')
# lc = st.text_input('점심에 무엇을 드셨습니까?', '')
# dn = st.text_input('저녁에 무엇을 드셨습니까?', '')
# if st.button("영양 진단하기"):
#     st.text("저런, 단백질이 50g 부족하네요! 내일 요 음식 어떠세요~? 레시피는 아래 링크 참조")
#     img = Image.open("./Img_test_omelet.jpg")
#     st.image(img, width=400, caption="계란말이")
# st.text("\n")
# st.text("\n")
# st.text("\n")
#
# st.subheader(f'앗, 냉장고에 계란이 없으시다구요? 지금 {name}님의 냉장고에 어떤 재료가 있는지 알려주세요~')
# name = st.text_input('냉장고 재료 입력', '')
# if st.button("냉부를 부탁해~"):
#     st.text("내일은 치킨 시켜드세요~")
#     img = Image.open("./Img_test_chicken.jpg")
#     st.image(img, width=400, caption="치킨")



# if __name__ == '__main__':
#     main()
