import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

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

name = st.text_input('크루네임 입력', '크루')
if st.button("Submit"):
    st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛')
st.text("\n")
st.text("\n")
st.text("\n")

def common():
    time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('', '10분 이내', '20분 이내', '30분 이내', '60분 이내'))
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

    if st.button('추천음식 보러가기(결과화면 수정필요)'):
        img = Image.open("./Img_test_omelet.jpg")
        st.image(img, width=300, caption="계란말이(5m, 하) 레시피 보러가기")
        img = Image.open("./Img_test_chicken.jpg")
        st.image(img, width=300, caption="치킨(30m, 상) 레시피 보러가기")

def tandanji(name):
    height = st.text_input(f'{name}님의 키(cm)를 입력해 주세요', '170')
    st.text("\n")
    st.text("\n")

    activity = st.selectbox(f"{name}님의 활동량을 선택하세요.",
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

    st.info(f'{name}님의 하루 권장 칼로리 : {cal}kcal')

    tan = cal * 0.5 / 4
    dan = cal * 0.2 / 4
    ji = cal * 0.3 / 9
    st.info(f'{name}님의 목표 탄단지 비율(하루 권장 섭취량) : 5({tan:.2f}g):2({dan:.2f}g):3({ji:.2f}g)')
    # st.info(f'{name}님 화이팅!💪')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # values = st.slider(
    # '선호하는 조리시간을 선택해 주세요',
    # 0, 180, (20, 30))
    # st.text("\n")
    # st.text("\n")
    # st.text("\n")

    common()


def gocal(name):
    # cat = st.selectbox(f"{name}님이 추구하는 식단 스타일을 골라 주세요",
    #                    ("", "고단백", "저칼로리", "고칼로리", "비건", "etc"))
    # st.write(cat, "을(를) 선택하셨습니다.")
    # st.text("\n")
    # st.text("\n")
    # st.text("\n")

    st.info(f'{name}님~ 1000칼로리 이상 감당하실 수 있으시죠?😇')
    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()


def vegan(name):
    st.info(f'{name}님~ 비건식단을 추천합니다😇')
    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()

def supper(name):
    st.info(f'{name}님~ 밤늦은 시각 출출하신가요~')
    supper_cat = st.selectbox(f'카테고리 선택',
                        ("", "낮은 칼로리 버전", "단백질 높은 버전", "튀긴 버전",
                         "건강한 버전", "매운 버전", "자극적인 버전"))
    st.write(supper_cat, "을(를) 선택하셨습니다.")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()

def random(name):
    favor = st.selectbox(f'음식 카테고리 선택',
                            ("", "한식", "중식", "양식", "일식", "매운거", "안매운거"))
    st.write(favor, "을(를) 선택하셨습니다.")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('', '10분 이내', '20분 이내', '30분 이내', '60분 이내'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choice = st.selectbox('요리 난이도 선택', ('', '상', '중', '하'))
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

def worldcup(name):
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
            img = keras.preprocessing.image.load_img(
                './Img_test_omelet.jpg', target_size=(180, 180)
            )
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)  # Create a batch
            model = keras.models.load_model('./kf_model.h5')
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            st.text(
                "{}(정확도 {:.2f}%)"
                    .format(class_names[np.argmax(score)], 100 * np.max(score))
                 )
    # if uploaded_file is not None:
    #     # To read file as bytes:
    #     bytes_data = uploaded_file.getvalue()
    #     st.write(bytes_data)
    #
    #     # To convert to a string based IO:
    #     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #     st.write(stringio)
    #
    #     # To read file as string:
    #     string_data = stringio.read()
    #     st.write(string_data)
    #
    #     # Can be used wherever a "file-like" object is accepted:
    #     dataframe = pd.read_csv(uploaded_file)
    #     st.write(dataframe)

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    message = st.text_area("불편사항을 알려주세요.")
    if st.button("Click"):
        if message.title():
            st.success(f"{name}님의 소중한 의견은 서비스 개선에 적극 반영하겠습니다. 감사합니다.")
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
    ('건강을 챙기는 으르신', '먹고죽자 치팅데이', '밤에 출출한 야식러',
     '생각없는 당신을위한 랜덤', '레시피를 찾아드려요(추억소환)')) #, '비건에의한 비건을위한'
st.text("\n")
st.text("\n")
st.text("\n")
if page == '건강을 챙기는 으르신':
    tandanji(f'{name}')
elif page == '먹고죽자 치팅데이':
    gocal(f'{name}')
# elif page == '비건에의한 비건을위한':
#     vegan(f'{name}')
elif page == '밤에 출출한 야식러':
    supper(f'{name}')
elif page == '생각없는 당신을위한 랜덤':
    random(f'{name}')
else:
    worldcup(f'{name}')



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
