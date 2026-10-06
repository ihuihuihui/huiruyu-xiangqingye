# huiruyu-xiangqingye

辉如雨详情页设计是一个面向 Codex 的通用电商视觉工作流 skill：从产品素材和用户需求出发，完成竞品结构拆解、用户痛点提炼、详情页框架、逐屏文案、AI 生图提示、视觉验收和交付整理。

它不绑定任何具体品牌、IP、产品、品类或项目，可用于潮玩、家居、数码、文创、服饰、美妆及其他需要主图和长详情页的商品。技能会区分实拍、渲染图、风格参考和过时素材，要求产品结构、配件、尺寸和使用方式以当前任务中已确认的事实为准。

## 安装

将仓库克隆到 Codex 的 skills 目录：

```bash
git clone https://github.com/ihuihuihui/huiruyu-xiangqingye.git ~/.codex/skills/huiruyu-xiangqingye
```

如果你的 Codex 使用其他 skills 路径，请将仓库放入对应目录。仓库已经包含 skill 所需的说明、模板、脚本和 MIT 许可证，不需要额外安装 Python 包、字体、外部 skill 或项目文件。

## 使用

在 Codex 中调用：

```text
$huiruyu-xiangqingye
```

例如：

> 使用 $huiruyu-xiangqingye，根据我上传的产品图制作小红书商品详情页。

默认工作流包括：

1. 素材分级与产品事实锁定
2. 竞品详情页结构拆解
3. 用户痛点与购买动机提炼
4. 页面框架与逐屏文案
5. Style Lock 与逐图生图提示
6. 独立生成、逐张检查和必要重生
7. 文件命名、验证报告和交付清单

仓库内的 `references/` 保存竞品研究、文案结构、视觉生成和验收模板；`scripts/validate_assets.py` 用 Python 标准库检查 PNG 数量、尺寸和比例。

## 运行依赖说明

本仓库没有需要通过 pip、npm 或其他包管理器安装的运行依赖。

- `scripts/validate_assets.py` 只使用 Python 3 标准库。
- 图像生成、图片查看和联网研究由 Codex 当前运行环境提供，不属于本仓库的第三方依赖，也不需要另行购买或安装许可证。
- 如果当前运行环境暂不支持某项能力，skill 会输出可执行的 Prompt、研究表和验收记录，不会把未执行的动作写成已完成。

更详细的边界和许可说明见 [DEPENDENCIES.md](DEPENDENCIES.md)。

## 事实与视觉原则

- 产品实拍优先于效果图，用于锁定真实结构、配件、连接方式和表面状态。
- 风格参考只学习版式、光影、色彩和信息组织，不复制品牌、文案或未经授权的画面。
- 用户要求成品图时，每张最终图独立生成并单独验收，不能用本地拼贴代替成品图。
- 具体材质、工艺特征、尺寸和使用限制只按当前任务的事实账本表达。
- 没有真实评价、销量、认证或背书证据时，不把推测写成事实。

## 目录

```text
SKILL.md
agents/openai.yaml
references/
scripts/validate_assets.py
DEPENDENCIES.md
LICENSE
```

## 许可证

本项目使用 MIT License，详见 [LICENSE](LICENSE)。
