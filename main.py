import yttranscripts
import hft2
t = "https://en.wikipedia.org/wiki/Bharatanatyam"
opt = 2
v= "sAzL4XMke80"

if opt <= 1:
    print(hft2.hugging_face(t,opt))
elif opt == 2:
    print(hft2.hugging_face(yttranscripts.youtube_cap(v),0))
