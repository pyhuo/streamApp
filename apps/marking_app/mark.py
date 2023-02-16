import pandas as pd
import streamlit as st
import pymysql

st.set_page_config(
    page_title="Labeling",
)

st.title("Labeling")

userId = st.text_input('UUID')
# st.write('The current UUID: ', userId)
st.write("\n")
st.markdown('### 当前指示（用户输入)')
if userId != "123456":
    st.info("目前没有分配给您的标注数据")
else:
    st.info("loading data......")
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='users')
    cursor = db.cursor()
    sql = "select * from labelUsers"
    try:
        # 执行sql中的语句
        cursor.execute(sql)

        # 获得列名
        column = [col[0] for col in cursor.description]

        # 获得数据
        data = cursor.fetchall()
        df = pd.DataFrame(
            data,
            columns=('id', 'name', 'age')
        )
        st.dataframe(df)
        st.success("loading data success!")
    except Exception as e:
        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')



