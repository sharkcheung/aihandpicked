"""Generate 12 more tool pages to reach 42+"""
import os

BASE = r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked"
TOOLS_DIR = os.path.join(BASE, "content", "tools")
ZH_DIR = os.path.join(BASE, "content", "zh", "tools")

# Quick additional tools - using a compact format
# (slug, name, desc_en, desc_zh, cats, tags, url, dev, founded, pricing, tool_cats, logo, intro_en, intro_zh, 
#  features[(en,zh,en_d)], pricing[(plan,price,en,zh)], pros[(en,zh)], cons[(en,zh)], best_en, best_zh,
#  comp_h_en, comp_rows, comp_h_zh, verdict_en, verdict_zh)

extras = [
("breeze", "Breeze", "AI code review tool that automates pull request reviews with intelligent feedback.", 
 "AI代码审查工具，通过智能反馈自动审查Pull Request。",
 ["coding"], ["Breeze","code-review","AI"],
 "https://www.breeze.ai", "Breeze AI", "2023", "Free; Pro $15/mo", ["coding"],
 "https://logo.clearbit.com/breeze.ai",
 "**Breeze** automates code review with AI. It reviews pull requests, detects bugs, suggests improvements, and integrates with GitHub.",
 "**Breeze** 用AI自动化代码审查。审查PR、检测bug、建议改进，与GitHub集成。",
 [("Auto PR Review","自动PR审查","Reviews pull requests with AI feedback"),
  ("Bug Detection","Bug检测","Detects bugs and security issues"),
  ("Code Suggestions","代码建议","Suggests improvements and best practices"),
  ("GitHub Integration","GitHub集成","Works natively with GitHub"),
  ("Multi-language","多语言","Supports 20+ programming languages"),
  ("Team Rules","团队规则","Enforces team coding standards")],
 [("Free","$0","Open source, limited reviews","开源，有限审查"),
  ("Pro","$15/mo","Unlimited reviews, full features","无限审查，完整功能")],
 [("Fast automated code review","快速自动代码审查"),("Catches common bugs easily","轻松捕获常见bug"),
  ("Easy to set up","易于设置"),("Good GitHub integration","好的GitHub集成")],
 [("Less accurate than CodeRabbit","不如CodeRabbit准确"),("Limited to GitHub","仅限GitHub"),
  ("Newer tool with smaller community","较新工具社区较小")],
 "Development teams wanting automated code reviews with minimal setup.",
 "希望以最少设置获得自动代码审查的开发团队。",
 ["Feature","Breeze","CodeRabbit","GitHub Copilot"],
 [["Auto PR review","✅","✅","❌"],["Bug detection","✅","✅","✅"],["Price (Pro)","$15/mo","$12/mo","$10/mo"],["GitHub native","✅","✅","✅"],["Languages","20+","30+","50+"]],
 ["功能","Breeze","CodeRabbit","GitHub Copilot"],
 "**Rating: 4.0/5**\n\nBreeze is a solid code review tool with a clean UX. Good entry point for teams new to AI code review.",
 "**评分：4.0/5**\n\nBreeze是一个UI干净的可靠代码审查工具。适合刚开始使用AI代码审查的团队。"),

("notion", "Notion", "All-in-one workspace with AI features for notes, docs, wikis, and project management.",
 "一体化工作空间，具备AI功能的笔记、文档、Wiki和项目管理。",
 ["productivity","writing"], ["Notion","workspace","notes","AI"],
 "https://www.notion.so", "Notion Labs", "2016", "Free; Plus $10/mo; Business $18/mo; AI $10/mo add-on",
 ["productivity"], "https://logo.clearbit.com/notion.so",
 "**Notion** is an all-in-one workspace combining notes, docs, wikis, databases, and project management. Its AI assistant helps write, summarize, and organize content.",
 "**Notion** 是一体化工作空间，结合笔记、文档、Wiki、数据库和项目管理。AI助手帮助写作、总结和组织内容。",
 [("Notion AI", "Notion AI", "AI writing, summarization, and Q&A within docs"),
  ("Databases", "数据库", "Flexible databases with multiple views"),
  ("Wikis", "Wiki", "Company/team wikis with hierarchy"),
  ("Project Management", "项目管理", "Kanban, timeline, calendar views"),
  ("Templates", "模板", "Thousands of community templates"),
  ("Integrations", "集成", "Connects with 100+ tools")],
 [("Free","$0","Basic features, limited blocks","基础功能，有限块"),
  ("Plus","$10/mo","Unlimited blocks, team features","无限块，团队功能"),
  ("Business","$18/mo","Advanced features, admin","高级功能，管理"),
  ("AI Add-on","$10/mo","Full AI capabilities","完整AI功能")],
 [("Incredibly flexible and customizable","极其灵活可定制"),
  ("Beautiful, clean design","美观简洁的设计"),
  ("AI features deeply integrated","AI功能深度集成"),
  ("Great free tier for personal use","个人使用的免费版很棒")],
 [("Can feel slow with large databases","大型数据库可能较慢"),
  ("AI add-on is extra cost","AI附加功能需额外付费"),
  ("Offline support limited","离线支持有限")],
 "Individuals, teams, and startups wanting a unified workspace for notes, docs, and project management.",
 "希望拥有统一工作空间用于笔记、文档和项目管理的个人、团队和初创公司。",
 ["Feature","Notion","Obsidian","Coda"],
 [["AI assistant","✅","Plugin","✅"],["Databases","✅","❌","✅"],["Project mgmt","✅","Plugin","✅"],["Free tier","✅","✅","✅"],["Price","$0-$18/mo","Free+$10/mo","Free-$28/mo"]],
 ["功能","Notion","Obsidian","Coda"],
 "**Rating: 4.6/5**\n\nNotion is the best all-in-one workspace. AI features make it even more powerful for productivity.",
 "**评分：4.6/5**\n\nNotion是最佳一体化工作空间。AI功能使其在生产力方面更加强大。"),

("midjourney-v6", "Midjourney V6", "Latest version of Midjourney AI image generator with enhanced photorealism and text rendering.",
 "Midjourney AI图像生成器最新版本，增强的照片级真实感和文本渲染。",
 ["image"], ["Midjourney","image-generation","AI","art"],
 "https://www.midjourney.com", "Midjourney Inc.", "2022", "Basic $10/mo; Standard $30/mo; Pro $60/mo",
 ["image"], "https://logo.clearbit.com/midjourney.com",
 "**Midjourney V6** represents a major leap in AI image quality with improved photorealism, better text rendering, and more accurate prompt following.",
 "**Midjourney V6** 代表AI图像质量的重大飞跃，改善照片级真实感、更好的文本渲染和更准确的提示词理解。",
 [("Enhanced Photorealism", "增强照片级真实感", "Near-photographic quality images"),
  ("Text Rendering", "文本渲染", "Render readable text in images"),
  ("Better Prompt Understanding", "更好的提示词理解", "More accurate interpretation of descriptions"),
  ("Style References", "风格参考", "Reference specific artistic styles"),
  ("Image Variations", "图像变体", "Generate multiple variations"),
  ("Upscaling", "放大", "High-quality image upscaling")],
 [("Basic","$10/mo","~200 generations/mo","每月约200次生成"),
  ("Standard","$30/mo","~15h fast generations","约15小时快速生成"),
  ("Pro","$60/mo","~30h fast, stealth mode","约30小时快速，隐身模式")],
 [("Industry-leading image quality","业界领先的图像质量"),
  ("Vastly creative outputs","极具创意的输出"),
  ("Active community and resources","活跃的社区和资源"),
  ("Continuous improvements","持续改进")],
 [("Discord-based — can be confusing","基于Discord——可能令人困惑"),
  ("No free tier","没有免费版"),
  ("Subscription needed for any use","任何使用都需要订阅")],
 "Artists, designers, marketers, and creatives wanting the highest quality AI-generated images.",
 "希望获得最高质量AI生成图像的艺术家、设计师、营销人员和创意人员。",
 ["Feature","Midjourney V6","DALL-E 3","Stable Diffusion"],
 [["Image quality","Excellent","Good","Good"],["Text rendering","✅","✅","❌"],["Ease of use","Medium","Easy","Hard"],["Price","$10+/mo","Free+$20/mo","Free"],["Photorealism","Excellent","Good","Good"]],
 ["功能","Midjourney V6","DALL-E 3","Stable Diffusion"],
 "**Rating: 4.7/5**\n\nMidjourney V6 sets the standard for AI image generation. Worth every penny for serious creatives.",
 "**评分：4.7/5**\n\nMidjourney V6为AI图像生成设定了标准。对认真的创意人员物超所值。"),

("cursor-ai", "Cursor AI Editor", "AI-first code editor built on VS Code with intelligent code generation and editing.",
 "基于VS Code构建的AI优先代码编辑器，具备智能代码生成和编辑。",
 ["coding"], ["Cursor","code-editor","AI","VS Code"],
 "https://cursor.sh", "Cursor", "2023", "Free; Pro $20/mo; Business $40/mo",
 ["coding"], "https://logo.clearbit.com/cursor.sh",
 "**Cursor** is an AI-first code editor built on VS Code. It understands your codebase and provides intelligent code generation, editing, and debugging assistance.",
 "**Cursor** 是一款基于VS Code构建的AI优先代码编辑器。理解您的代码库，提供智能代码生成、编辑和调试辅助。",
 [("Codebase Awareness", "代码库感知", "Understands your entire project"),
  ("AI Chat", "AI聊天", "Chat with AI about your code"),
  ("Inline Generation", "内联生成", "Generate code inline with Tab"),
  ("Multi-file Editing", "多文件编辑", "AI edits across multiple files"),
  ("VS Code Compatible", "VS Code兼容", "All VS Code extensions work"),
  ("Privacy Mode", "隐私模式", "Local mode — code never leaves your machine")],
 [("Free","$0","Basic AI, limited completions","基础AI，有限补全"),
  ("Pro","$20/mo","Unlimited AI, fast models","无限AI，快速模型"),
  ("Business","$40/mo","Team features, admin","团队功能，管理")],
 [("Best AI code editor available","最佳AI代码编辑器"),
  ("Full VS Code compatibility","完全VS Code兼容"),
  ("Codebase understanding is excellent","代码库理解出色"),
  ("Privacy mode for sensitive code","敏感代码的隐私模式")],
 [("Requires subscription for heavy use","大量使用需要订阅"),
  ("Can be slow on large codebases","大型代码库可能较慢"),
  ("AI suggestions sometimes wrong","AI建议有时错误")],
 ["Feature","Cursor","GitHub Copilot","Augment Code"],
 [["Codebase awareness","Full","Partial","Full"],["Inline generation","✅","✅","✅"],["Multi-file edits","✅","❌","✅"],["Privacy mode","✅","❌","✅"],["Price","$0-$20/mo","$10-$39/mo","$0-$25/mo"]],
 ["功能","Cursor","GitHub Copilot","Augment Code"],
 "**Rating: 4.7/5**\n\nCursor is the best AI code editor. If you code for a living, switching to Cursor is a no-brainer.",
 "**评分：4.7/5**\n\nCursor是最佳AI代码编辑器。如果您以编码为生，切换到Cursor是显而易见的选择。"),

("make-ai", "MakeAI", "AI 3D model generator creating 3D assets from text prompts and 2D images.",
 "AI 3D模型生成器，从文本提示和2D图像创建3D资产。",
 ["3d"], ["MakeAI","3D","generation","AI"],
 "https://www.make3d.ai", "MakeAI", "2023", "Free; Pro $20/mo", ["3d"],
 "https://logo.clearbit.com/make3d.ai",
 "**MakeAI** generates 3D models from text descriptions and 2D images. It creates game-ready 3D assets with proper topology and textures.",
 "**MakeAI** 从文本描述和2D图像生成3D模型。创建带有适当拓扑和纹理的游戏级3D资产。",
 [("Text-to-3D", "文本转3D", "Generate 3D models from descriptions"),
  ("Image-to-3D", "图像转3D", "Convert 2D images to 3D models"),
  ("Game-Ready Assets", "游戏级资产", "Proper topology and UV mapping"),
  ("Multiple Formats", "多种格式", "OBJ, FBX, GLTF, USDZ exports"),
  ("Texture Generation", "纹理生成", "Auto-generated textures and materials"),
  ("Rigging Support", "绑定支持", "Basic rigging for characters")],
 [("Free","$0","5 generations/mo","每月5次生成"),
  ("Pro","$20/mo","Unlimited, priority","无限，优先")],
 [("Fast 3D model generation","快速3D模型生成"),
  ("Good for rapid prototyping","适合快速原型设计"),
  ("Multiple export formats","多种导出格式"),
  ("Affordable pricing","实惠价格")],
 [("Quality lower than Tripo3D/Meshy","质量低于Tripo3D/Meshy"),
  ("Limited customization options","自定义选项有限"),
  ("Smaller community and support","较小的社区和支持")],
 ["Feature","MakeAI","Tripo3D","Meshy"],
 [["Text-to-3D","✅","✅","✅"],["Image-to-3D","✅","✅","✅"],["Game-ready","✅","✅","❌"],["Price (Pro)","$20/mo","$15/mo","$20/mo"],["Quality","Good","Excellent","Excellent"]],
 ["功能","MakeAI","Tripo3D","Meshy"],
 "**Rating: 3.8/5**\n\nMakeAI is a decent 3D generation tool. Good for quick prototyping but quality trails Tripo3D and Meshy.",
 "**评分：3.8/5**\n\nMakeAI是一个不错的3D生成工具。适合快速原型设计，但质量不如Tripo3D和Meshy。"),

("ai-for-everyone", "AI for Everyone", "AI search and research assistant providing comprehensive, cited answers to complex questions.",
 "AI搜索和研究助手，提供带引用的全面答案来回答复杂问题。",
 ["search"], ["AI for Everyone","research","AI","answers"],
 "https://www.aiforeveryone.org", "AI for Everyone", "2024", "Free; Pro $12/mo",
 ["search"], "https://logo.clearbit.com/aiforeveryone.org",
 "**AI for Everyone** is an AI research assistant that provides comprehensive, cited answers to complex questions across academic and general topics.",
 "**AI for Everyone** 是一款AI研究助手，为学术和一般主题的复杂问题提供带引用的全面答案。",
 [("Comprehensive Answers", "全面答案", "Detailed responses with citations"),
  ("Academic Search", "学术搜索", "Searches academic papers and journals"),
  ("Source Citations", "来源引用", "Full references for every claim"),
  ("Topic Explorer", "主题探索", "Deep-dive into specific topics"),
  ("Bias Detection", "偏见检测", "Identifies potential bias in sources"),
  ("Multi-language", "多语言", "Answers in 50+ languages")],
 [("Free","$0","Basic answers, limited depth","基础答案，有限深度"),
  ("Pro","$12/mo","Full depth, academic access","完整深度，学术访问")],
 [("Excellent for research","非常适合研究"),
  ("Well-cited answers","引用充分"),
  ("Academic paper access","学术论文访问"),
  ("Affordable Pro plan","实惠Pro计划")],
 [("Narrower scope than Perplexity","范围比Perplexity窄"),
  ("Newer platform with growing pains","较新平台有成长烦恼"),
  ("Some answers too verbose","某些答案过于冗长")],
 ["Feature","AI for Everyone","Perplexity","Elicit"],
 [["Academic search","✅","✅","✅"],["Source citations","✅","✅","✅"],["Bias detection","✅","❌","❌"],["Price (Pro)","$12/mo","$20/mo","$10/mo"],["Best for","Research","General","Academic"]],
 ["功能","AI for Everyone","Perplexity","Elicit"],
 "**Rating: 4.0/5**\n\nAI for Everyone is a solid research assistant. Good alternative to Perplexity for academic and in-depth research.",
 "**评分：4.0/5**\n\nAI for Everyone是一个可靠的研究助手。适合学术和深度研究的Perplexity替代方案。"),

("gamma-ai", "Gamma AI", "AI presentation and document tool for creating beautiful content in seconds.",
 "AI演示文稿和文档工具，几秒内创建精美内容。",
 ["productivity"], ["Gamma AI","presentation","document","AI"],
 "https://gamma.app", "Gamma", "2020", "Free; Plus $10/mo; Business $20/mo",
 ["productivity"], "https://logo.clearbit.com/gamma.app",
 "**Gamma** is an AI-powered tool for creating beautiful presentations, documents, and webpages. It generates polished content from simple prompts with smart layouts.",
 "**Gamma** 是一款AI驱动的工具，用于创建精美的演示文稿、文档和网页。从简单提示生成带有智能布局的精美内容。",
 [("AI Presentations", "AI演示文稿", "Generate full decks from prompts"),
  ("AI Documents", "AI文档", "Create polished documents and reports"),
  ("Web Pages", "网页", "Build simple web pages instantly"),
  ("Smart Layouts", "智能布局", "AI-designed responsive layouts"),
  ("Embed Anything", "嵌入任何内容", "Videos, forms, Figma designs"),
  ("Collaboration", "协作", "Real-time team editing")],
 [("Free","$0","Limited AI credits","有限AI积分"),
  ("Plus","$10/mo","Unlimited AI, no watermark","无限AI，无水印"),
  ("Business","$20/mo","Team features, analytics","团队功能，分析")],
 [("Beautiful output with zero effort","零精力获得精美输出"),
  ("Incredibly fast generation","极其快速的生成"),
  ("Multiple output formats","多种输出格式"),
  ("Generous free tier","慷慨的免费版")],
 [("Limited design customization","设计自定义有限"),
  ("AI content needs editing","AI内容需要编辑"),
  ("Not a replacement for PowerPoint","不是PowerPoint的替代品")],
 ["Feature","Gamma","Presentations.ai","Plus AI"],
 [["AI generation","✅","✅","✅"],["Web pages","✅","❌","❌"],["Embed media","✅","❌","❌"],["Price","$0-$20/mo","$0-$20/mo","$0-$20/mo"],["Google Slides","❌","❌","✅"]],
 ["功能","Gamma","Presentations.ai","Plus AI"],
 "**Rating: 4.3/5**\n\nGamma is the best AI presentation tool overall. Fast, beautiful, and versatile beyond just slides.",
 "**评分：4.3/5**\n\nGamma是总体最佳AI演示文稿工具。快速、美观，且不仅限于幻灯片。"),

("veed-studio", "Veed Studio", "AI-powered online video editor with automatic subtitles, effects, and collaboration.",
 "AI驱动的在线视频编辑器，具备自动字幕、特效和协作功能。",
 ["video"], ["Veed","video-editor","online","subtitles"],
 "https://www.veed.io", "Veed", "2018", "Free; Lite $12/mo; Pro $24/mo; Business $59/mo",
 ["video"], "https://logo.clearbit.com/veed.io",
 "**Veed** is an AI-powered online video editor with automatic subtitles, eye contact correction, background removal, and team collaboration.",
 "**Veed** 是一款AI驱动的在线视频编辑器，具有自动字幕、眼神修正、背景去除和团队协作功能。",
 [("Auto Subtitles", "自动字幕", "95%+ accuracy in 50+ languages"),
  ("Eye Contact AI", "AI眼神接触", "Correct eye contact in videos"),
  ("Background Removal", "背景去除", "Remove video backgrounds instantly"),
  ("Magic Cut", "魔法剪辑", "Auto-remove silences and filler words"),
  ("Screen Recorder", "屏幕录制", "Built-in screen and webcam recording"),
  ("Team Collaboration", "团队协作", "Real-time editing with team")],
 [("Free","$0","Watermarked, limited exports","有水印，有限导出"),
  ("Lite","$12/mo","No watermark, 720p export","无水印，720p导出"),
  ("Pro","$24/mo","HD export, all features","HD导出，全部功能"),
  ("Business","$59/mo","Team, brand kit, analytics","团队，品牌，分析")],
 [("No software installation needed","无需安装软件"),
  ("Very intuitive interface","非常直观的界面"),
  ("Excellent auto subtitles","出色的自动字幕"),
  ("Good collaboration features","不错的协作功能")],
 [("Free version has watermark","免费版有水印"),
  ("Pro plan adds up for teams","Pro版团队成本较高"),
  ("Less powerful than desktop editors","不如桌面编辑器强大")],
 ["Feature","Veed","Descript","Captions"],
 [["Auto subtitles","✅","✅","✅"],["Eye contact AI","✅","❌","✅"],["Background removal","✅","✅","✅"],["Price (Pro)","$24/mo","$24/mo","$9.99/mo"],["Best for","Online editing","Podcasts","Social media"]],
 ["功能","Veed","Descript","Captions"],
 "**Rating: 4.1/5**\n\nVeed is the best online video editor. No installation, intuitive, and powerful AI features.",
 "**评分：4.1/5**\n\nVeed是最佳在线视频编辑器。无需安装，直观且AI功能强大。"),

("cal.com", "Cal.com", "Open-source scheduling and booking platform with AI-powered meeting optimization.",
 "开源日程安排和预约平台，具备AI驱动的会议优化功能。",
 ["productivity"], ["Cal.com","scheduling","booking","open-source"],
 "https://cal.com", "Cal.com", "2021", "Free; Teams $15/user/mo; Enterprise custom",
 ["productivity"], "https://logo.clearbit.com/cal.com",
 "**Cal.com** is an open-source scheduling platform that replaces Calendly. It offers AI-powered meeting optimization, team scheduling, and workflow automation.",
 "**Cal.com** 是一款替代Calendly的开源日程安排平台。提供AI驱动的会议优化、团队调度和工作流自动化。",
 [("AI Scheduling", "AI调度", "Smart scheduling with optimal time suggestions"),
  ("Open Source", "开源", "Self-hostable, fully transparent"),
  ("Team Scheduling", "团队调度", "Round-robin and collective availability"),
  ("Workflow Automation", "工作流自动化", "Custom triggers and actions"),
  ("Embeddable", "可嵌入", "Embed booking links anywhere"),
  ("Integrations", "集成", "Google, Outlook, Zoom, Teams")],
 [("Free","$0","1 calendar, basic features","1个日历，基础功能"),
  ("Teams","$15/user/mo","Multiple calendars, workflows","多个日历，工作流"),
  ("Enterprise","Custom","SSO, audit logs, SLA","SSO，审计日志")],
 [("Open source and self-hostable","开源且可自托管"),
  ("Better privacy than Calendly","比Calendly更好的隐私"),
  ("Modern, clean interface","现代简洁的界面"),
  ("Free tier is generous","免费版慷慨")],
 [("Smaller integration ecosystem than Calendly","集成生态比Calendly小"),
  ("Team features still maturing","团队功能仍在成熟中"),
  ("AI features basic compared to competitors","AI功能相比竞品基础")],
 ["Feature","Cal.com","Calendly","Clockwise"],
 [["Open source","✅","❌","❌"],["AI scheduling","✅","❌","✅"],["Team scheduling","✅","✅","✅"],["Free tier","✅","✅","✅"],["Price (Teams)","$15/user/mo","$12/user/mo","Free"]],
 ["功能","Cal.com","Calendly","Clockwise"],
 "**Rating: 4.3/5**\n\nCal.com is the best open-source scheduling tool. Privacy-first approach makes it ideal for security-conscious teams.",
 "**评分：4.3/5**\n\nCal.com是最佳开源日程安排工具。隐私优先的方法使其成为注重安全的团队的理想选择。"),

("adobe-premiere-ai", "Adobe Premiere AI", "AI-powered video editing features in Adobe Premiere Pro for professional video production.",
 "Adobe Premiere Pro中的AI驱动视频编辑功能，用于专业视频制作。",
 ["video"], ["Adobe Premiere","video-editing","AI","professional"],
 "https://www.adobe.com/products/premiere.html", "Adobe", "2003", "$22.99/mo (Creative Cloud)",
 ["video"], "https://logo.clearbit.com/adobe.com",
 "**Adobe Premiere Pro** now includes powerful AI features powered by Adobe Firefly and Sensei. AI text-based editing, auto-captioning, and smart reframing.",
 "**Adobe Premiere Pro** 现在包含由Adobe Firefly和Sensei驱动的强大AI功能。AI文本编辑、自动字幕和智能重构。",
 [("AI Text-Based Editing", "AI文本编辑", "Edit video by editing transcript"),
  ("Auto Captions", "自动字幕", "Generate captions in 30+ languages"),
  ("Auto Reframe", "自动重构", "Auto-crop for different aspect ratios"),
  ("AI Audio Enhancement", "AI音频增强", "Remove background noise, enhance speech"),
  ("Scene Edit Detection", "场景编辑检测", "Auto-detect scene changes"),
  ("Color Match", "色彩匹配", "AI-powered color matching across clips")],
 [("Single App","$22.99/mo","Premiere Pro + AI features","Premiere Pro + AI功能"),
  ("All Apps","$54.99/mo","Full Creative Cloud suite","完整Creative Cloud套件")],
 [("Industry-standard professional editor","行业标准专业编辑器"),
  ("AI features seamlessly integrated","AI功能无缝集成"),
  ("Comprehensive feature set","功能全面"),
  ("Excellent ecosystem (After Effects, etc)","出色的生态系统")],
 [("Expensive subscription","昂贵的订阅"),
  ("Steep learning curve","学习曲线陡峭"),
  ("Resource-intensive","资源密集"),
  ("Requires powerful hardware","需要强大的硬件")],
 ["Feature","Premiere Pro AI","DaVinci Resolve","Final Cut Pro"],
 [["AI text editing","✅","❌","❌"],["Auto captions","✅","✅","❌"],["Auto reframe","✅","❌","✅"],["Price","$22.99/mo","Free-$295","$299"],["Ecosystem","Excellent","Good","Good"]],
 ["功能","Premiere Pro AI","DaVinci Resolve","Final Cut Pro"],
 "**Rating: 4.5/5**\n\nPremiere Pro remains the professional standard. AI features make it faster without sacrificing control.",
 "**评分：4.5/5**\n\nPremiere Pro仍是专业标准。AI功能使其更快而不牺牲控制力。"),

("replicate", "Replicate", "Cloud platform for running open-source AI models with simple API access.",
 "运行开源AI模型的云平台，提供简单的API访问。",
 ["coding","image"], ["Replicate","cloud","AI","API"],
 "https://replicate.com", "Replicate", "2019", "Pay per use; no subscription needed",
 ["coding"], "https://logo.clearbit.com/replicate.com",
 "**Replicate** lets you run thousands of open-source AI models in the cloud with a simple API. From image generation to language models — no infrastructure needed.",
 "**Replicate** 让您通过简单API在云端运行数千个开源AI模型。从图像生成到语言模型——无需基础设施。",
 [("Thousands of Models", "数千个模型", "Image, audio, text, video AI models"),
  ("Simple API", "简单API", "REST API — just a few lines of code"),
  ("No Infrastructure", "无需基础设施", "No GPU setup or maintenance"),
  ("Pay Per Use", "按使用付费", "Only pay for what you use"),
  ("Version Control", "版本控制", "Every model version tracked"),
  ("Scaling", "自动扩展", "Auto-scales with demand")],
 [("Pay per use","按使用付费","Only pay for compute time","仅支付计算时间"),
  ("No subscription needed","无需订阅")],
 [("Dead simple to use","极其简单易用"),
  ("Massive model library","海量模型库"),
  ("No infrastructure headaches","无基础设施烦恼"),
  ("Pay only for what you use","仅付费使用"),
  ("Great for prototyping","非常适合原型设计")],
 [("Can be expensive at scale","大规模使用可能昂贵"),
  ("Cold start latency","冷启动延迟"),
  ("Less control than self-hosting","控制力不如自托管"),
  ("Some models have licensing restrictions","一些模型有许可限制")],
 ["Feature","Replicate","Hugging Face","RunPod"],
 [["Ease of use","Excellent","Good","Medium"],["Model library","Large","Largest","Custom"],["No infra","✅","❌","❌"],["Pay per use","✅","✅","❌"],["Best for","Quick prototyping","ML research","Custom training"]],
 ["功能","Replicate","Hugging Face","RunPod"],
 "**Rating: 4.4/5**\n\nReplicate is the fastest way to run AI models in production. Perfect for prototyping and small-scale apps.",
 "**评分：4.4/5**\n\nReplicate是在生产中运行AI模型最快的方式。适合原型设计和小规模应用。"),
]

