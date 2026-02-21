import streamlit as st
from utils import generate_scripts

st.title("🎦视频脚本生成器")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入deepseekAPI密钥：" , type = "password")
    st.markdown("[获取deepseekAPI密钥](https://platform.deepseek.com)")

subject = st.text_input("请输入视频的主题：")
video_length = st.number_input("请输入视频的大致时长（单位：分钟）：" ,
                               min_value = 0.1 ,
                               value = 0.1 ,
                               step = 0.1)
creativity = st.slider("请输入视频脚本的创造性（数字越小生成的内容就越严谨，数字越大生成的内容就越多样）：" ,
                       min_value = 0.1 ,
                       max_value = 2.0 ,
                       value = 0.2 ,
                       step = 0.1)

submit = st.button("生成脚本")
if submit and not deepseek_api_key:
    st.info("deepseekAPI密钥不能为空！")
    st.stop()
if submit and not subject:
    st.info("视频主题不能为空！")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频时长至少为0.1分钟！")
    st.stop()
if submit:
    with st.spinner("AI正在生成中，请稍候......"):
        search_result , title , script = generate_scripts(subject, video_length , creativity , deepseek_api_key)
    st.success("视频脚本已生成！")
    st.subheader("视频标题：")
    st.write(title)
    st.subheader("视频脚本：")
    st.write(script)
    with st.expander("DuckDuckGoSearch搜索结果："):
        st.info(search_result)