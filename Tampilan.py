import os
import time
b = '\x1b[1;34m'
m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
a = '\x1b[36;1m'
r = '\x1b[31m'
u = '\x1b[35m'
os.system('clear')
print(f'{b}╠══════════════════════════════════════════════════════════╣')
print(f'{b}║{r}░░░██████╗░██╗░░░██╗░░██████╗█████╗░██╗░░██╗██╗███╗░░░██╗░{b}║')
print(f'{b}║{r}░░░██╔══██╗██║░░░██║██╔════╝██╔══██╗██║ ██╔╝██║████╗░░██║░{b}║')
print(f'{b}║{r}░░░██████╔╝██║░░░██║██║░░░░░███████║█████╔╝░██║██╔██╗░██║░{b}║')
print(f'{b}║{r}░░░██╔══██╗██║░░░██║██║░░░░░██╔══██║██╔═██╗░██║██║╚██╗██║░{b}║')
print(f'{b}║{r}░░░██║░░██║╚██████╔╝╚██████╗██║░░██║██║░░██╗██║██║░╚████║░{b}║')
print(f'{b}║{r}░░░╚═╝░░╚═╝░╚═════╝░░╚═════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═══╝░{b}║')
print(f'{b}╠══════════════════════════════════════════════════════════╣')
print(f'{h}================{m} WELCOME TO TOOLS RUCAKIN {h}================{b}')
print(f'{b}        ╔════════════════════════════════════════╗')
print(f'        ║{u}  AUTHOR = CLOCK {b}                       ║')
print(f'        ║{u}  BY     = RUCAKIN {b}                     ║')
print('        ╠════════════════════════════════════════╣')
print(f'        ║{k} [1]{h}  TAMPILAN EROR                     {b}║')
print(f'        ║{k} [2]{h}  Tampilan Ubuntu                   {b}║')
print(f'        ║{k} [3]{h}  Tampilan Debian                   {b}║')
print(f'        ║{k} [4]{h}  Tampilan Kali Linux               {b}║')
print(f'        ║{k} [5]{h}  Tampilan Linux                    {b}║')
print(f'        ║{k} [6]{h}  Tampilan Arch                     {b}║')
print(f'        ║{k} [7]{h}  Tampilan Parrot                   {b}║')
print(f'        ║{k} [8]{h}  Tampilan Windows                  {b}║')
print(f'        ║{k} [9]{h}  Tampilan BlackArch                {b}║')
print(f'        ║{k} [10]{h} Tampilan MAlWARE                  {b}║')
print(f'        ║{k} [11]{m} Keluar                            {b}║')
print(f'        ╚════════════════════════════════════════╝{h}')
ha = input('└──╼PILIH NOMORNYA > ')
import time
import os

import os, time

if ha == '1':
    os.system('clear')

    # 🔊 puter MP3 (background)
    os.system('mpv https://c.top4top.io/m_3682rzqpo1.mp3 --no-video &')

    # 🔥 ASCII ERROR
    print(f"""{m}
███████╗██████╗ ██████╗  ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
{h}
{m}⚠ SYSTEM ERROR ⚠
AKSES DITOLAK
""")

    # ⏳ tunggu 5 detik
    time.sleep(5)

    # 🔇 matiin MP3
    os.system('pkill mpv')

    # ⌨️ baru minta ENTER
    input(f"{k}TEKAN ENTER BUAT BALIK{h}")

    # 🔁 balik ke Tampilan.py
    os.system('python Tampilan.py')
    exit()

elif ha == '2':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro ubuntu\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mUbuntu\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    os.system('cd')
    exit()
elif ha == '3':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro debian\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mDebian\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    os.system('cd')
    exit()
elif ha == '4':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro kali\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mKali☠️Linux\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    exit()
elif ha == '5':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro linux\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mLinux\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    os.system('cd')
    exit()
elif ha == '6':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro Arch\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mArch\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    os.system('cd')
    exit()
elif ha == '7':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro parrot\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mParrot\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('login')
    os.system('cd')
    exit()
elif ha == '8':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro windows\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mWindows\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('cd')
    os.system('login')
    exit()
elif ha == '9':
    bashrc_path = '/data/data/com.termux/files/usr/etc/bash.bashrc'
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install neofetch -y')
    os.system('pkg install git -y')
    with open(bashrc_path, 'w') as bashrc_file:
        bashrc_file.write('clear\n')
        bashrc_file.write('neofetch --ascii_distro BlackArch\n')
        bashrc_file.write("PS1='┌─(\\033[1;32mBlackArch\\033[0m)-[\\e[01;32m\\w\\e[00m]\\n└──╼ \\$ '\n")
    print('Konfigurasi selesai. Memulai ulang shell...')
    os.system('cd')
    os.system('login')
    exit()
elif ha == '10':
    os.system('bash -c "source /data/data/com.termux/files/usr/etc/bash.bashrc"')
    exit()
elif ha == '11':
    os.system('clear')
    print('Subscribe YT gw...')
    os.system('xdg-open https://www.youtube.com/@ilhamardi21')
    time.sleep(2)
    exit()
else:
    print(f'{m}Pilihan tidak valid!{h}')