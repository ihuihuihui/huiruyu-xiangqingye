# 依赖与许可说明

## 运行依赖

本 skill 仓库本身没有需要单独安装的 Python、Node.js、字体或外部资源依赖。

仓库内的验证脚本 `scripts/validate_assets.py` 只使用 Python 3 标准库，可直接运行：

```bash
python3 scripts/validate_assets.py /path/to/task-folder
```

## 宿主能力

图像生成、图像查看、联网搜索和文件操作由 Codex 当前宿主环境提供。这些能力不是本仓库打包的第三方依赖，使用者不需要为本仓库另行安装外部 skill、插件或许可证。宿主环境不支持某项能力时，skill 应明确交付可执行的文字方案或 Prompt，并标记未执行项。

## 第三方内容

仓库只包含本项目编写的 Markdown、YAML 和 Python 标准库脚本，没有复制第三方品牌素材、字体、图片或代码。用户上传的产品图、竞品页面和参考图仍由使用者负责确认其使用权限；本仓库不会为这些外部素材授予额外授权。

## 许可证

本项目代码、说明和模板使用 [MIT License](LICENSE)。MIT 许可只覆盖本仓库中的文件，不覆盖用户提供的素材、第三方页面内容或宿主平台能力。
