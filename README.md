# ethprice
display the price of eth

为了随时掌握eth价格，又不想总是看着手机或者打开网页，就随手写了个显示eth价格的小软件（基于pyside2），想显示如btc等其他币种的朋友建议自行修改代码，很简单  
![pic](pic/ethprice.jpg)

## 注意
1、ethprice.py 为主程序，由于查询币价的火币网的域名国内网访问不畅，故加了一层代理（能流畅访问github的话，我默认你拥有代理的软件），但是一般代理端口为1080或1081，请根据自己情况自行修改  
2、ui_dis.py为qt界面的配置文件，无需改动  
3、releases的exe版本由pyinstaller编译，使用的端口号为889，如想使用不同端口，请自行编译


