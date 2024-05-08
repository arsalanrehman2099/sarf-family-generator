import re
import base64
from functions import *
import streamlit as st # type: ignore

font_bytes = base64.b64encode(open("assets/MUHAMMADIBold.ttf", "rb").read()).decode()

st.markdown("""
    <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        .stButton > button {
            margin: 0 auto;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def is_arabic(word):
    arabic_pattern = re.compile("[\u0621-\u064A\u0660-\u0669 ]+")
    return bool(arabic_pattern.fullmatch(word))


def main():
   
    show_original = False
    show_generated = False

    show_error = False
    error_text = ''
    
    st.title("Sarf Family Generator")

    st.markdown(f"""
            <style>
                @font-face {{
                    font-family: 'MuhammadI-Bold';
                    src: url('data:font/ttf;base64,{font_bytes}') format('truetype');
                }}
                .custom-font {{
                    font-family: 'MuhammadI-Bold', sans-serif;
                }}
                
            </style>
             """, unsafe_allow_html=True)
   
        
    with st.form("my_form"):

        
        # Input fields
        st.markdown("<p style='font-size:14px;margin-bottom:2px;'>Enter <span class='custom-font'>ف</span> letter:</p>", unsafe_allow_html=True)
        input_F = st.text_input("Enter ف letter:",max_chars=1,label_visibility='collapsed')

        st.markdown("<p style='font-size:14px;margin-bottom:2px;'>Enter <span class='custom-font'>ع</span> letter:</p>", unsafe_allow_html=True)
        input_I = st.text_input("Enter ع letter:",max_chars=1,label_visibility='collapsed')
        
        st.markdown("<p style='font-size:14px;margin-bottom:2px;'>Enter <span class='custom-font'>ل</span> letter:</p>", unsafe_allow_html=True)
        input_L = st.text_input("Enter ل letter:",max_chars=1,label_visibility='collapsed')
        
        dropdown = st.selectbox('Select Category:',('Big Families (8)', 'Small Families (6)'))

        # Buttons column layout
        col1, col2, col3 = st.columns(3)

        # Button to generate input families
        with col1:
            if st.form_submit_button("Generate Families"):
                
                if input_F and input_I and input_L:
                    if not is_arabic(input_F):
                        show_error = True
                        error_text = 'ف letter is not in arabic.'
                    elif not is_arabic(input_I):
                        show_error = True
                        error_text = 'ع letter is not in arabic'
                    elif not is_arabic(input_L):
                        show_error = True
                        error_text = 'ل letter is not in arabic'
                    else:
                        show_error = False
                        show_original = False
                        show_generated = True  
                else:
                    show_error = True
                    error_text = "Please fill in all the input fields."

        # Button to display original families
        with col2:
            if st.form_submit_button("Original Families"):
                show_original = True
                show_generated = False

        # Button to clear input
        with col3:
            if st.form_submit_button("Clear Data"):
                show_original = False
                show_generated = False
                
                
        if show_error:
            st.error(error_text)


    # --------- DISPLAYING FAMILIES --------- #
    if show_original:
        generate_families(category=dropdown)

    if show_generated:
        generate_families(category=dropdown, F=input_F, I=input_I, L=input_L)


def generate_families(category,F=None,I=None,L=None):

    
    if category == 'Big Families (8)':
        family_names = ['أَسْلَمَ','عَلَّمَ','جَاهَدَ','تَعَلَّمَ','تَسَاءَلَ','اِنْقَلَبَ','اِقْتَرَبَ', 'اِسْتَغْفَرَ']
        family_digits = ['IV','II','III','V', 'VI','VII', 'VIII', 'X']
    else:
        family_names = ['نَصَرَ', 'فَتَحَ', 'ضَرَبَ','سَمِعَ', 'حَسِبَ', 'كَرُمَ']
        family_digits = ['I', 'I', 'I','I', 'I', 'I']


    if F==None or I==None or L==None:
        if category == 'Big Families (8)':
            families = [aslama_family(), allama_family(), jahaada_family(),
                        taallama_family(), tasaala_family(),
                        inqalaba_family(), iqtaraba_family(), istagfara_family()]
        else:
            families = [nasara_family(), fataha_family(), dharaba_family(),
                        samiaa_family(), hasiba_family(), karuma_family(),]
    else:
        if category == 'Big Families (8)':
            families = [aslama_family(F,I,L), allama_family(F,I,L), jahaada_family(F,I,L),
                    taallama_family(F,I,L), tasaala_family(F,I,L),
                    inqalaba_family(F,I,L), iqtaraba_family(F,I,L), istagfara_family(F,I,L)]
        else:
            families = [nasara_family(F,I,L), fataha_family(F,I,L), dharaba_family(F,I,L),
                        samiaa_family(F,I,L), hasiba_family(F,I,L), karuma_family(F,I,L)]
    
    
    style = "style='font-size:25px;text-align:center;margin-bottom:20px;line-height: 55px;'"

    # st.markdown(f"""
    #         <style>
    #             @font-face {{
    #                 font-family: 'MuhammadI-Bold';
    #                 src: url('data:font/ttf;base64,{font_bytes}') format('truetype');
    #             }}
    #             .custom-font {{
    #                 font-family: 'MuhammadI-Bold', sans-serif;
    #             }}
    #         </style>
    #     """, unsafe_allow_html=True)

    
    for i,family in enumerate(families):

        st.markdown(f"<div style='text-align: center;margin-bottom:10px;'><h3>Family {family_digits[i]} – <span class='custom-font'>{family_names[i]}</span></h3></div>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col4:
            st.markdown(f"<p class='custom-font' {style}'>{family['past']}</p>", unsafe_allow_html=True)
            if i != 5:
                st.markdown(f"<p class='custom-font' {style}'>{family['past_passive']}</p>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<p class='custom-font' {style}'>{family['pres']}</p>", unsafe_allow_html=True)
            if i != 5:
                st.markdown(f"<p class='custom-font' {style}'>{family['pres_passive']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p class='custom-font' {style}'>{family['masdar']}</p>", unsafe_allow_html=True)
            if i != 5:
                st.markdown(f"<p class='custom-font' {style}'>{family['masdar']}</p>", unsafe_allow_html=True)
        with col1:
            st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_before_isms}</span> {family['ism_fail']}</p>", unsafe_allow_html=True)
            if i != 5:
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_before_isms}</span> {family['ism_mafool']}</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col3:
            if category == 'Big Families (8)':
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_commanding}</span> {family['commanding']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_commanding}</span><br/>{family['commanding']}</p>", unsafe_allow_html=True)
        with col2:
            if category == 'Big Families (8)':
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_forbidding}</span> {word_for_forbidding2} {family['forbidding']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_forbidding}</span><br/>{word_for_forbidding2} {family['forbidding']}</p>", unsafe_allow_html=True)
        with col1:
            if category == 'Big Families (8)':
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_time_place}</span> {family['time_place']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='custom-font' {style}'><span style='opacity:0.5;'>{word_for_time_place}</span><br/>{family['time_place']}</p>", unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        if i != len(families)-1: st.markdown("---")
        st.write("<br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
