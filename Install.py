import os
import sys

def is_termux():
    return 'com.termux' in os.environ.get('PREFIX', '')

choice = input('[+] To install press (Y) to uninstall press (N) >> ')
run = os.system

if choice.lower() == 'y':
    if is_termux():
        prefix = os.environ.get('PREFIX')
        bin_path = os.path.join(prefix, 'bin', 'Web-Extractor')
        share_path = os.path.join(prefix, 'share', 'Web-Extractor')

        run('chmod 755 Web-Extractor.py')
        run(f'mkdir -p {share_path}')
        run(f'cp Web-Extractor.py {share_path}/Web-Extractor.py')

        termux_launcher = f'#! /data/data/com.termux/files/usr/bin/sh\nexec python3 {share_path}/Web-Extractor.py "$@"'
        with open(bin_path, 'w') as file:
            file.write(termux_launcher)

        run(f'chmod +x {bin_path} && chmod +x {share_path}/Web-Extractor.py')
        print('''\n\n[+] Web-Extractor installed successfully in Termux
[+] Now just type \x1b[6;30;42mwebextractor\x1b[0m in terminal''')

    else:
        if os.geteuid() != 0:
            print("Please run as root or with sudo")
            sys.exit(1)

        run('chmod 755 Web-Extractor.py')
        run('mkdir -p /usr/share/Web-Extractor')
        run('cp Web-Extractor.py /usr/share/Web-Extractor/Web-Extractor.py')

        linux_launcher = '#! /bin/sh\nexec python3 /usr/share/Web-Extractor/Web-Extractor.py "$@"'
        with open('/usr/bin/Web-Extractor', 'w') as file:
            file.write(linux_launcher)

        run('chmod +x /usr/bin/Web-Extractor && chmod +x /usr/share/Webb-Extractor/Web-Extractor.py')
        print('''\n\n[+] Web-Extractor installed successfully on Linux
[+] Now just type \x1b[6;30;42mWeb-Extractor\x1b[0m in terminal''')

elif choice.lower() == 'n':
    if is_termux():
        prefix = os.environ.get('PREFIX')
        run(f'rm -rf {prefix}/share/Web-Extractor')
        run(f'rm -f {prefix}/bin/Web-Extractor')
        print('[!] Web-Extractor removed from Termux successfully')
    else:
        if os.geteuid() != 0:
            print("Please run as root or with sudo")
            sys.exit(1)
        run('rm -rf /usr/share/Web-Extractor')
        run('rm -f /usr/bin/Web-Extractor')
        print('[!] Web-Extractor removed from Linux successfully')