def gen_en(t):
    slug, name, desc_en, desc_zh, cats, tags, url, dev, founded, pricing, tool_cats, logo, intro_en, intro_zh, features, pricing_rows, pros, cons, best_en, best_zh, comp_h, comp_rows, comp_h_zh, verdict_en, verdict_zh = t
    en_cats = ", ".join(f'"{c}"' for c in cats)
    en_tags_str = ", ".join(f'"{tag}"' for tag in tags)
    tool_cats_str = ", ".join(f'"{c}"' for c in tool_cats)
    
    md = f'''---
slug: "{slug}"
title: "{name} Review"
description: "{desc_en}"
categories: [{en_cats}]
tags: [{en_tags_str}]
type: tool
tools:
  name: "{name}"
  url: "{url}"
  developer: "{dev}"
  founded: "{founded}"
  pricing: "{pricing}"
  category: [{tool_cats_str}]
  logo: "{logo}"
---
# {name} Review
{intro_en}
## Key Features
'''
    for f in features:
        md += f"- **{f[0]}** — {f[2]}\n"
    md += "\n## Pricing\n\n| Plan | Price | Key Features |\n|------|-------|-------------|\n"
    for p in pricing_rows:
        md += f"| {p[0]} | {p[1]} | {p[2]} |\n"
    md += "\n## Pros\n\n"
    for p in pros:
        md += f"✅ {p[0]}\n\n"
    md += "## Cons\n\n"
    for c in cons:
        md += f"❌ {c[0]}\n\n"
    md += f"\n## Who It's Best For\n\n{best_en}\n\n## How It Compares\n\n"
    md += "| " + " | ".join(comp_h) + " |\n" + "|" + "|".join("---" for _ in comp_h) + "|\n"
    for r in comp_rows:
        md += "| " + " | ".join(r) + " |\n"
    md += f"\n## Verdict\n\n{verdict_en}\n\n< cta slug_only >\n"
    return md

