from fastapi import FastAPI
import qrcode


app = FastAPI()








@app.post("/qrcode/")
async def generate(url: str):
    qr = qrcode.QRCode()
    file_path = "qrcode/qrcode.png"
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)

    return {"message":"QrCode Generate",
            "url":{url}}

