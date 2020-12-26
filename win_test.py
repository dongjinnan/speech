import speech
import logging
logging.basicConfig(level=logging.DEBUG)

def callback(phr, phrase):
	if phr == phrase["closeMainSystem"]:
		speech.say("Goodbye.人机交互即将关闭，谢谢使用")
		speech.stoplistening()
		sys.exit()
	elif phr == phrase["film"]:
		speech.say("正在为您打开百度")
		webbrowser.open_new("http://www.baidu.com/")
	elif phr == phrase["cmd"]:
		speech.say("即将打开CMD")
		os.popen("C:\Windows\System32\cmd.exe")
		
def main():

	phrase = {
		"closeMainSystem" : "关闭人机交互",
		"film" : "我要看电影",
		"listenMusic": "我好累啊",
		"blog" : "看博客",
		"cmd" : "cmd"
	}
	
	while True:
		phrase = speech.input() # 接收语音
		speech.say("you said:" + phrase) # 说话
		if phrase == "turn off":
			break
	
	
if __name__=='__main__':
	main()