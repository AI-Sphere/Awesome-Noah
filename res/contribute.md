# 如何为开源贡献


<div align="center">
<font color="red"><b>学习道路千万条，帮助开源第一条。</b></font>
</div>
<br>
非常感谢，为此仓库做贡献非常非常简单！只需三步：

##### 1. 找到一个竞赛分享方案.
##### 2. Fork仓库然后克隆到本地，不用修改markdown文件，直接把您收集到的信息新增到文件夹`InfoCenter`对应的Json文件中即可。格式如下，非常简单.

截图为`InfoCenter/nlp.json`文件
![](https://aigroupz-1258285787.cos.ap-shanghai.myqcloud.com/blog/15505044191770.jpg)

|key|含义|
|----|----|
|id|数目标识符|
|title|竞赛名称|
|game link|竞赛官方链接|
|**solutions**|**您或他人分享的解决方案(非常重要)**|

##### 3.提PR.

可选项: 在您提PR之前，可以运行`python json_test.py`保证您修改后的json格式正确，python2/3均可运行。

PS: 收到您的PR，我们会运行`python run.py`生成最终readme文件(您也可以运行后再提PR)。

```
python run.py
```

## How to contribute

It's very easy to make a contribution for the repo!

1. Find a Shared Competition Solution.
2. Fill its info in the corresponding JSON file in folder `InfoCenter`, format is below.
3. pull request.


Optinal: Before you pull request, hope you can run `python json_test.py` to make sure you modify the Json file correctly. Support python 2/3.

Format:

|Name|Mean|
|----|----|
|id|Number of entries(not important)|
|title|game name|
|game link|game link|
|**solutions**|shared competition solutions from you or others(very important)|

