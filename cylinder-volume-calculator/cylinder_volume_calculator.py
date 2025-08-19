{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "434735ea-b49f-46df-be95-c23cc0f1b19d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import math\n",
    "\n",
    "def calculate_volume(diameter, length, unit):\n",
    "    radius = diameter / 2\n",
    "    volume = math.pi * (radius ** 2) * length\n",
    "    \n",
    "    if unit == \"mm\":\n",
    "        # 转换为立方米\n",
    "        volume_m3 = volume / (1000 ** 3)\n",
    "        return volume, volume_m3\n",
    "    else:  # inch\n",
    "        # 转换为立方英尺\n",
    "        volume_ft3 = volume / (12 ** 3)\n",
    "        return volume, volume_ft3\n",
    "\n",
    "def main():\n",
    "    st.title(\"圆柱桩载体体积计算器\")\n",
    "    st.write(\"输入直径和长度来计算圆柱体积\")\n",
    "    \n",
    "    # 单位选择\n",
    "    unit = st.radio(\"选择单位:\", (\"mm\", \"inch\"))\n",
    "    \n",
    "    # 输入字段\n",
    "    col1, col2 = st.columns(2)\n",
    "    \n",
    "    with col1:\n",
    "        diameter = st.number_input(f\"直径 ({unit})\", min_value=0.0, value=100.0, step=0.1)\n",
    "    \n",
    "    with col2:\n",
    "        length = st.number_input(f\"长度 ({unit})\", min_value=0.0, value=1000.0, step=0.1)\n",
    "    \n",
    "    # 计算按钮\n",
    "    if st.button(\"计算体积\"):\n",
    "        volume, converted_volume = calculate_volume(diameter, length, unit)\n",
    "        \n",
    "        st.success(\"计算结果:\")\n",
    "        st.write(f\"圆柱体积: {volume:,.2f} {unit}³\")\n",
    "        \n",
    "        if unit == \"mm\":\n",
    "            st.write(f\"转换为立方米: {converted_volume:,.6f} m³\")\n",
    "        else:\n",
    "            st.write(f\"转换为立方英尺: {converted_volume:,.6f} ft³\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
