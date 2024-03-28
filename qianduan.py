import streamlit as st


st.title('这里是福建理工大学，欢迎您的到来')
st.write('### 晚上好，我是你的专门顾问欧阳丁城! ')

checked = st.checkbox('同意及接受协议,受到语言打击，一切由自己承担')
if checked :
    st.write('感谢你的理解')

st.divider()

age=st.number_input("请问你多大了：",value=10,min_value=1,max_value=100)
if 12<age<36:
    st.write(f'这个年龄别想太多啦')
elif 36<age<100:
    st.write(f'你已经很不错了，加油')


phone =st.text_input("你的电话是", type="password")

st.divider()

you = st.text_input('请告诉我你的故事，我会对此给出建议')
sub = st.button('提交')
if sub :
    st.write('请+v:18684963620')
