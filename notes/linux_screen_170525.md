# screen 命令简单用法

## 新建一个Screen Session

```
$ screen -S screen_session_name
```

## 将当前Screen Session放到后台

```
$ screen -d screen_session_name
$ CTRL + A + D
```

## 列出所有Screen Session

```
$ screen -ls
```

## 唤起一个Screen Session

```
$ screen -r screen_session_name
```

## 分享一个Screen Session

```
$ screen -x screen_session_name
```

通常你想和别人分享你在终端里的操作时可以用此命令。

## 终止一个Screen Session

```
$ exit
$ CTRL + D
```

## 查看一个screen里的输出

当你进入一个screen时你只能看到一屏内容，如果想看之前的内容可以如下：

```
$ Ctrl + a ESC
```

