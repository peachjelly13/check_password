import re
import streamlit as st
st.set_page_config(page_title="Password Check",page_icon=":tada",layout="wide")
js_code = f"""
    <script>
        document.body.style.backgroundColor = 'blue';
    </script>
"""
st.markdown(js_code, unsafe_allow_html=True)



with st.container():
    st.subheader("This is Your friendly Password :blue[Consultant]")
    st.title("A :red[Password] Designer Just For You.")
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        
        st.header("-We Help You Create The Best :blue[Password] For Yourself :sunglasses:")
        st.write("##")
 
        st.write(
            """
            **Some Steps We suggest For A :green[Strong Password]**
            - Minimum Characters: :red[10-12]
            - Have A Mix Of  :blue[Uppercase] , :blue[Lowercase] And :blue[Special Characters]
            - Try To Add :green[Digits]
            - Please Avoid Using :violet[Spaces]
            - Please do not use the same password at :red[multiple places]
            
            

            """
        )
        st.write(
            """ 
            ***Guidelines To Use :blue[This Platform]***
            - Enter your password in the input box.
            - Press the :blue[Validate Password button] to check if your password is valid.
            - Press the :green[Clear button] to clear everything from the screen 

            **:rainbow[Please enter your Password]:**


            """
        )

special_char = re.compile('[@_!$%^&*()<>??|\/}{~:]')
verdict = False

def generate(password):
    global verdict
    val = True
    if(len(password)<10):
        st.write("**:red[Problem] : Password Is Too Small**")
        st.write("**:green[Solution] : Please Increase The Length Of Your Password**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        verdict = False
        val = False
    elif(password.isupper()):
        st.write("**:red[Problem] : Password Has No Lower Case Letters**")
        st.write("**:green[Solution] : Please Increase The Number Of Lower Case Letters**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        verdict = False
        val = False
    elif(password.islower()):
        st.write("**:red[Problem] : Password Has No Upper Case Letters**")
        st.write("**:green[Solution] : Please Increase The Number Of Upper Case Letters**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        val = False
        verdict = False
    elif(password.isnumeric()):
        st.write("**:red[Problem] : Password Has Only Numbers**")
        st.write("**:green[Solution] : Please Add Letters**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        val = False
        verdict = False
    elif(password.isalpha()):
        st.write("**:red[Problem] : Password Has Only Alphabets Add Numbers**")
        st.write("**:green[Solution] : Please Add Numbers**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        val = False
        verdict = False
    elif(special_char.search(password)==None):
        st.write("**:red[Problem] : Password Has No Special Characters**")
        st.write("**:green[Solution] : Please Add Special Characters**")
        st.write("**:violet[Verdict] : Password Not Accepted**")
        st.write("**:blue[Please Try Again]**")
        val = False
        verdict = False
    if(val==True):
        verdict = True
        st.write("**Good Job Chosing A Strong Password**")
    
        


if "my_text" not in st.session_state:
    st.session_state.my_text = ""

def submit():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""

st.text_input("Enter text here", key="widget", on_change=submit)

input_= st.session_state.my_text

st.write(" :rainbow[Your Password]: "+ input_)
if st.button("Validate Password"):
    if(input_):
        generate(input_)
        input_  = ""
if st.button("Clear"):
        input_ = " "





        
   


    
    






