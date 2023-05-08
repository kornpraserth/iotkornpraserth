from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, MessageAction,
    ButtonsTemplate, URIAction,
    CarouselTemplate, CarouselColumn)

import paho.mqtt.client as mqttClient
import time
import datetime
import schedule

ph = ""
def on_message(client, userdata, msg):
    global ph
    print(msg.topic+" "+str(msg.payload))
    text = msg.payload.decode('UTF-8')
    textsplit = text.split(',')
    ph    = textsplit[0]
    #t_and_h = text_t_h.split(',')
    #temp = t_and_h[0]
    #humi = t_and_h[1]

channel_secret = "c79551b1c8c824351b95a97c8baf025e"
channel_access_token = "8PYghpalnLFa6epdqVcwW7NjHodkQq/rB0vKIkqkQulP5y9An6OJfV7u6KioU0RgdMFwgArLXxdQmoNxoDkL/90NPvQHGDChjD2kOtELu5Jp3rrRn6D0j0xi3XeXk18qQkPZH+mmL+4OUAHCQo6AFAdB04t89/1O/w1cDnyilFU="

broker_address= "mqtt.netpie.io"
port = 1883

client = mqttClient.Client("ee869771-b52d-4093-b2de-47b5cfccbd6e") # Client ID
user = "LHr6HD34hU6vYiJUMPTts9SCSY1uByHa" # Token
password = "9r$lx(xOagVvESncEf$XX-*~ZEhYEDJo" # Secret              
client.username_pw_set(user, password=password)    
client.on_message = on_message

try:
    client.connect(broker_address, port=port)        
except:
    print("Connection failed")

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

####schedule####
#def job():
#    client.publish("@msg/Test01","servo on")
#    print("Hello World")
    
#schedule.every().day.at("13:54").do(job)
#schedule.every().day.at("13:55").do(job)


#while True:
#    schedule.run_pending()
################schedule end##############    
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    global ph
    text = event.message.text
    print(text)

    try:
        client.connect(broker_address, port=port)        
    except:
        print("Connection failed")
    

    if (text=="clean on"):
        client.publish("@msg/Test01","clean on")
        text_out = "Pump & UV is on now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="clean off"):
        client.publish("@msg/Test01","clean off")
        text_out = "Pump & UV is off now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="water pump on"):
        client.publish("@msg/Test01","water pump on")
        text_out = "Pump is on now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="water pump off"):
        client.publish("@msg/Test01","water pump off")
        text_out = "Pump is off now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="uv on"):
        client.publish("@msg/Test01","uv on")
        text_out = "UV is on now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="uv off"):
        client.publish("@msg/Test01","uv off")
        text_out = "UV is off now"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="ให้อาหารปลา"):
        client.publish("@msg/Test01","servo on")
        text_out = "ให้อาหารปลาเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon1_white"):
        client.publish("@msg/Test01","white")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon2_red"):
        client.publish("@msg/Test01","red")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon3_green"):
        client.publish("@msg/Test01","green")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon4_blue"):
        client.publish("@msg/Test01","blue")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon5_purple"):
        client.publish("@msg/Test01","purple")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon6_cyan"):
        client.publish("@msg/Test01","cyan")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon7_yellow"):
        client.publish("@msg/Test01","yellow")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="lon8_slidecolor"):
        client.publish("@msg/Test01","swap")
        text_out = "เปิดไฟเเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text[0]=="#"): 
        client.publish("@msg/Test01",text)
        text_out = "ส่งค่าสี " + text + " เเล้ว"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=="ขอทราบค่า PH"):
        client.subscribe("@msg/Test02")
        client.loop_start()
        time.sleep(1.5) 
        client.loop_stop()
        if len(ph) > 0 :
            text_out = "PH is " + ph 
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

    if (text=='Water filtration system'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='Water filtration system',text='ควมคุมการทำงานของ Water pump เเละ UV พร้อมๆกัน', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='สั่งเปิด ระบบกรอง',text='clean on'),
                MessageAction(label='สั่งปิด ระบบกรอง',text='clean off'),
                MessageAction(label='ย้อนกลับ', text='Clean')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        
    if (text=='Water pump'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='Water pump',text='ควมคุมการทำงานของ Water pump', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='สั่งเปิด Water pump',text='water pump on'),
                MessageAction(label='สั่งปิด Water pump',text='water pump off'),
                MessageAction(label='ย้อนกลับ', text='Clean')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='UV'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='UV',text='ควมคุมการทำงานของ UV', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='สั่งเปิด UV',text='uv on'),
                MessageAction(label='สั่งปิด UV',text='uv off'),
                MessageAction(label='ย้อนกลับ', text='Clean')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='Clean'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='ควมคุมการทำงานของระบบกรอง',text='เลือกอุปกรณ์ที่จะควบคุม', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='ระบบกรอง',text='Water filtration system'),
                MessageAction(label='ปั้มน้ำ',text='Water pump'),
                MessageAction(label='ยูวี', text='UV')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='Light'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='ควบคุมรูปเเบบของเเสง',text='เลือกรูปเเบบของเเสง', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='Light01',text='ledon1'),
                MessageAction(label='Light02',text='ledon2'),
                MessageAction(label='Light03', text='ledon3')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='ledon1'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='ควบคุมรูปเเบบของเเสง',text='เลือกรูปเเบบของเเสง', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='white',text='lon1_white'),
                MessageAction(label='red',text='lon2_red'),
                MessageAction(label='green', text='lon3_green')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='ledon2'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='ควบคุมรูปเเบบของเเสง',text='เลือกรูปเเบบของเเสง', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='blue',text='lon4_blue'),
                MessageAction(label='purple',text='lon5_purple'),
                MessageAction(label='cyan', text='lon6_cyan')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if (text=='ledon3'):
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='ควบคุมรูปเเบบของเเสง',text='เลือกรูปเเบบของเเสง', actions=[
                # กำหนด MessageAction ได้ไม่เกิน 3 ตัวเลือก
                MessageAction(label='yellow',text='lon7_yellow'),
                MessageAction(label='slidecolor',text='lon8_slidecolor'),
                MessageAction(label='back', text='ledon1')]),
            
        ])
        template_message = TemplateSendMessage(alt_text='test',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)


'''
    client.subscribe("@msg/Test01")
    client.loop_start()
    time.sleep(1.5) 
    client.loop_stop()
    if len(ph) <=4 :
        text_out = "PH is " + ph + "!!!อันตราย PH มีความเป็นกรดสูง!!!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    elif len(ph) >=11 :
        text_out = "PH is " + ph + "!!!อันตราย PH มีความเป็นด่างสูง!!!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
'''

'''
    if (text=='Clean'):
        text_show = 'คุณต้องการควบคุมการทำงานใดบ้าง'
        # กำหนดได้ไม่เกิน 4 ตัวเลือก
        buttons_template = ButtonsTemplate(
            title='Clean Menu', text=text_show,
            thumbnail_image_url = img_url,actions=[
                MessageAction(label='Water filtration system', text='คุณเลือก Water filtration system'),
                MessageAction(label='Water pump', text='คุณเลือก Water pump'),
                MessageAction(label='UV', text='คุณเลือก UV'),
                URIAction(label='เข้าดูเว็บไซต์',uri='http://ee.eng.su.ac.th')])

        template_message = TemplateSendMessage(alt_text=text_show,
                                               template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
'''
                     
if __name__ == "__main__":          
    app.run()

