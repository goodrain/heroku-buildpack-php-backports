# Rainbond buildpack for PHP

云帮提供PHP应用的buildpack是基于[Heroku buildpack](http://devcenter.heroku.com/articles/buildpacks) for PHP，它提供更加稳定高效的构建功能。buildpack使用`Composer`作为依赖管理器，提供使用PHP或HHVM作为进行时，还提供了Apache和Nginx这样的web服务器。

## 用法

在您的应用中至少有一个空的 `composer.json` 文件。
```bash
echo '{}' > composer.json
git add .
git commit -am "add composer.json for PHP app detection"
```
如果您还有来自其他框架或语言的文件，这些文件可能会触发其他buildpack检测您的应用程序。如：`package.json`可能导致您的代码被检测为`Node.js`应用程序，那么您需要手动设置您的应用来使用buildpack：
```bash
rainbond buildpacks:set https://github.com/heroku/heroku-buildpack-php
```
