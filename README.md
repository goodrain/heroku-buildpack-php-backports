# Heroku buildpack for PHP

云帮 PHP 源码构建的核心部分是基于[Heroku buildpack for PHP](http://devcenter.heroku.com/articles/buildpacks) 来实现的。

## 工作原理

当buildpack在您代码的根目录下检测到`index.php` 文件或者 `composer.json`文件，该程序语言类型被识别为PHP。buildpack使用`Composer`作为依赖管理器，并且我们提供多种PHP与HHVM的版本，还提供Apache和Nginx  web服务器。

## 文档

以下文章了解更多：

- [云帮支持PHP](http://www.rainbond.com/docs/stable/user-lang-docs/php/lang-php-overview.html)
- [运行时环境设置与调试](http://www.rainbond.com/docs/stable/user-lang-docs/php/lang-php-runtime.html)
- [如何在云帮部署ThinkPHP框架程序](http://www.rainbond.com/docs/stable/user-lang-docs/php/lang-php-thinkphp.html)

## 配置

在您的应用中至少有一个空的 `composer.json` 文件。
```bash
echo '{}' > composer.json
git add .
git commit -am "add composer.json for PHP app detection"
```

### 指定一个PHP版本

在`composer.json`文件中可指定使用PHP应用的相关依赖，例如指定`PHP 5.5.26`版本：

```
{
    "require": {"php": "5.5.26"}
}
```

## 授权

根据 MIT 授权证获得许可。 请参阅LICENSE文件
