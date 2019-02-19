# 如何为开源贡献


<div align="center">
<font color="red"><b>学习道路千万条，帮助开源第一条。</b></font>
</div>
<br>
非常感谢，为此仓库做贡献非常简单！只需四步：

1. 点击右上角的*Fork*，让自己的repo列表里也有本项目
2. 点进`InfoCenter`文件夹，把您收集到的竞赛信息添加到对应的Json文件末尾
3. 在项目页面左侧，点击 New pull requests (可以百度一下如何发起pull requests)
4. 等管理员merge

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

