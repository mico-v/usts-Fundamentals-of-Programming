1. 红楼梦与水浒传中人物统计并保存统计结果。：
小说内容保存在文本文件中，小说主要人物名字保存在文本文件中，每行一人。读取小说内容，通过第三方分词库jieba进行分词，统计主要人物在小说中出现的次数，然后将人物名字和出现次数按照从大到小的顺序保存到文件中。提示：
1）使用jieba.add_word(name)将人物名字添加到jieba自定义词库，提高分词准确率；
2）使用sorted(counts.items(), key=lambda x: x[1], reverse=True)按照出现次数从大到小排序。


2. CSV文件解析：手写数字数据集数据的解析：
MNIST数据集是机器学习和计算机视觉领域中最经典、最常用的基准数据集之一。它包含大量手写数字（0到9）的灰度图像，图像分辨率是28x28。MNIST数据集被转换为CSV格式时，包含以下特点：
1) 行：第一行是字段名，以后的每一行代表一张手写数字图像。
2) 列：第1列 (Label)是该图像对应的真实标签，即图像中手写数字的值（0到9）。第2列到第785列：代表图像的像素值（0~255）。一张28x28的图像共有784个像素。
要求编写Python程序读取CSV文件中的前10张手写数字图像，用字符方式输出手写字图像，即像素值非零时用字符#显示，零值时用空格显示，如下图所示：


3. 英文学习词典：
简明英汉词典保存在一个CSV文件中，文件名为dictionary.csv。第一列是英文单词，第二列是词性和中文解释。
要求编写一个Python程序，随机从词典中挑选50个单词，生成一个每日英文学习词典，并保存到文件study.txt，以便复制到手机上，有空时打开背单词。下图是英文学习词典示例：
resupply v.再供给，再补给
jambalaya n.什锦菜肴
tabernacular adj.临时房屋的
castaneous adj.栗色的
dowry n. 嫁妆，天资
acrogenous adj.顶生的
springhalt n.跛行症
greenbrier n.缐薔薇
cadastral adj.（记载地产产权，价值等供征税用的）土地清册的
armature n.盔甲，电枢（电机的部件），（动植物的防护器官)爪，牙齿
yenisei n.叶尼塞河（西伯利亚中部河流）
something pron.某事,某物adj.有点象，大约
range n.山脉，行列，范围，射程vt.排列，归类于，使并列，放牧vi.平行，延伸，漫游
ichthyol n.鱼油精
asiadollar n.（储入亚洲的银行并在亚洲各金融市场上流通的）亚洲美元[仿Eurodollar]
focal adj.焦点的，有焦点的，在焦点上的
multilevel n.多级
araucaria n.[植]南洋杉属树（原产南半球)
foppishly adv.浮华地，艳冶地
montenegrin adj. Montenegro的n. Montenegro
hibakusha [单复同]日>n，被炸者（指1945，年日本广岛和长崎遭原子弹轰炸后的幸存者）
renoiresque adj.（法国印象派画家)雷诺阿（作品）的
revisable adj.可修改的，可订正的
britannic adj.大不列颠的，英国的
marengo adj.［用手名词后[烹]马伦戈式的，油炸后加西红柿和蘑菇（以及大蒜、葡萄酒等）一起炖的
edible adj.可食用的
stopped v.停止，停下来vbl.停止，停下来
allochromatic adj.[物][化]杂质引起光化作用的，[矿]无色但含有色杂质之矿物的
succubus n.女妖，妓女，魔鬼
houseguest n.在家过夜或暂住的来客
suborbicular adj.近似圆形的
eudemonic adj.幸福的，幸福学的
pyelogram n.[医]肾孟X线(照）片，肾盂造影照片
cullion n. <舌>卑劣的人，痞子，环蛋
barracks n.兵营，许多人居住的简陋房舍
caravaggiesque adj.（意大利画家）卡拉瓦乔的，卡拉瓦乔作品[风格]的
livability n.（家禽，牲畜的）存活率，（住宅，环境的）适于居住性
hemostasia n.「医]正血，正血法
southpaw adj.用左手的n.用左手的运动员，左撇子
plumbic adj.铅的
asocial adj.缺乏社交性的，自我中心的，自私的
arsenious adj.[化]含砒素的，含砷的
dirtiness n.污秽，肮脏
drugger 吸毒者
coextension n.共同扩张，共同伸展
acuteness n. 敏锐，剧烈
viaticum n. 旅费，「宗]临终的圣餐
wady n.干容
anatolia n.安纳托利亚（亚洲西部半岛小亚细亚的旧称）
sapric adj.（土壤、土层）含极腐烂生物的