"""Streamlit Math Operations Calculator

An interactive web application that provides a user-friendly interface
for the comprehensive math_operations module.
"""

import streamlit as st
import math_operations as mo
import math

# Page configuration
st.set_page_config(
    page_title="Math Operations Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .category-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .result-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🧮 Math Operations Calculator</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for category selection
st.sidebar.title("📚 Operation Categories")
st.sidebar.markdown("Select a category to perform calculations:")

category = st.sidebar.selectbox(
    "Choose Category",
    [
        "Basic Arithmetic",
        "Advanced Math",
        "Statistics",
        "Trigonometry",
        "Logarithms",
        "Geometry",
        "Conversions",
        "Percentages"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Tip:** This app uses the comprehensive math_operations module "
    "with 50+ mathematical functions!"
)

# Main content area
if category == "Basic Arithmetic":
    st.markdown('<h2 class="category-header">➕ Basic Arithmetic Operations</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("First Number", value=10.0, key="basic_num1")
    with col2:
        num2 = st.number_input("Second Number", value=5.0, key="basic_num2")
    
    operation = st.selectbox(
        "Select Operation",
        ["Add", "Subtract", "Multiply", "Divide", "Floor Divide", "Modulo", "Power"]
    )
    
    if st.button("Calculate", key="basic_calc"):
        try:
            if operation == "Add":
                result = mo.add(num1, num2)
                st.success(f"✅ {num1} + {num2} = **{result}**")
            elif operation == "Subtract":
                result = mo.subtract(num1, num2)
                st.success(f"✅ {num1} - {num2} = **{result}**")
            elif operation == "Multiply":
                result = mo.multiply(num1, num2)
                st.success(f"✅ {num1} × {num2} = **{result}**")
            elif operation == "Divide":
                result = mo.divide(num1, num2)
                st.success(f"✅ {num1} ÷ {num2} = **{result}**")
            elif operation == "Floor Divide":
                result = mo.floor_divide(num1, num2)
                st.success(f"✅ {num1} // {num2} = **{result}**")
            elif operation == "Modulo":
                result = mo.modulo(num1, num2)
                st.success(f"✅ {num1} % {num2} = **{result}**")
            elif operation == "Power":
                result = mo.power(num1, num2)
                st.success(f"✅ {num1} ^ {num2} = **{result}**")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif category == "Advanced Math":
    st.markdown('<h2 class="category-header">🔬 Advanced Mathematical Operations</h2>', unsafe_allow_html=True)
    
    operation = st.selectbox(
        "Select Operation",
        ["Square Root", "Cube Root", "Factorial", "Absolute Value", "GCD", "LCM", "Is Prime", "Is Even", "Is Odd"]
    )
    
    if operation in ["GCD", "LCM"]:
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("First Number", value=12, step=1, key="adv_num1")
        with col2:
            num2 = st.number_input("Second Number", value=8, step=1, key="adv_num2")
    else:
        num1 = st.number_input("Enter Number", value=16.0, key="adv_single")
    
    if st.button("Calculate", key="adv_calc"):
        try:
            if operation == "Square Root":
                result = mo.square_root(num1)
                st.success(f"✅ √{num1} = **{result}**")
            elif operation == "Cube Root":
                result = mo.cube_root(num1)
                st.success(f"✅ ∛{num1} = **{result}**")
            elif operation == "Factorial":
                result = mo.factorial(int(num1))
                st.success(f"✅ {int(num1)}! = **{result}**")
            elif operation == "Absolute Value":
                result = mo.absolute(num1)
                st.success(f"✅ |{num1}| = **{result}**")
            elif operation == "GCD":
                result = mo.gcd(int(num1), int(num2))
                st.success(f"✅ GCD({int(num1)}, {int(num2)}) = **{result}**")
            elif operation == "LCM":
                result = mo.lcm(int(num1), int(num2))
                st.success(f"✅ LCM({int(num1)}, {int(num2)}) = **{result}**")
            elif operation == "Is Prime":
                result = mo.is_prime(int(num1))
                st.success(f"✅ {int(num1)} is {'prime' if result else 'not prime'}")
            elif operation == "Is Even":
                result = mo.is_even(int(num1))
                st.success(f"✅ {int(num1)} is {'even' if result else 'odd'}")
            elif operation == "Is Odd":
                result = mo.is_odd(int(num1))
                st.success(f"✅ {int(num1)} is {'odd' if result else 'even'}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif category == "Statistics":
    st.markdown('<h2 class="category-header">📊 Statistical Operations</h2>', unsafe_allow_html=True)
    
    st.write("Enter numbers separated by commas:")
    numbers_input = st.text_input("Numbers", value="10, 20, 30, 40, 50", key="stats_input")
    
    operation = st.selectbox(
        "Select Operation",
        ["Mean", "Median", "Mode", "Variance", "Standard Deviation", "Sum", "Min", "Max", "Range"]
    )
    
    if st.button("Calculate", key="stats_calc"):
        try:
            numbers = [float(x.strip()) for x in numbers_input.split(",")]
            
            if operation == "Mean":
                result = mo.mean(numbers)
                st.success(f"✅ Mean = **{result:.4f}**")
            elif operation == "Median":
                result = mo.median(numbers)
                st.success(f"✅ Median = **{result:.4f}**")
            elif operation == "Mode":
                result = mo.mode(numbers)
                st.success(f"✅ Mode = **{result}**")
            elif operation == "Variance":
                result = mo.variance(numbers)
                st.success(f"✅ Variance = **{result:.4f}**")
            elif operation == "Standard Deviation":
                result = mo.standard_deviation(numbers)
                st.success(f"✅ Standard Deviation = **{result:.4f}**")
            elif operation == "Sum":
                result = mo.sum(numbers)
                st.success(f"✅ Sum = **{result:.4f}**")
            elif operation == "Min":
                result = mo.min(numbers)
                st.success(f"✅ Minimum = **{result:.4f}**")
            elif operation == "Max":
                result = mo.max(numbers)
                st.success(f"✅ Maximum = **{result:.4f}**")
            elif operation == "Range":
                result = mo.range(numbers)
                st.success(f"✅ Range = **{result:.4f}**")
            
            st.info(f"📝 Dataset: {numbers}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif category == "Trigonometry":
    st.markdown('<h2 class="category-header">📐 Trigonometric Functions</h2>', unsafe_allow_html=True)
    
    angle = st.number_input("Enter Angle (in degrees)", value=45.0, key="trig_angle")
    
    operation = st.selectbox(
        "Select Function",
        ["Sine", "Cosine", "Tangent", "Arcsine", "Arccosine", "Arctangent"]
    )
    
    if st.button("Calculate", key="trig_calc"):
        try:
            if operation == "Sine":
                result = mo.sine(angle)
                st.success(f"✅ sin({angle}°) = **{result:.6f}**")
            elif operation == "Cosine":
                result = mo.cosine(angle)
                st.success(f"✅ cos({angle}°) = **{result:.6f}**")
            elif operation == "Tangent":
                result = mo.tangent(angle)
                st.success(f"✅ tan({angle}°) = **{result:.6f}**")
            elif operation == "Arcsine":
                if -1 <= angle <= 1:
                    result = mo.arcsine(angle)
                    st.success(f"✅ arcsin({angle}) = **{result:.6f}°**")
                else:
                    st.error("❌ Arcsine input must be between -1 and 1")
            elif operation == "Arccosine":
                if -1 <= angle <= 1:
                    result = mo.arccosine(angle)
                    st.success(f"✅ arccos({angle}) = **{result:.6f}°**")
                else:
                    st.error("❌ Arccosine input must be between -1 and 1")
            elif operation == "Arctangent":
                result = mo.arctangent(angle)
                st.success(f"✅ arctan({angle}) = **{result:.6f}°**")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif category == "Logarithms":
    st.markdown('<h2 class="category-header">📈 Logarithmic Functions</h2>', unsafe_allow_html=True)
    
    num = st.number_input("Enter Number (must be positive)", value=100.0, min_value=0.0001, key="log_num")
    
    operation = st.selectbox(
        "Select Function",
        ["Natural Log (ln)", "Log Base 10", "Log Base N"]
    )
    
    if operation == "Log Base N":
        base = st.number_input("Enter Base", value=2.0, min_value=0.0001, key="log_base")
    
    if st.button("Calculate", key="log_calc"):
        try:
            if operation == "Natural Log (ln)":
                result = mo.natural_log(num)
                st.success(f"✅ ln({num}) = **{result:.6f}**")
            elif operation == "Log Base 10":
                result = mo.log_base_10(num)
                st.success(f"✅ log₁₀({num}) = **{result:.6f}**")
            elif operation == "Log Base N":
                result = mo.log_base_n(num, base)
                st.success(f"✅ log_{base}({num}) = **{result:.6f}**")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif category == "Geometry":
    st.markdown('<h2 class="category-header">📏 Geometric Calculations</h2>', unsafe_allow_html=True)
    
    shape = st.selectbox(
        "Select Shape",
        ["Circle", "Rectangle", "Triangle", "Sphere", "Cylinder"]
    )
    
    if shape == "Circle":
        radius = st.number_input("Radius", value=5.0, min_value=0.0, key="circle_r")
        calc_type = st.radio("Calculate", ["Area", "Circumference"])
        
        if st.button("Calculate", key="circle_calc"):
            if calc_type == "Area":
                result = mo.circle_area(radius)
                st.success(f"✅ Circle Area = **{result:.4f}** square units")
            else:
                result = mo.circle_circumference(radius)
                st.success(f"✅ Circle Circumference = **{result:.4f}** units")
    
    elif shape == "Rectangle":
        col1, col2 = st.columns(2)
        with col1:
            length = st.number_input("Length", value=10.0, min_value=0.0, key="rect_l")
        with col2:
            width = st.number_input("Width", value=5.0, min_value=0.0, key="rect_w")
        
        calc_type = st.radio("Calculate", ["Area", "Perimeter"])
        
        if st.button("Calculate", key="rect_calc"):
            if calc_type == "Area":
                result = mo.rectangle_area(length, width)
                st.success(f"✅ Rectangle Area = **{result:.4f}** square units")
            else:
                result = mo.rectangle_perimeter(length, width)
                st.success(f"✅ Rectangle Perimeter = **{result:.4f}** units")
    
    elif shape == "Triangle":
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base", value=10.0, min_value=0.0, key="tri_b")
        with col2:
            height = st.number_input("Height", value=8.0, min_value=0.0, key="tri_h")
        
        if st.button("Calculate Area", key="tri_calc"):
            result = mo.triangle_area(base, height)
            st.success(f"✅ Triangle Area = **{result:.4f}** square units")
    
    elif shape == "Sphere":
        radius = st.number_input("Radius", value=5.0, min_value=0.0, key="sphere_r")
        
        if st.button("Calculate Volume", key="sphere_calc"):
            result = mo.sphere_volume(radius)
            st.success(f"✅ Sphere Volume = **{result:.4f}** cubic units")
    
    elif shape == "Cylinder":
        col1, col2 = st.columns(2)
        with col1:
            radius = st.number_input("Radius", value=5.0, min_value=0.0, key="cyl_r")
        with col2:
            height = st.number_input("Height", value=10.0, min_value=0.0, key="cyl_h")
        
        if st.button("Calculate Volume", key="cyl_calc"):
            result = mo.cylinder_volume(radius, height)
            st.success(f"✅ Cylinder Volume = **{result:.4f}** cubic units")

elif category == "Conversions":
    st.markdown('<h2 class="category-header">🔄 Unit Conversions</h2>', unsafe_allow_html=True)
    
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Temperature", "Angle"]
    )
    
    if conversion_type == "Temperature":
        temp_conversion = st.radio("Convert", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        temp = st.number_input("Temperature", value=25.0, key="temp_input")
        
        if st.button("Convert", key="temp_calc"):
            if temp_conversion == "Celsius to Fahrenheit":
                result = mo.celsius_to_fahrenheit(temp)
                st.success(f"✅ {temp}°C = **{result:.2f}°F**")
            else:
                result = mo.fahrenheit_to_celsius(temp)
                st.success(f"✅ {temp}°F = **{result:.2f}°C**")
    
    else:  # Angle
        angle_conversion = st.radio("Convert", ["Degrees to Radians", "Radians to Degrees"])
        angle = st.number_input("Angle", value=180.0, key="angle_input")
        
        if st.button("Convert", key="angle_calc"):
            if angle_conversion == "Degrees to Radians":
                result = mo.degrees_to_radians(angle)
                st.success(f"✅ {angle}° = **{result:.6f} radians**")
            else:
                result = mo.radians_to_degrees(angle)
                st.success(f"✅ {angle} radians = **{result:.6f}°**")

elif category == "Percentages":
    st.markdown('<h2 class="category-header">💯 Percentage Calculations</h2>', unsafe_allow_html=True)
    
    operation = st.selectbox(
        "Select Operation",
        ["Calculate Percentage", "Percentage Of", "Percentage Change"]
    )
    
    if operation == "Calculate Percentage":
        col1, col2 = st.columns(2)
        with col1:
            part = st.number_input("Part", value=25.0, key="pct_part")
        with col2:
            whole = st.number_input("Whole", value=100.0, key="pct_whole")
        
        if st.button("Calculate", key="pct_calc1"):
            result = mo.percentage(part, whole)
            st.success(f"✅ {part} is **{result:.2f}%** of {whole}")
    
    elif operation == "Percentage Of":
        col1, col2 = st.columns(2)
        with col1:
            percent = st.number_input("Percentage", value=20.0, key="pct_percent")
        with col2:
            number = st.number_input("Number", value=150.0, key="pct_number")
        
        if st.button("Calculate", key="pct_calc2"):
            result = mo.percentage_of(percent, number)
            st.success(f"✅ {percent}% of {number} = **{result:.2f}**")
    
    elif operation == "Percentage Change":
        col1, col2 = st.columns(2)
        with col1:
            old_value = st.number_input("Old Value", value=100.0, key="pct_old")
        with col2:
            new_value = st.number_input("New Value", value=120.0, key="pct_new")
        
        if st.button("Calculate", key="pct_calc3"):
            result = mo.percentage_change(old_value, new_value)
            change_type = "increase" if result > 0 else "decrease"
            st.success(f"✅ Percentage {change_type}: **{abs(result):.2f}%**")
            st.info(f"From {old_value} to {new_value}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>" 
    "Built with ❤️ using Streamlit | Powered by math_operations module"
    "</div>",
    unsafe_allow_html=True
)
