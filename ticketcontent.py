import streamlit as st

# 设置页面标题
st.title("工单信息模板")

# 步骤1
st.subheader("信息查询确认")
query_previous_ticket = st.checkbox("是否查询了以前工单")
query_kb = st.checkbox("是否查询了KB")
query_ei = st.checkbox("是否查询了EI")

# 判断步骤1的选项是否全选
if query_previous_ticket and query_kb and query_ei:
    # 步骤2
    st.subheader("追加信息确认")
    patch_updated = st.radio("是否打了最新补丁", ["Yes", "No"])
    latest_terminal_used = st.radio("是否用了最新终端", ["Yes", "No"])
    attempt_reproduce = st.radio("是否尝试复现", ["Yes", "No"])

    # 步骤3
    st.subheader("模板信息")
    st.write("【环境】")
    terminal_version = st.text_input("终端版本")
    ucss_version = st.text_input("UCSS版本")
    patch_info = st.text_input("补丁版本")

    st.write("【紧急度】")
    urgency = st.selectbox("请选择紧急度", ["一般", "重要", "紧急"])

    st.write("【故障现象描述】")
    fault_description = st.text_area("在些输入故障现象和排查步骤")

    st.write("【对开发的要求】")
    dev_requirements = st.text_input("在些输入对开发的要求")

    st.write("【日志路径】")
    log_path = st.text_input("请输入日志路径")

    # 拷贝按钮
    if st.button("生成升级模板\n\n\n\n"):
        # 将步骤2和步骤3的内容拼接成字符串
        content_to_copy = (
            f"\n\n\n"
            f"【环境】\n\n\n"
            f"终端版本\n {terminal_version}\n\n"
            f"UCSS版本情况 \n{ucss_version}\n\n"
            f"补丁情况 \n{patch_info}\n\n"
            f"【紧急度】\n {urgency}\n\n"
            f"【故障现象描述】\n \n"
            f"{fault_description}\n\n"
            f"【对开发的要求】 \n {dev_requirements}\n\n"
            f"【日志路径】 \n {log_path}\n\n\n"
            f"\n\n\n"
        )
        # 使用streamlit提供的功能将内容拷贝到剪贴板
        st.write(content_to_copy)

else:
    st.write("请先完成上面的确认")