import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="QR Code Generator", page_icon="📱")

st.title("📱 QR Code Generator")
st.write("Enter any text or URL to generate a QR code.")

# User input
text = st.text_input("Enter Text", "Hello shree")

if st.button("Generate QR Code"):
    # Generate QR code
    qr = qrcode.make(text)

    # Display QR code
    st.image(qr, caption="Generated QR Code", use_container_width=False)

    # Save image to memory
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    # Download button
    st.download_button(
        label="📥 Download QR Code",
        data=buffer,
        file_name="qrcode.png",
        mime="image/png"
    )
