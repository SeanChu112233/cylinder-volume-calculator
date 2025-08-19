import streamlit as st
import math

def calculate_volume(diameter, length, unit):
    radius = diameter / 2
    volume_cubic = math.pi * (radius ** 2) * length
    
    if unit == "mm":
        # 从mm³转换为升
        volume_liters = volume_cubic / 1_000_000
    else:  # inch
        # 从inch³转换为升 (1 inch³ = 0.0163871升)
        volume_liters = volume_cubic * 0.0163871
    
    return volume_liters

def main():
    st.title("圆柱桩载体体积计算器（单位：升）")
    st.write("输入直径和长度来计算圆柱体积（结果统一为升）")
    
    # 单位选择
    unit = st.radio("选择输入单位:", ("mm", "inch"))
    
    # 输入字段
    col1, col2 = st.columns(2)
    
    with col1:
        diameter = st.number_input(f"直径 ({unit})", min_value=0.0, value=100.0, step=0.1)
    
    with col2:
        length = st.number_input(f"长度 ({unit})", min_value=0.0, value=1000.0, step=0.1)
    
    # 计算按钮
    if st.button("计算体积"):
        volume_liters = calculate_volume(diameter, length, unit)
        
        st.success("计算结果:")
        st.write(f"圆柱体积: {volume_liters:,.3f} 升")
        
        # 显示中间计算过程（可选）
        with st.expander("查看详细计算"):
            st.write(f"直径: {diameter} {unit}")
            st.write(f"长度: {length} {unit}")
            st.write(f"半径: {diameter/2} {unit}")
            st.write(f"原始体积: {math.pi * ((diameter/2) ** 2) * length:,.2f} {unit}³")

if __name__ == "__main__":
    main()
