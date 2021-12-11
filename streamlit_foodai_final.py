import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

# https://docs.streamlit.io/
# streamlit run streamlit_foodai_final.py

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

st.title('🎉ChrisKitchen🎉')
st.header('당신만의 푸드설계앱 ChrisKitchen😊')

with st.expander('서비스 소개 더보기'):
    st.write("""

모두가 건강에 대해 걱정하지만 관심도가 낮으며, 특히 개별진단/케어 서비스는 있지만,
원포인트/전방위 케어 서비스 부재

만개의레시피DB + 식품영양성분DB 결합
냉부를 부탁해 + 부족한 영양소를 진단하고 영양관리 해주는 서비스 + 영양제 판매/일일 새벽배송

     """)
st.text("\n")
st.text("\n")

name = st.text_input('크루네임 입력', '크루')
if st.button("Submit"):
    st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛')
st.text("\n")
st.text("\n")
st.text("\n")

def common(name):
    common_time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('10분 이내', '15분 이내', '30분 이내', '60분 이내'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    common_level = st.selectbox('요리 난이도 선택', ('아무나', '초급', '중급', '고급'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    common_dislike_food = st.text_input('혹시 오늘은 먹기 싫은 것이 있나요?', '')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    common_fridge = st.text_input('활용하고 싶은 재료 - 냉장고에 있는 재료들을 입력해 주세요', '')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    common_dislike_ingredient = st.text_input('혹시 “이건 안 들어갔으면” 하는 재료들도 있나요?', '')
    st.text("\n")
    st.text("\n")

    if st.button('추천 레시피 보러가기'):
        st.text('결과화면(수정필요)')


def random(name):
    random_time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('10분 이내', '15분 이내', '30분 이내', '60분 이내'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    random_level = st.selectbox('요리 난이도 선택', ('아무나', '초급', '중급', '고급'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    if st.button('추천 레시피 보러가기'):
        st.text('결과화면(수정필요)')

def memory(name):
    st.info(f'{name}님의 추억이 담긴 레시피를 찾아드려요~😇')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    class_names = [
        '후라이드치킨', '간장게장', '갈비구이', '갈비찜', '갈비탕', '갈치구이', '갈치조림', '감자전', '감자조림', '감자채볶음', '감자탕', '갓김치', '건새우볶음', '경단',
        '계란국', '계란말이', '계란찜', '계란후라이', '고등어구이', '고등어조림', '고사리나물', '고추장진미채볶음', '고추튀김', '곱창구이', '곱창전골', '과메기', '김밥',
        '김치볶음밥', '김치전', '김치찌개', '김치찜', '깍두기', '깻잎장아찌', '꼬막찜', '꽁치조림', '꽈리고추무침', '꿀떡', '나박김치', '누룽지', '닭갈비', '닭계장',
        '닭볶음탕', '더덕구이', '도라지무침', '도토리묵', '동그랑땡', '동태찌개', '된장찌개', '두부김치', '두부조림', '땅콩조림', '떡갈비', '떡꼬치', '떡만두국', '떡볶이',
        '라면', '라볶이', '막국수', '만두', '매운탕', '멍게', '메추리알장조림', '멸치볶음', '무국', '무생채', '물냉면', '물회', '미역국', '미역줄기볶음', '불고기',
        '전복죽'
    ]

    uploaded_file = st.file_uploader("파일찾기")
    if uploaded_file:
        st.image(uploaded_file, width=400) #, caption="입력 데이터"
        if st.button("이미지 분석하기"):
            # img = keras.preprocessing.image.load_img(
            #     './Img_test_omelet.jpg', target_size=(180, 180)
            # ) # './Img_test_omelet.jpg'
            # img_array = keras.preprocessing.image.img_to_array(img)
            # img_array = tf.expand_dims(img_array, 0)  # Create a batch
            # model = keras.models.load_model('./kf_model.h5')
            # predictions = model.predict(img_array)
            # score = tf.nn.softmax(predictions[0])
            #
            # st.text(
            #     "{}(정확도 {:.2f}%)"
            #         .format(class_names[np.argmax(score)], 100 * np.max(score))
            #      )

            st.text("계란말이: 97.8%")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    message = st.text_area('불편사항을 알려주세요.')
    if st.button('Click'):
        if message.title():
            st.success(f'{name}님의 소중한 의견은 서비스 개선에 적극 반영하겠습니다. 감사합니다.')
        else:
            st.error('텍스트를 입력해주세요')

page = st.radio(
     '★원하는 서비스 선택★',
    ('냉부를 부탁해', '레시피를 찾아드려요(추억소환)', '생각없는 당신을위한 랜덤'))
st.text("\n")
st.text("\n")
st.text("\n")
if page == '냉부를 부탁해':
    common(f'{name}')
elif page == '레시피를 찾아드려요(추억소환)':
    memory(f'{name}')
elif page == '생각없는 당신을위한 랜덤':
    random(f'{name}')



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
