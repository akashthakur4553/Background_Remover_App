import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO

st.set_page_config(layout="wide")


def main():
    st.title("AI Background Remover")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Remove Background"):
            # Remove background
            img_no_bg = remove(img)

            # Display edited image
            st.image(
                img_no_bg, caption="Image without Background", use_column_width=True
            )

            # Prepare the edited image for download
            img_format = "PNG"  # Explicitly set the format to PNG
            buffer = BytesIO()
            img_no_bg.save(buffer, format=img_format)
            buffer.seek(0)

            # Download button
            st.download_button(
                label="Download image without background",
                data=buffer,
                file_name=f"no_bg_image.{img_format.lower()}",
                mime=f"image/{img_format.lower()}",
            )


if __name__ == "__main__":
    main()
