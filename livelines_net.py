import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import os
import numpy as np
from tensorflow.keras.models import model_from_json
import time
import json
import smtplib
import ssl
import mimetypes
from smtplib import SMTP_SSL
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email sender and receiver
file = open("credential.json")

data = json.load(file)

email_sender = data["email_sender"]
email_password = data["email_password"]
email_receiver = data["email_receiver"]


emailImage = "emailImage.png"

# Set the subject and body of the email
subject = 'Alert! One Fake Face is Detected'
body = """
Person using fake image...
"""

emailMessage = EmailMessage()
emailMessage = MIMEMultipart('alternative')
emailMessage['From'] = email_sender
emailMessage['To'] = email_receiver
emailMessage['Subject'] = subject
html = """\
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warning Page</title>
    <style>
        body {
            font-family: "Baloo Tamma 2", cursive;
            background: black;
            color: rgb(176, 28, 28);
        }

        h1 {
            padding-top: 6rem;
            text-align: center;
        }

        .mainSection {
            display: flex;
        }

        .image {
            padding-left: 25%;
            padding-top: 3rem;
            height: 175;
            width: 177;
        }

        .text {
            padding-left: 5rem;
            font-size: large;
        }
        @keyframes opa {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }
        #warning {
            filter: drop-shadow(0px 0px 10px red);
        }

        #Group7 {
            animation: opa 0.6s ease-in-out infinite alternate;
        }

        footer {
            padding-top: 5rem;
            font-family: "Baloo Tamma 2", cursive;
            color: rgb(227, 34, 34);
            opacity: 0.5;
        }

        .footer-items {
            padding-top: 10px;
            display: flex;
            color: rgb(253, 16, 51);
            justify-content: space-around;
        }
    </style>
</head>

<body style="background-color:black">
    <h1>Warning!!!</h1>
    <h1> Someone is Cheating</h1>

    <section class="mainSection">
        <div class="image">
            <svg width="177" height="175" viewBox="0 0 354 350" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g id="warning" clip-path="url(#clip0)" filter="url(#filter0_d)">
                    <path id="Vector" d="M23.1782 341.846C17.8761 339.739
                        12.9242 337.707 9.04747 332.727C2.36302 324.164 2.9344
                        315.623 7.2627 306.912C18.8775 283.523 30.8303 260.303
                        42.6694 237.025C65.5468 192.034 88.456 147.056 111.397
                        102.091C112.365 100.197 114.076 97.7929 115.83
                        97.4214C117.817 96.9824 120.997 97.9127 122.262
                        99.4171C123.38 100.746 123.251 103.955 122.49
                        105.865C120.677 110.39 118.155 114.63 115.937
                        118.996C104.813 140.876 93.6895 162.76 82.5672
                        184.647C70.1598 208.957 57.6357 233.205 45.2559
                        257.531C35.9849 275.748 26.8 294 17.701 312.288C12.6047
                        322.555 19.5103 329.046 28.468 330.136C29.6968 330.283
                        30.9593 330.163 32.2065 330.163C129.444 330.163 226.682
                        330.137 323.92 330.083C327.179 330.083 330.7 329.433
                        333.633 328.079C337.968 326.083 340.063 320.345 337.934
                        315.764C331.585 302.05 324.997 288.445 318.169
                        274.948C306.038 251.056 293.594 227.326 281.383
                        203.473C270.14 181.497 258.979 159.482 247.9
                        137.43C238.282 118.394 228.765 99.3127 219.122
                        80.2926C209.222 60.7721 199.273 41.2761 189.273
                        21.8047C188.584 17.313 183.694 11.2124 179.676
                        11.1418C176.911 11.0927 174.147 12.8519 171.36
                        13.8037C169.21 16.7296 166.633 19.4468 164.949
                        22.6276C160.034 31.9119 155.485 41.3867 150.751
                        50.7693C150.137 52.0158 149.123 53.0842 148.552
                        54.3522C146.745 58.365 143.455 58.8286 140.205
                        57.1154C136.679 55.2426 137.293 51.7364 138.669
                        48.6631C140.408 44.7731 142.395 40.9875 144.328
                        37.1927C148.19 29.5888 152.071 21.9941 155.97
                        14.4085C160.44 5.74742 167.004 0.125827 177.265
                        0.0152988C187.294 -0.0890891 194.16 5.13645 198.544
                        13.5673C211.556 38.6327 224.347 63.8208 237.142
                        88.9998C269.655 152.965 302.148 216.942 334.622
                        280.932C338.886 289.329 343.239 297.68 347.46
                        306.108C350.817 312.804 350.495 319.863 348.572
                        326.774C346.686 333.565 339.378 340.535 331.892
                        340.792H326.506C325.441 340.746 324.378 340.657 323.312
                        340.657C236.819 340.692 150.328 340.732 63.8378
                        340.777H28.6093L23.1782 341.846Z" fill="#F9F805" />
                    <g id="Group7">
                        <path id="Vector_2" d="M150.105 110.24C150.803
                                105.456 150.766 99.236 152.707 93.7065C156.507
                                82.8839 167.624 76.5654 179.857 77.0321C189.844
                                77.4128 201.074 85.512 203.431 95.7236C204.966
                                102.331 204.481 109.491 204.263 116.383C204.079
                                122.128 202.709 127.823 202.309 133.576C201.105
                                150.975 200.159 168.396 199.025 185.801C198.028
                                201.095 196.951 216.382 195.794 231.661C195.308
                                237.931 195.038 244.314 193.573 250.39C191.849
                                257.519 182.41 263.014 174.794 261.66C166.939
                                260.263 159.509 252.143 159.204 245.244C158.409
                                227.249 157.174 209.273 156.031 191.294C155.034
                                175.613 153.972 159.937 152.846 144.267C152.056
                                133.346 151.095 122.441 150.105 110.24ZM192.915
                                113.003L192.467 112.972C192.467 109.414 192.581
                                105.849 192.442 102.297C192.224 96.6907 189.567
                                92.6043 184.225 90.6547C172.736 86.4546 160.857
                                93.381 161.622 105.659C162.67 122.545 163.68
                                139.431 164.774 156.296C165.425 166.305 166.245
                                176.305 166.924 186.314C168.016 202.484 169.069
                                218.654 170.085 234.823C170.242 237.307 169.778
                                239.874 170.248 242.281C171.05 246.447 173.32
                                249.211 178.164 249.106C183.11 248.999 183.856
                                246.036 183.949 242.008C184.025 238.677 184.756
                                235.367 184.947 232.033C185.733 218.266 186.412
                                204.496 187.149 190.726C187.5 184.198 187.782
                                177.662 188.286 171.144C189.773 151.743 191.361
                                132.367 192.915 113.003Z" fill="#FAFA02" />
                        <path id="Vector_3" d="M177.556 318.401C165.839
                                    320.044 153.871 307.183 154.403
                                    295.78C155.017 282.725 164.485 273.174
                                    177.267 272.508C189.631 271.866 200.77
                                    283.56 200.822 295.534C200.868 306.292
                                    189.072 320.243 177.556 318.401ZM177.682
                                    306.618C183.362 306.652 189.214 301.245
                                    189.048 296.102C188.842 289.378 183.46
                                    284.079 176.944 284.187C171.415 284.279
                                    165.886 289.581 165.843 294.834C165.784
                                    301.177 171.2 306.569 177.682
                                    306.609V306.618Z" fill="#F9F804" />
                    </g>
                </g>
                <defs>
                    <filter id="filter0_d" x="0" y="0" width="354" height="351" filterUnits="userSpaceOnUse"
                        color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix" />
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0
                                            0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha" />
                        <feOffset dy="4" />
                        <feGaussianBlur stdDeviation="2" />
                        <feComposite in2="hardAlpha" operator="out" />
                        <feColorMatrix type="matrix" values="0 0 0 0 1 0
                                                            0 0 0 0 0 0 0 0 0 0
                                                            0 0 0.25 0" />
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow" />
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape" />
                    </filter>
                    <clipPath id="clip0">
                        <rect width="346" height="343" fill="white" transform="translate(4)" />
                    </clipPath>
                </defs>

            </svg>
        </div>
        <div class="text
                                                            container pt-5">
            <p>
                This email is to inform you that we have noticed some issues with recent performance the student in online class. We would like to bring to your attention , however, this behavior is unacceptable and needs to be addressed immediately.
            </p>
        </div>
    </section>

    <footer class="container
                                                        pt-5">
        <div class="footer-items">
            <div class="codezone">CMRCET</div>
            <div class="dbrocode">Batch - 34</div>
        </div>
    </footer>
</body>
"""
part2 = MIMEText(html, 'html')
emailMessage.attach(part2)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email


