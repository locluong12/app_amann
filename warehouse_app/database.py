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
            print("Kết nối thành công")
        return engine
    except Exception as e:
        # Nếu có lỗi xảy ra, in ra lỗi và trả về None
        print(f"Lỗi kết nối: {e}")
        return None

# Lấy engine và kiểm tra
engine = get_engine()

# Kiểm tra nếu engine hợp lệ trước khi sử dụng
if engine:
    with engine.begin() as conn:
        # Thực hiện các thao tác với cơ sở dữ liệu
        print("Đang thực hiện thao tác với cơ sở dữ liệu")
else:
    print("Không thể kết nối với cơ sở dữ liệu")
