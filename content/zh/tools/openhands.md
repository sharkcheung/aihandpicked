---
title: "OpenHands — 开源AI软件开发助手"
date: 2026-06-17
draft: false
description: "OpenHands（前OpenDevin）是开源AI智能体，可以写代码、修复bug、协作处理GitHub issues。透明、可定制、可自托管。"
categories: ["ai-coding"]
tags: ["开源", "AI智能体", "OpenHands", "GitHub", "开发者工具"]
slug: "openhands"
---

# OpenHands

OpenHands（以前称为 OpenDevin）是一个开源 AI 软件开发助手，可以像人类开发者一样编写代码、修复错误并协作处理软件项目。基于 AI 辅助应该是透明、可定制且对每个人都可访问的信念，OpenHands 提供了完整的、可观察的系统，您可以本地运行或部署在自己的基础设施上。

OpenHands 真正特别之处在于其 AI 辅助方法：它不是黑盒 API，而是完整的、可观察的系统，您可以查看 AI 采取的每个操作，修改其行为，甚至将改进贡献回项目。从编写整个功能到修复 GitHub 问题以及重构代码库，OpenHands 代表了开源社区对专有 AI 编码工具的回应。

## 核心功能

- **全栈开发** — 跨整个技术栈编写前端、后端和数据库代码
- **GitHub 集成** — 自动获取问题、创建 PR 并响应代码审查
- **终端访问** — 可以运行命令、执行测试并与开发环境交互
- **多智能体架构** — 用于不同任务（编码、测试、研究）的专门智能体
- **人在回路** — 您可以在任何时刻干预、指导和纠正 AI
- **自托管** — 在本地或您自己的服务器上运行，实现完全控制和隐私
- **可扩展** — 用于添加自定义工具、智能体和功能的插件系统

## 价格方案

| 方案 | 价格 | 功能 |
|------|------|------|
| 自托管 | ¥0 | 完全访问权限，在您自己的硬件上运行 |
| 云版（Beta） | ¥0 | Beta期间免费，有限计算 |
| 专业版（计划） | 待定 | 增强计算，优先支持 |
| 企业版 | 联系我们 | 本地部署，SSO，专用支持 |

*注意：OpenHands 是开源软件。您可以免费在自己的硬件上运行它。云托管费用涵盖计算资源。*

## 优点 ✅

- 完全开源——检查、修改和自托管
- 可观察的 AI 操作——准确查看 AI 正在做什么
- 强大的 GitHub 集成——自动化问题解决
- 活跃的社区开发和贡献
- 无供应商锁定——您的数据和工作流程与您在一起
- 支持多个 LLM 后端（OpenAI、Anthropic、本地模型）

## 缺点 ❌

- 需要技术设置（Docker、API 密钥、配置）
- 质量取决于底层 LLM——需要好的模型才能出色
- 较年轻的项目——文档仍在改进
- 对于复杂、模糊的任务可能需要指导
- 如果使用云托管会产生计算成本

## 评分

⭐⭐⭐⭐ (4.4/5)

## 适合人群

希望 AI 编码辅助而无供应商锁定的开发者和团队：开源爱好者、注重隐私的组织、希望定制 AI 行为的公司，以及希望了解和修改 AI 工具工作方式的开发者。 also ideal for maintaining legacy projects where you need an AI that can understand and refactor large, complex codebases.

## 快速入门

1. 访问 [all-hands.dev](https://www.all-hands.dev) 查看文档
2. 使用 Docker 在本地安装 OpenHands
3. 配置您的 LLM 提供商（OpenAI/Anthropic/本地模型）
4. 开始使用开源 AI 开发助手

---

## 同类推荐

- [Windsurf](/zh/tools/windsurf/) — AI 原生 IDE
- [Claude Code](/zh/tools/claude-code/) — Anthropic 官方 CLI
- [Manus](/zh/tools/manus/) — 通用 AI 智能体
