import streamlit as st

# Define dictionaries to store student data for admission and graduation
admission_data = {
    "Yusuf Ibrahim": {"admission_year": 2001},
    "Godswill Joshua": {"admission_year": 2002},
    "Justice Adukwu": {"admission_year": 2001},
    "Marvin Jok": {"admission_year": 2003},
    "Maxwell Tanko": {"admission_year": 2002},
    "Kefas Gimba": {"admission_year": 2003},
    "Dang Samuel": {"admission_year": 2002},
    "Mafeng Dung": {"admission_year": 2003},
    "Henrietta Banny": {"admission_year": 2002},
    "Keziah Davou": {"admission_year": 2001},
    # Add more student data for admission as needed
}

graduation_data = {
    "Yusuf Ibrahim": {"graduation_year": 2007},
    "Godswill Joshua": {"graduation_year": 2008},
    "Justice Adukwu": {"graduation_year": 2007},
    "Marvin Jok": {"graduation_year": 2009},
    "Maxwell Tanko": {"graduation_year": 2008},
    "Kefas Gimba": {"graduation_year": 2009},
    "Mafeng Dung": {"graduation_year": 2009},
    "Henrietta Banny": {"graduation_year": 2008},
    "Keziah Davou": {"graduation_year": 2007},
    # Add more student data for graduation as needed
}

# Define the number of students in each class for three years
class_data = {
    "2007": {
        "Primary One": 108,
        "Primary Two": 80,
        "Primary Three": 97,
        "Primary Four": 60,
        "Primary Five": 113,
        "Primary Six": 75,
    },
    "2008": {
        "Primary One": 110,
        "Primary Two": 85,
        "Primary Three": 95,
        "Primary Four": 58,
        "Primary Five": 115,
        "Primary Six": 72,
    },
    "2009": {
        "Primary One": 112,
        "Primary Two": 88,
        "Primary Three": 93,
        "Primary Four": 62,
        "Primary Five": 118,
        "Primary Six": 70,
    },
}

# Display the logo at the top of the app
logo_image = 'C:/Users/Drex/Desktop/School App/logo.png'  # Update with the actual image file path
st.image(logo_image, use_column_width=True)

# Create the Streamlit app UI
st.title("School Admission and Graduation Checker")

# Input field to enter the student's name
student_name = st.text_input("Enter the student's name:")

# Input field to enter the admission year
admission_year = st.number_input("Enter the admission year:")

# Function to check admission and calculate graduation
def check_admission_and_calculate_graduation(student_name, admission_year):
    if student_name in admission_data:
        student_admission_year = admission_data[student_name]["admission_year"]
        if student_admission_year == admission_year:
            st.write(f"{student_name} was admitted in {admission_year} in Primary One.")
            
            # Check the last class of graduation
            last_graduation_class = None
            for year, classes in class_data.items():
                if student_name in graduation_data and graduation_data[student_name]["graduation_year"] == int(year):
                    last_graduation_class = next(reversed(classes))
            
            if last_graduation_class:
                st.write(f"{student_name} graduated in {last_graduation_class}.")
            else:
                st.write(f"{student_name} was unable to graduate.")
        else:
            st.write(f"{student_name} was not admitted in {admission_year}.")
    else:
        st.write(f"{student_name} not found in the admission data.")

# Button to check admission and calculate graduation
if st.button("Check Admission and Calculate Graduation"):
    check_admission_and_calculate_graduation(student_name, admission_year)

# Run the Streamlit app
if __name__ == '__main__':
    st.write("Thank You For Using Me")