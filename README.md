## lab.py

Windows:<br/>
该工具依赖opencv python库和Python3.<br/>
将要标注的图片放在frames文件夹下，先运行rename.py文件再运行lab.py文件，标完按s键保存并继续
注意：图片名不能包含中文

Linux:<br/>
Ubuntu 16.04下需要安装python-opencv来支持import cv2<br/>

## 其他说明
breakpoint.txt文件是记录断点，用来关闭程序后能够恢复原有位置<br/>
frames用来存放图片文件的文件夹，内部存放xml、和.xml.txt<br/>

## 快捷键:
- ESC:         关闭，程序会记住断点，所以再次打开也会还原回来
- s:           保存当前的记录，如果有画框、没画框都将保存xml文件和.xml.txt文件（主要便于python读取）
- 数字键1-9:   切换当前框定类别为定义的1-9类
- UP or <:     上一个图片
- DOWM or >:   下一个图片
- p:           删除前一个框定区域
