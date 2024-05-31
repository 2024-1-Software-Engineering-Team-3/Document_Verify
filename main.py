from src.Verify_main import API_Document_Verify
import streamlit as st
import os
import time

ABSOLUTE_PATH = "./data"

def main():
    st.title('Document Verify Testing Tool')

    image = st.file_uploader("Upload your document (use data/test.jpg)", type=["jpg", "jpeg", "png"])

    if image is not None:
        # 이미지 파일이 업로드되었을 때
        image_path = os.path.join(ABSOLUTE_PATH, image.name)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        description = st.text_input("Write description")

        if st.button("Run"):
            if description:
                start_time = time.time()
                result, ocr_result = API_Document_Verify(image_path, description)
                end_time = time.time()
                
                st.write("## OCR Result:")
                st.write(ocr_result)
            
                st.write("## API Result:")
                st.write("API Result:", result)
                st.write("API Time Taken:", round(end_time - start_time, 2), "seconds")
            else:
                st.write("Fill both of the image and description")
    else:
        st.write("Please upload an image")

if __name__ == "__main__":
    main()