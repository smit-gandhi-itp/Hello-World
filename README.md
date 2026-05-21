# Hello-World 🌍

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

My first repository on GitHub! This project demonstrates a comprehensive mathematical operations library with an interactive web interface built using Streamlit.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line](#command-line)
  - [Streamlit Web App](#streamlit-web-app)
- [Mathematical Operations](#mathematical-operations)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains:

1. **math_operations.py** - A comprehensive Python module with 50+ mathematical functions
2. **hello.py** - A command-line demonstration script
3. **streamlit_app.py** - An interactive web application for performing mathematical calculations

## ✨ Features

### Core Mathematical Library

- **Basic Arithmetic**: Addition, subtraction, multiplication, division, modulo, power operations
- **Advanced Math**: Square root, cube root, factorial, GCD, LCM, prime checking
- **Statistics**: Mean, median, mode, variance, standard deviation, range
- **Trigonometry**: Sine, cosine, tangent, and their inverse functions (in degrees)
- **Logarithms**: Natural log, log base 10, custom base logarithms
- **Geometry**: Area and volume calculations for circles, rectangles, triangles, spheres, cylinders
- **Conversions**: Temperature (Celsius ↔ Fahrenheit), Angle (Degrees ↔ Radians)
- **Percentages**: Calculate percentages, percentage of a number, percentage change

### Interactive Web Interface

- 🎨 **Modern UI**: Clean, responsive design with custom styling
- 📊 **Category-based Navigation**: Organized into 8 mathematical categories
- ✅ **Real-time Validation**: Input validation with helpful error messages
- 🧮 **Visual Feedback**: Color-coded results and informative displays
- 📱 **Mobile Responsive**: Works seamlessly on desktop and mobile devices

## 📁 Project Structure

```
Hello-World/
│
├── math_operations.py    # Core mathematical operations module (50+ functions)
├── hello.py              # Command-line demonstration script
├── streamlit_app.py      # Interactive Streamlit web application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/smit-gandhi-itp/Hello-World.git
cd Hello-World
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Command Line

Run the demonstration script to see various mathematical operations in action:

```bash
python hello.py
```

This will display:
- A "Hello World!" message
- Demonstrations of all mathematical operations
- Example outputs for each function category

### Streamlit Web App

Launch the interactive web application:

```bash
streamlit run streamlit_app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

#### Using the Web App

1. **Select a Category** from the sidebar:
   - Basic Arithmetic
   - Advanced Math
   - Statistics
   - Trigonometry
   - Logarithms
   - Geometry
   - Conversions
   - Percentages

2. **Enter Your Values** in the input fields

3. **Choose an Operation** from the dropdown menu

4. **Click Calculate** to see the result

## 🔢 Mathematical Operations

### Basic Arithmetic
```python
add(a, b)           # Addition
subtract(a, b)      # Subtraction
multiply(a, b)      # Multiplication
divide(a, b)        # Division
floor_divide(a, b)  # Floor division
modulo(a, b)        # Modulo operation
power(a, b)         # Exponentiation
```

### Advanced Math
```python
square_root(n)      # Square root
cube_root(n)        # Cube root
factorial(n)        # Factorial
absolute(n)         # Absolute value
gcd(a, b)           # Greatest common divisor
lcm(a, b)           # Least common multiple
is_prime(n)         # Prime number check
is_even(n)          # Even number check
is_odd(n)           # Odd number check
```

### Statistics
```python
mean(numbers)               # Average
median(numbers)             # Middle value
mode(numbers)               # Most frequent value
variance(numbers)           # Variance
standard_deviation(numbers) # Standard deviation
sum(numbers)                # Sum of all numbers
min(numbers)                # Minimum value
max(numbers)                # Maximum value
range(numbers)              # Range (max - min)
```

### Trigonometry (all angles in degrees)
```python
sine(angle)         # Sine function
cosine(angle)       # Cosine function
tangent(angle)      # Tangent function
arcsine(value)      # Inverse sine
arccosine(value)    # Inverse cosine
arctangent(value)   # Inverse tangent
```

### Logarithms
```python
natural_log(n)      # Natural logarithm (base e)
log_base_10(n)      # Logarithm base 10
log_base_n(n, base) # Logarithm with custom base
```

### Geometry
```python
circle_area(radius)                    # Area of circle
circle_circumference(radius)           # Circumference of circle
rectangle_area(length, width)          # Area of rectangle
rectangle_perimeter(length, width)     # Perimeter of rectangle
triangle_area(base, height)            # Area of triangle
sphere_volume(radius)                  # Volume of sphere
cylinder_volume(radius, height)        # Volume of cylinder
```

### Conversions
```python
celsius_to_fahrenheit(celsius)         # °C to °F
fahrenheit_to_celsius(fahrenheit)      # °F to °C
degrees_to_radians(degrees)            # Degrees to radians
radians_to_degrees(radians)            # Radians to degrees
```

### Percentages
```python
percentage(part, whole)                # Calculate percentage
percentage_of(percent, number)         # Find percentage of number
percentage_change(old_value, new_value) # Calculate percentage change
```

## 📸 Screenshots

### Web Application Interface

The Streamlit app features:
- **Sidebar Navigation**: Easy category selection
- **Input Forms**: User-friendly input fields with validation
- **Result Display**: Clear, color-coded results
- **Responsive Design**: Works on all screen sizes

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **Streamlit 1.28+**: Web application framework
- **Math Module**: Built-in Python mathematical functions
- **Statistics Module**: Built-in Python statistical functions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Ideas for Contributions

- Add more mathematical functions
- Improve the UI/UX of the Streamlit app
- Add unit tests
- Create visualizations for mathematical concepts
- Add support for complex numbers
- Implement matrix operations
- Add calculus functions (derivatives, integrals)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Smit Gandhi**

- GitHub: [@smit-gandhi-itp](https://github.com/smit-gandhi-itp)

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Streamlit team for creating an amazing framework
- All contributors who help improve this project

## 📞 Support

If you have any questions or run into issues, please:

1. Check the [Issues](https://github.com/smit-gandhi-itp/Hello-World/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much detail as possible

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

Made with ❤️ by Smit Gandhi

</div>
