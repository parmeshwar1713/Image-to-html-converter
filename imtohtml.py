from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
results = ocr.ocr(r"C:\Users\PiLog SSD\Desktop\gst files\V000429707.BMP",cls=True)
txtss = [[line[0][0],line[1][0]] for i,line in enumerate(results)]
planetext=[f"""<h6 style="position: absolute; top: {[i][0][0][1]}px; left: {[i][0][0][0]}px">{[i][0][1]}</h6>""" for i in txtss]
listToStr = ' '.join([str(elem) for elem in planetext])
f = open('helloworld.html','w')
message = f"""<html>
<head></head>
<body>
{listToStr}
</body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'helloworld.html'
# webbrowser.open_new_tab(filename)