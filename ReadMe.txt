Git教程
https://www.liaoxuefeng.com/wiki/896043488029600/898732864121440

出了解决不了的问题就把库删掉，在本地重新push一遍所有文件（仅限文件数不多的情况）

常用命令：
初始化一个Git仓库：git init
从GitHub克隆一个本地库:git clone <git@github.com:AyinFC/learngit.git>
把本地master分支的最新修改推送至GitHub：git push origin master

添加文件到Git仓库，分两步：


使用命令git add <file> 提交文件至暂存区；
使用命令git commit -m <'message'> 从暂存区提交至版本库


git tag <tagname> 打一个新标签（默认标签是打在最新提交的commit上的）
git tag  -a <v0.1> -m <"version 0.1 released"> <1094adb> 创建带有说明的标签，用-a指定标签名，-m指定说明文字
git tag <tagname> <commit_id> 对历史commit打标签
git tag 查看所有标签
git show <tagname> 查看标签信息




git status命令可以让我们时刻掌握仓库当前的状态
git diff可以查看修改内容


在版本的历史之间穿梭：git reset --hard <commit_id>
<commit_id>：版本号
git log可以查看提交历史，以便确定要回退到哪个版本
git reflog查看命令历史，以便确定要回到未来的哪个版本


git checkout -- <file>可以丢弃工作区的修改

命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：
一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态


删除文件：rm <file>

1.确实要从版本库中删除该文件，那就用命令git rm删掉，并且git commit -m <message>
2.删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本git checkout -- <file>
(git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”)

