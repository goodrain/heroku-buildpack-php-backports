# Heroku buildpack for PHP

云帮 PHP 源码构建的核心部分是基于[Heroku buildpack for PHP](http://devcenter.heroku.com/articles/buildpacks) 来实现的。buildpack使用`Composer`作为依赖管理器，提供使用PHP或HHVM作为运行时，还提供了Apache和Nginx作为web服务器。

## 工作原理

## 文档

以下文章了解更多：

[云帮支持PHP]()

## 配置

在您的应用中至少有一个空的 `composer.json` 文件。
```bash
echo '{}' > composer.json
git add .
git commit -am "add composer.json for PHP app detection"
```

## 授权

根据 MIT 授权证获得许可。 请参阅LICENSE文件
