# 资源文件夹使用说明

在这里放入你的自建教学资源文件（HTML 互动课件、PDF 文档、图片等）。

## 使用方法

1. 把你的资源文件（如 `my_tool.html`）复制到这个文件夹
2. 打开 `admin.html` 管理页面
3. 在"链接地址"中填写 `resources/my_tool.html`
4. 生成 JSON 代码，复制到 `data/tools.json`

## 文件命名规则

- 使用英文或拼音命名
- 不要包含空格和特殊字符
- 推荐格式：`主题_内容.html`，如 `yuan_mianji.html`

## 示例

如果你的文件是 `resources/fenshu_qiang.html`，
在管理页面的"链接地址"中填写：
```
resources/fenshu_qiang.html
```

系统会自动识别为"本地资源"，并在卡片上显示绿色角标。
