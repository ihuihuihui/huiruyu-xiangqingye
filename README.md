# huiruyu-xiangiqngye

辉如雨详情页设计是一个面向 Codex 的电商视觉工作流 skill：从产品素材和用户需求出发，完成竞品结构拆解、用户痛点提炼、详情页框架、逐屏文案、AI 生图提示、视觉验收和交付整理。

它适合潮玩、手办、3D 打印件、文创挂件以及其他需要主图和长详情页的产品。技能会区分实拍、渲染图、风格参考和过时素材，要求产品结构、配件、尺寸和使用方式以已确认事实为准。

## 安装

将仓库克隆到 Codex 的 skills 目录：

```bash
git clone https://github.com/ihuihuihui/huiruyu-xiangiqngye.git ~/.codex/skills/huiruyu-xiangiqngye
```

如果你的 Codex 使用其他 skills 路径，请将仓库放入对应目录。

## 使用

在 Codex 中调用：

```text
$huiruyu-xiangiqngye
```

例如：

> 使用 $huiruyu-xiangiqngye，根据我上传的产品图制作小红书商品详情页。

默认工作流包括：

1. 素材分级与产品事实锁定
2. 竞品详情页结构拆解
3. 用户痛点与购买动机提炼
4. 页面框架与逐屏文案
5. Style Lock 与逐图生图提示
6. 独立生成、逐张检查和必要重生
7. 文件命名、验证报告和交付清单

仓库内的 `references/` 保存竞品研究、文案结构、视觉生成和验收模板；`scripts/validate_assets.py` 用于检查图片数量、尺寸和比例。

## 事实与视觉原则

- 产品实拍优先于效果图，用于锁定真实结构、配件、连接方式和表面状态。
- 风格参考只学习版式、光影、色彩和信息组织，不复制品牌、文案或未经授权的画面。
- 每张最终图独立生成并单独验收，不能用本地拼贴代替成品图。
- 3D 打印层纹作为适度工艺提示，除非用户明确要求，不把它当作首屏卖点。
- 没有真实评价、销量、认证或背书证据时，不把推测写成事实。

## 目录

```text
SKILL.md
agents/openai.yaml
references/
scripts/validate_assets.py
```

## 许可证

本项目使用 MIT License，详见 [LICENSE](LICENSE)。
