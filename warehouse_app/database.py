from sqlalchemy import create_engine
import streamlit as st

@st.cache_resource
def get_engine():
    try:
        # Cập nhật chuỗi kết nối MySQL
        engine = create_engine(
            "mysql+pymysql://admin:Luongloc1210@database-demo.cp2oiuwu4ba1.ap-southeast-2.rds.amazonaws.com:3306/warehouse"
        )
        # Kiểm tra kết nối (nếu có thể)
        with engine.connect() as conn:
            st.success("Kết nối thành công với cơ sở dữ liệu!")
        return engine
    except Exception as e:
        # Nếu có lỗi xảy ra, hiển thị lỗi và trả về None
        st.error(f"Lỗi kết nối: {e}")
        return None

# Lấy engine và kiểm tra
engine = get_engine()

# Kiểm tra nếu engine hợp lệ trước khi sử dụng
if engine:
    try:
        with engine.begin() as conn:
            # Thực hiện các thao tác với cơ sở dữ liệu
            st.write("Đang thực hiện thao tác với cơ sở dữ liệu...")
            # Bạn có thể thực hiện các truy vấn SQL tại đây, ví dụ:
            # result = conn.execute("SELECT * FROM table_name")
            # st.write(result.fetchall())
    except Exception as e:
        st.error(f"Lỗi khi thực hiện thao tác với cơ sở dữ liệu: {e}")
else:
    st.error("Không thể kết nối với cơ sở dữ liệu")
