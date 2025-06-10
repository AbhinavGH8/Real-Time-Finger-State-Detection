import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()

mpdraw=mp.solutions.drawing_utils
prev=0
while True:
    success,img = cap.read()

    if not success:
        break
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        
        for mlandmark in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,mlandmark,mphands.HAND_CONNECTIONS)
            fingers=[] 
            if mlandmark.landmark[3].x < mlandmark.landmark[4].x:
                fingers.append("Thumb : up")
            else:
                fingers.append("Thumb : down")
                
            
            tips={8:"Index", 12: "Middle", 16: "Ring", 20: "Pinky"}
            for tip in tips:
                if mlandmark.landmark[tip].y > mlandmark.landmark[tip-2].y:
                    fingers.append(f"{tips.get(tip)} : down")
                else:
                    fingers.append(f"{tips.get(tip)} : up")
            fingerdict={}
            for finger in fingers:
                key,value = map(str.strip,finger.split(":"))
                fingerdict[key]=value
            noofup=0
            noofdown=0
            for key in fingerdict:
                if(fingerdict[key]=="up"):
                    isDown=False
                    noofup+=1
                elif(fingerdict[key]=="down"):
                    isUp=False
                    noofdown+=1
                  
            if fingers != prev:
                print(f"\033[36m\nPositions\033[0m: {fingers}")
                print(f"\033[32m{noofup}\033[0m fingers are up and \033[31m{noofdown}\033[0m fingers are down")

                if noofup==2 and fingerdict["Index"]=="up" and fingerdict["Middle"]=="up":
                    print("\n✌️ Peace")
                if noofup==5 :
                    print("\n👋 Hi there!")
                if noofdown==2 and fingerdict["Middle"] == "down" and fingerdict["Ring"]=="down":
                    print("\n🤘 Yo 😊")
                if noofup==1 and fingerdict["Index"]=="up":
                    print("\n1️⃣ No.1")
                if noofup==3 and fingerdict["Thumb"]=="down" and fingerdict["Pinky"]=="down":
                    print("\n3️⃣ No.3")
                if noofup==4 and fingerdict["Thumb"]=="down":
                    print("\n4️⃣ No.4")
                
            isDown=True                                   
            prev=fingers
            
    cv2.imshow("Example test",img)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()