def sendEmail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, emailMessage.as_string())
    print("Email sent Successfully")


root_dir = os.getcwd()
# Load Face Detection Model
face_cascade = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml")
# Load Anti-Spoofing Model graph
json_file = open('antispoofing_models/antispoofing_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load antispoofing model weights
model.load_weights('antispoofing_models/antispoofing_model.h5')
print("Model loaded from disk")
# video.open("http://192.168.1.101:8080/video")
# vs = VideoStream(src=0).start()
# time.sleep(2.0)

video = cv2.VideoCapture(0)
timer = int(0)

while True:
    while (timer > 0):
        timer = timer-1
        time.sleep(1)
    try:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = frame[y-5:y+h+5, x-5:x+w+5]
            resized_face = cv2.resize(face, (160, 160))
            resized_face = resized_face.astype("float") / 255.0
            # resized_face = img_to_array(resized_face)
            resized_face = np.expand_dims(resized_face, axis=0)
            # pass the face ROI through the trained liveness detector
            # model to determine if the face is "real" or "fake"
            preds = model.predict(resized_face)[0]
            print(preds)
            if preds > 0.5:
                label = 'spoof'
                cv2.putText(frame, label, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              (0, 0, 255), 2)
                if timer <= 0:
                    timer = 10
                    sendEmail()
            else:
                label = 'real'
                cv2.putText(frame, label, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except Exception as e:
        pass
video.release()
cv2.destroyAllWindows()
