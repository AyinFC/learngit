Git教程
https://www.liaoxuefeng.com/wiki/896043488029600/898732864121440

常用命令：
把本地master分支的最新修改推送至GitHub：git push origin master
初始化一个Git仓库：git init


添加文件到Git仓库，分两步：


使用命令git add <file>，提交文件至暂存区；
使用命令git commit -m <message>，从暂存区提交至版本库


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