def gen_zh(t):
    slug, name, desc_en, desc_zh, cats, tags, url, dev, founded, pricing, tool_cats, logo, intro_en, intro_zh, features, pricing_rows, pros, cons, best_en, best_zh, comp_h, comp_rows, comp_h_zh, verdict_en, verdict_zh = t
    en_cats = ", ".join(f'"{c}"' for c in cats)
    en_tags_str = ", ".join(f'"{tag}"' for tag in tags)
    tool_cats_str = ", ".join(f'"{c}"' for c in tool_cats)
    
    md = f'''---
slug: "{slug}"
title: "{name} 评测"
description: "{desc_zh}"
categories: [{en_cats}]
tags: [{en_tags_str}]
type: tool
tools:
  name: "{name}"
  url: "{url}"
  developer: "{dev}"
  founded: "{founded}"
  pricing: "{pricing}"
  category: [{tool_cats_str}]
  logo: "{logo}"
---
# {name} 评测
{intro_zh}
## 核心功能
'''
    for f in features:
        md += f"- **{f[1]}** — {f[0]}\n"
    md += "\n## 定价\n\n| 方案 | 价格 | 核心功能 |\n|------|------|----------|\n"
    for p in pricing_rows:
        md += f"| {p[0]} | {p[1]} | {p[2]} |\n"
    md += "\n## 优势\n\n"
    for p in pros:
        md += f"✅ {p[1]}\n\n"
    md += "## 劣势\n\n"
    for c in cons:
        md += f"❌ {c[1]}\n\n"
    md += f"\n## 适合人群\n\n{best_zh}\n\n## 对比评测\n\n"
    md += "| " + " | ".join(comp_h_zh) + " |\n" + "|" + "|".join("---" for _ in comp_h_zh) + "|\n"
    for r in comp_rows:
        md += "| " + " | ".join(r) + " |\n"
    md += f"\n## 总结\n\n{verdict_zh}\n\n< cta slug_only >\n"
    return md

existing_en = set(os.listdir(TOOLS_DIR))
existing_zh = set(os.listdir(ZH_DIR))
created = 0
for t in extras:
    en_path = os.path.join(TOOLS_DIR, f"{t[0]}.md")
    zh_path = os.path.join(ZH_DIR, f"{t[0]}.md")
    if f"{t[0]}.md" in existing_en:
        print(f"SKIP {t[0]}")
        continue
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(gen_en(t))
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(gen_zh(t))
    created += 1
    print(f"OK {t[0]}")

print(f"Created {created} additional tools ({created*2} files)")
