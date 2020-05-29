
# Настройка линукса

1. вход в вирутуальную машину под рутом
2. установка selinux `yum install –y policycoreutils-python`


3. включаем firewall `systemctl start firewalld.service`

4. установка sshd `yum install openssh openssh-server openssh-clients openssl-libs`

5. поднимаем демона sshd`systemctl start ssh.service`

6. устанавливаем nginx`yum install epel-release`
`yum install nginx`. 

7. запускаем nginx `systemctl start nginx.service`


8. настраиваем firewall 
`firewall-cmd --permanent --zone=public --add-service=http`
`systemctl restart firewalld.service`

* В папке прилагаются скрины экрана, где показан статус работающих nginx и sshd.

* Также предоставлен проброс портов для понимания, куда по http (8080 -> 80 ) идут запросы(смотреть скрин с пробросом портов)

* в папке приложен скрин экрана с рабоающим selinux, firewall, порты nginx и sshd 

* подключаемся к виртуальной машине через ssh происходит по 127.0.0.1:2222 -> 22) (смотреть скрин с пробросом портов)
