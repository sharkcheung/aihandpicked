# Generate 42 new AI tool pages (EN + ZH)
# Run from: C:\Users\sharkcheung\.qclaw\workspace\aihandpicked

$tools = @(
    # AI Productivity
    @{
        slug = "shortwave"
        title = "Shortwave — Best AI Email Client"
        desc = "Complete review of Shortwave — AI-powered email client built on Gmail with smart sorting, AI replies, and inbox zero automation."
        zh_title = "Shortwave — 最佳AI邮件客户端"
        zh_desc = "Shortwave完整评测——基于Gmail的AI邮件客户端，智能分类、AI回复和收件箱清零自动化。"
        categories = @("writing","productivity")
        tags = @("Shortwave","email","productivity","Gmail")
        type_val = "tool"
        url = "https://shortwave.com"
        developer = "Shortwave (Ex-Google team)"
        founded = "2023"
        pricing = "Free; Pro $19/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/shortwave.com"
        intro = "**Shortwave** is an AI-powered email client built on top of Gmail. Created by a team of ex-Google engineers, it uses AI to categorize, prioritize, and even draft your emails automatically."
        zh_intro = "**Shortwave** 是一款基于Gmail的AI邮件客户端。由前谷歌工程师团队打造，利用AI自动分类、优先排序甚至自动起草邮件。"
        features = @(
            "**AI Email Sorting** — Automatically categorizes emails by importance and topic",
            "**AI Draft Replies** — Generates context-aware reply suggestions",
            "**Inbox Zero Automation** — AI helps archive and organize to reach inbox zero",
            "**Gmail Integration** — Works directly with your existing Gmail account",
            "**Daily Summary** — AI-generated daily email digest",
            "**Search Enhancement** — Natural language search across all emails"
        )
        zh_features = @(
            "**AI邮件分类** — 自动按重要性和主题分类邮件",
            "**AI起草回复** — 生成上下文感知的回复建议",
            "**收件箱清零自动化** — AI帮助归档和组织以实现收件箱清零",
            "**Gmail集成** — 直接使用现有Gmail账户",
            "**每日摘要** — AI生成的每日邮件摘要",
            "**搜索增强** — 支持自然语言搜索所有邮件"
        )
        pricing_table = @(
            @("Free","$0","Basic AI sorting, 1 account"),
            @("Pro","$19/mo","AI replies, unlimited accounts, priority support")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础AI分类，1个账户"),
            @("专业版","$19/月","AI回复，无限账户，优先支持")
        )
        pros = @(
            "Transforms chaotic Gmail inbox into organized workflow",
            "AI replies save significant time on routine emails",
            "Beautiful, intuitive interface",
            "Works with existing Gmail — no migration needed"
        )
        zh_pros = @(
            "将混乱的Gmail收件箱转变为有序的工作流程",
            "AI回复在常规邮件上节省大量时间",
            "美观直观的界面",
            "直接使用现有Gmail，无需迁移"
        )
        cons = @(
            "Gmail-only — no Outlook or other providers",
            "Pro plan is relatively expensive for an email tool",
            "AI replies sometimes need manual editing"
        )
        zh_cons = @(
            "仅支持Gmail——不支持Outlook等其他提供商",
            "Pro版对于邮件工具来说相对较贵",
            "AI回复有时需要手动编辑"
        )
        best_for = "Gmail power users, professionals drowning in email, and remote teams wanting AI-assisted inbox management."
        zh_best_for = "Gmail重度用户、被邮件淹没的专业人士，以及需要AI辅助收件箱管理的远程团队。"
        compare_headers = @("Feature","Shortwave","Superhuman","Notion Mail")
        compare_rows = @(
            @("AI email sorting","✅","✅","✅"),
            @("AI draft replies","✅","✅","✅"),
            @("Gmail native","✅","✅","❌"),
            @("Daily AI summary","✅","❌","❌"),
            @("Price (Pro)","$19/mo","$30/mo","$10/mo")
        )
        verdict = "Rating: 4.2/5`n`nShortwave is the best AI email client for Gmail users. The free tier is surprisingly capable, and Pro ($19/mo) is a game-changer for email-heavy professionals."
        zh_verdict = "评分：4.2/5`n`nShortwave是Gmail用户最佳的AI邮件客户端。免费版功能出人意料地强大，Pro版（$19/月）对邮件密集型专业人士来说是革命性的。"
        zh_compare_headers = @("功能","Shortwave","Superhuman","Notion Mail")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Productivity - tl;dv
    @{
        slug = "tldv"
        title = "tl;dv — Best AI Meeting Recorder"
        desc = "Complete review of tl;dv — AI meeting recorder that auto-transcribes, summarizes, and highlights key moments from Zoom, Google Meet, and Teams calls."
        zh_title = "tl;dv — 最佳AI会议录制工具"
        zh_desc = "tl;dv完整评测——AI会议录制工具，自动转录、总结并标记Zoom、Google Meet和Teams通话中的关键时刻。"
        categories = @("productivity")
        tags = @("tl;dv","meeting","transcription","productivity")
        type_val = "tool"
        url = "https://tldv.io"
        developer = "tl;dv"
        founded = "2020"
        pricing = "Free; Pro $12/mo; Business $20/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/tldv.io"
        intro = "**tl;dv** is an AI-powered meeting recorder that automatically transcribes, summarizes, and creates highlight reels from your video calls on Zoom, Google Meet, and Microsoft Teams."
        zh_intro = "**tl;dv** 是一款AI驱动的会议录制工具，可自动转录、总结并从Zoom、Google Meet和Microsoft Teams的视频通话中创建精彩集锦。"
        features = @(
            "**Auto Transcription** — Real-time transcription in 30+ languages",
            "**AI Summaries** — Instant meeting summaries with key decisions",
            "**Highlight Clips** — Create shareable video clips of key moments",
            "**Speaker Detection** — Automatically identifies who said what",
            "**CRM Integration** — Push summaries to Salesforce, HubSpot",
            "**Multi-platform** — Works with Zoom, Meet, Teams"
        )
        zh_features = @(
            "**自动转录** — 支持30多种语言的实时转录",
            "**AI摘要** — 即时生成包含关键决策的会议摘要",
            "**精彩片段** — 创建关键时刻的可分享视频片段",
            "**发言人识别** — 自动识别谁说了什么",
            "**CRM集成** — 将摘要推送到Salesforce、HubSpot",
            "**多平台支持** — 支持Zoom、Meet、Teams"
        )
        pricing_table = @(
            @("Free","$0","5 meetings/mo, basic transcription"),
            @("Pro","$12/mo","Unlimited meetings, AI summaries"),
            @("Business","$20/mo","Team features, CRM integration")
        )
        zh_pricing_table = @(
            @("免费版","$0","每月5次会议，基础转录"),
            @("专业版","$12/月","无限会议，AI摘要"),
            @("企业版","$20/月","团队功能，CRM集成")
        )
        pros = @(
            "Extremely accurate transcription",
            "Highlight clips are great for sharing",
            "Generous free tier for personal use",
            "Integrates with major meeting platforms"
        )
        zh_pros = @(
            "极其准确的转录",
            "精彩片段非常适合分享",
            "个人使用的免费版非常慷慨",
            "与主流会议平台集成"
        )
        cons = @(
            "Free tier limited to 5 meetings per month",
            "No native recording on desktop — browser-based only",
            "Some languages have lower accuracy"
        )
        zh_cons = @(
            "免费版每月仅限5次会议",
            "桌面端无原生录制——仅支持浏览器",
            "部分语言的准确度较低"
        )
        best_for = "Remote teams, sales teams, consultants, and anyone who needs to document and share meeting outcomes."
        zh_best_for = "远程团队、销售团队、顾问，以及任何需要记录和分享会议结果的人。"
        compare_headers = @("Feature","tl;dv","Otter.ai","Fireflies.ai")
        compare_rows = @(
            @("AI summaries","✅","✅","✅"),
            @("Video highlight clips","✅","❌","✅"),
            @("Free tier","5 meetings/mo","300 min/mo","800 min storage"),
            @("CRM integration","✅","❌","✅"),
            @("Price (Pro)","$12/mo","$17/mo","$10/mo")
        )
        verdict = "Rating: 4.3/5`n`ntl;dv is the best value meeting recorder. At $12/mo, it offers AI summaries, transcription, and highlight clips — outperforming pricier alternatives."
        zh_verdict = "评分：4.3/5`n`ntl;dv是性价比最高的会议录制工具。每月$12即可获得AI摘要、转录和精彩片段，表现优于更贵的替代品。"
        zh_compare_headers = @("功能","tl;dv","Otter.ai","Fireflies.ai")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Productivity - attio
    @{
        slug = "attio"
        title = "Attio — Best AI-Powered CRM"
        desc = "Complete review of Attio — AI-native CRM for modern teams with intelligent automation, relationship intelligence, and seamless workflows."
        zh_title = "Attio — 最佳AI驱动CRM"
        zh_desc = "Attio完整评测——面向现代团队的AI原生CRM，具备智能自动化、关系智能和无缝工作流。"
        categories = @("productivity")
        tags = @("Attio","CRM","productivity","sales")
        type_val = "tool"
        url = "https://attio.com"
        developer = "Attio"
        founded = "2019"
        pricing = "Free; Starter $49/seat/mo; Growth $79/seat/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/attio.com"
        intro = "**Attio** is an AI-native CRM designed for modern, fast-moving teams. It combines intelligent automation with relationship intelligence to help you manage contacts and deals effortlessly."
        zh_intro = "**Attio** 是一款专为现代快速团队设计的AI原生CRM。它将智能自动化与关系智能相结合，帮助您轻松管理联系人商机。"
        features = @(
            "**AI-Powered Data Entry** — Automatically enriches contact and company data",
            "**Smart Workflows** — AI-triggered automation based on deal stages",
            "**Relationship Mapping** — Visual maps of connections between contacts",
            "**Flexible Data Model** — Custom fields and views without rigid schemas",
            "**Real-time Sync** — Integrates with Gmail, Slack, calendar",
            "**AI Activity Summaries** — Auto-generates summaries of interactions"
        )
        zh_features = @(
            "**AI数据录入** — 自动丰富联系人和公司数据",
            "**智能工作流** — 基于商机阶段的AI触发自动化",
            "**关系图谱** — 联系人之间的可视化关系图谱",
            "**灵活数据模型** — 无需固定模式的自定义字段和视图",
            "**实时同步** — 与Gmail、Slack、日历集成",
            "**AI活动摘要** — 自动生成交互摘要"
        )
        pricing_table = @(
            @("Free","$0","Basic CRM, 1 user"),
            @("Starter","$49/seat/mo","AI automation, integrations"),
            @("Growth","$79/seat/mo","Advanced AI, team features")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础CRM，1个用户"),
            @("入门版","$49/席位/月","AI自动化，集成"),
            @("成长版","$79/席位/月","高级AI，团队功能")
        )
        pros = @(
            "Beautiful, modern interface that teams actually enjoy using",
            "AI automation saves hours on data entry",
            "Flexible enough for any workflow",
            "Strong integrations ecosystem"
        )
        zh_pros = @(
            "美观现代的界面，团队真正喜欢使用",
            "AI自动化节省大量数据录入时间",
            "足够灵活适应任何工作流",
            "强大的集成生态系统"
        )
        cons = @(
            "Relatively new — less established than Salesforce/HubSpot",
            "Starter plan pricing per seat adds up for larger teams",
            "Limited reporting compared to enterprise CRMs"
        )
        zh_cons = @(
            "相对较新——不如Salesforce/HubSpot成熟",
            "入门版按席位计费，大团队成本较高",
            "与大型CRM相比报告功能有限"
        )
        best_for = "Startups, SMBs, and modern teams that want a flexible, AI-powered CRM without the complexity of legacy systems."
        zh_best_for = "希望拥有灵活、AI驱动的CRM而无需传统系统复杂性的初创公司、中小企业和现代团队。"
        compare_headers = @("Feature","Attio","HubSpot","Salesforce")
        compare_rows = @(
            @("AI automation","✅","Partial","✅"),
            @("Modern UX","✅","✅","❌"),
            @("Setup time","<30 min","~1 hour","Days"),
            @("Price (entry)","Free","Free","$25/user/mo"),
            @("Custom fields","✅","✅","✅")
        )
        verdict = "Rating: 4.4/5`n`nAttio is the CRM for teams that hate CRMs. Its AI automation and modern design make it the best choice for startups and SMBs."
        zh_verdict = "评分：4.4/5`n`nAttio是给讨厌CRM的团队使用的CRM。其AI自动化和现代设计使其成为初创公司和中小企业的最佳选择。"
        zh_compare_headers = @("功能","Attio","HubSpot","Salesforce")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Productivity - linear
    @{
        slug = "linear"
        title = "Linear — Best AI Project Management"
        desc = "Complete review of Linear — AI-enhanced project management tool for software teams with smart issue tracking, automation, and roadmaps."
        zh_title = "Linear — 最佳AI项目管理工具"
        zh_desc = "Linear完整评测——面向软件团队的AI增强项目管理工具，智能问题跟踪、自动化和路线图规划。"
        categories = @("productivity","coding")
        tags = @("Linear","project-management","productivity","agile")
        type_val = "tool"
        url = "https://linear.app"
        developer = "Linear"
        founded = "2019"
        pricing = "Free; Standard $8/seat/mo; Plus $14/seat/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/linear.app"
        intro = "**Linear** is an AI-enhanced project management tool built for software teams. It combines beautiful design with intelligent automation to streamline issue tracking, sprint planning, and roadmapping."
        zh_intro = "**Linear** 是一款专为软件团队打造的AI增强项目管理工具。它将美观的设计与智能自动化相结合，简化问题跟踪、冲刺规划和路线图制定。"
        features = @(
            "**AI Issue Triage** — Auto-categorizes and assigns issues based on context",
            "**Smart Keyboard Shortcuts** — Full keyboard-driven workflow",
            "**Real-time Sync** — Instant updates across the entire team",
            **Cycles & Roadmaps** — Visual planning with drag-and-drop",
            "**Git Integration** — Auto-link PRs to issues, status updates on merge",
            "**AI Drafts** — Generate issue descriptions and specs from prompts"
        )
        zh_features = @(
            "**AI问题分类** — 根据上下文自动分类和分配问题",
            "**智能键盘快捷键** — 全键盘驱动的工作流",
            "**实时同步** — 全团队即时更新",
            "**周期与路线图** — 可视化拖拽式规划",
            "**Git集成** — 自动关联PR和问题，合并时更新状态",
            "**AI草稿** — 从提示词生成问题描述和规格说明"
        )
        pricing_table = @(
            @("Free","$0","Up to 10 users, basic features"),
            @("Standard","$8/seat/mo","Unlimited, advanced features"),
            @("Plus","$14/seat/mo","Priority support, admin features")
        )
        zh_pricing_table = @(
            @("免费版","$0","最多10个用户，基础功能"),
            @("标准版","$8/席位/月","无限用户，高级功能"),
            @("高级版","$14/席位/月","优先支持，管理功能")
        )
        pros = @(
            "Blazing fast — the fastest project management tool available",
            "Beautiful, minimal design that reduces clutter",
            "Excellent Git and GitHub/GitLab integration",
            "AI triage saves project managers significant time"
        )
        zh_pros = @(
            "极快——速度最快的项目管理工具",
            "美观简约的设计减少了杂乱",
            "出色的Git和GitHub/GitLab集成",
            "AI分类为项目经理节省大量时间"
        )
        cons = @(
            "Best suited for software teams — not ideal for non-tech projects",
            "Learning curve for teams used to Jira",
            "No built-in time tracking"
        )
        zh_cons = @(
            "最适合软件团队——不适合非技术项目",
            "习惯Jira的团队有学习曲线",
            "没有内置的时间追踪功能"
        )
        best_for = "Software engineering teams, product teams, and startups that want a fast, modern alternative to Jira."
        zh_best_for = "希望拥有Jira的快速现代替代方案的软件工程团队、产品团队和初创公司。"
        compare_headers = @("Feature","Linear","Jira","Asana")
        compare_rows = @(
            @("Speed","⚡ Extremely fast","Slow","Medium"),
            @("AI triage","✅","❌","❌"),
            @("Git integration","✅","✅","❌"),
            @("Free tier","✅ (10 users)","✅ (10 users)","✅ (10 users)"),
            @("Price (paid)","$8/seat/mo","$8/seat/mo","$11/user/mo")
        )
        verdict = "Rating: 4.6/5`n`nLinear is the best project management tool for software teams. It's fast, beautiful, and its AI features genuinely save time."
        zh_verdict = "评分：4.6/5`n`nLinear是软件团队最佳的项目管理工具。它快速、美观，其AI功能确实能节省时间。"
        zh_compare_headers = @("功能","Linear","Jira","Asana")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Productivity - ashby
    @{
        slug = "ashby"
        title = "Ashby — Best AI Recruitment Platform"
        desc = "Complete review of Ashby — AI-powered recruitment and ATS platform for modern hiring teams with intelligent sourcing and automation."
        zh_title = "Ashby — 最佳AI招聘平台"
        zh_desc = "Ashby完整评测——面向现代招聘团队的AI驱动招聘和ATS平台，具备智能寻源和自动化功能。"
        categories = @("productivity")
        tags = @("Ashby","recruitment","ATS","hiring")
        type_val = "tool"
        url = "https://ashbyhq.com"
        developer = "Ashby"
        founded = "2018"
        pricing = "Custom (contact for pricing)"
        category = @("productivity")
        logo = "https://logo.clearbit.com/ashbyhq.com"
        intro = "**Ashby** is an AI-powered Applicant Tracking System (ATS) and recruitment platform built for modern hiring teams. It combines intelligent sourcing, automation, and analytics to streamline the entire hiring pipeline."
        zh_intro = "**Ashby** 是一款为现代招聘团队打造的AI驱动申请人跟踪系统（ATS）和招聘平台。它将智能寻源、自动化和分析相结合，简化整个招聘流程。"
        features = @(
            "**AI Sourcing** — Automatically finds and ranks candidates from multiple sources",
            "**Smart Outreach** — AI-generated personalized outreach messages",
            "**Pipeline Analytics** — Real-time hiring funnel analytics with AI insights",
            "**Structured Interviews** — AI-assisted interview scorecards and feedback",
            "**Calendar Integration** — Seamless scheduling with Google/Outlook",
            "**Custom Workflows** — Fully customizable hiring stages and automations"
        )
        zh_features = @(
            "**AI寻源** — 自动从多个来源查找和排序候选人",
            "**智能触达** — AI生成的个性化触达消息",
            "**流程分析** — 实时招聘漏斗分析和AI洞察",
            "**结构化面试** — AI辅助面试评分卡和反馈",
            "**日历集成** — 与Google/Outlook无缝安排日程",
            "**自定义工作流** — 完全可定制的招聘阶段和自动化"
        )
        pricing_table = @(
            @("Starter","Custom","Core ATS, basic analytics"),
            @("Pro","Custom","AI sourcing, advanced analytics"),
            @("Enterprise","Custom","Full suite, dedicated support")
        )
        zh_pricing_table = @(
            @("入门版","联系定价","核心ATS，基础分析"),
            @("专业版","联系定价","AI寻源，高级分析"),
            @("企业版","联系定价","完整套件，专属支持")
        )
        pros = @(
            "Beautiful, intuitive interface that candidates and recruiters love",
            "Powerful AI sourcing reduces time-to-hire",
            "Excellent analytics and reporting",
            "Highly customizable workflows"
        )
        zh_pros = @(
            "美观直观的界面，候选人和招聘人员都喜欢",
            "强大的AI寻源缩短招聘周期",
            "出色的分析和报告功能",
            "高度可定制的工作流"
        )
        cons = @(
            "Pricing is custom — no self-serve plans",
            "Better suited for mid-market than enterprise",
            "Smaller integration ecosystem than Greenhouse/Lever"
        )
        zh_cons = @(
            "定价为定制——没有自助计划",
            "更适合中型市场而非企业级",
            "集成生态系统比Greenhouse/Lever小"
        )
        best_for = "Growing companies and mid-market teams that want a modern, AI-powered ATS without enterprise complexity."
        zh_best_for = "希望拥有现代化AI驱动的ATS而无需企业级复杂性的成长型公司和中等市场团队。"
        compare_headers = @("Feature","Ashby","Greenhouse","Lever")
        compare_rows = @(
            @("AI sourcing","✅","Partial","✅"),
            @("Modern UX","✅","✅","✅"),
            @("Self-serve pricing","❌","❌","❌"),
            @("Interview tools","✅","✅","✅"),
            @("Analytics","✅","✅","✅")
        )
        verdict = "Rating: 4.3/5`n`nAshby is the best-looking ATS on the market. Its AI sourcing and modern UX make it ideal for fast-growing companies."
        zh_verdict = "评分：4.3/5`n`nAshby是市场上最好看的ATS。其AI寻源和现代UX使其成为快速成长公司的理想选择。"
        zh_compare_headers = @("功能","Ashby","Greenhouse","Lever")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Productivity - decorwhisk
    @{
        slug = "decorwhisk"
        title = "DecorWhisk — Best AI Interior Design"
        desc = "Complete review of DecorWhisk — AI interior design tool that generates room redesigns, furniture suggestions, and style visualizations from photos."
        zh_title = "DecorWhisk — 最佳AI室内设计工具"
        zh_desc = "DecorWhisk完整评测——AI室内设计工具，从照片生成房间重新设计、家具建议和风格可视化。"
        categories = @("productivity","image")
        tags = @("DecorWhisk","interior-design","AI","home")
        type_val = "tool"
        url = "https://decorwhisk.com"
        developer = "DecorWhisk"
        founded = "2023"
        pricing = "Free credits; Pro $19/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/decorwhisk.com"
        intro = "**DecorWhisk** is an AI interior design tool that lets you upload photos of any room and get instant redesign suggestions with furniture, colors, and decor recommendations."
        zh_intro = "**DecorWhisk** 是一款AI室内设计工具，让您上传任何房间的照片，即可获得即时重新设计建议，包括家具、颜色和装饰推荐。"
        features = @(
            "**Room Redesign** — Upload a photo and get AI-generated room makeovers",
            "**Style Transfer** — Apply different interior design styles (modern, rustic, minimal)",
            "**Furniture Suggestions** — AI recommends furniture that fits your space",
            "**Color Palette** — Generates complementary color schemes",
            "**Budget Estimation** — Rough cost estimates for suggested designs",
            "**Multiple Rooms** — Kitchen, bedroom, living room, bathroom, office"
        )
        zh_features = @(
            "**房间重新设计** — 上传照片获得AI生成的房间改造",
            "**风格转换** — 应用不同的室内设计风格（现代、乡村、简约）",
            "**家具建议** — AI推荐适合您空间的家具",
            "**配色方案** — 生成互补的配色方案",
            "**预算估算** — 为建议设计提供粗略成本估算",
            "**多种房间** — 厨房、卧室、客厅、浴室、办公室"
        )
        pricing_table = @(
            @("Free","$0","Limited generations per month"),
            @("Pro","$19/mo","Unlimited generations, HD exports")
        )
        zh_pricing_table = @(
            @("免费版","$0","每月有限的生成次数"),
            @("专业版","$19/月","无限生成，高清导出")
        )
        pros = @(
            "See room changes before spending money",
            "Multiple design styles to explore",
            "Easy to use — just upload a photo",
            "Helpful for budget planning"
        )
        zh_pros = @(
            "在花钱之前先看到房间变化",
            "可探索多种设计风格",
            "简单易用——只需上传照片",
            "有助于预算规划"
        )
        cons = @(
            "Designs can be unrealistic — may not account for structural constraints",
            "Limited to visual suggestions — no architectural changes",
            "Furniture suggestions may not be available in your region"
        )
        zh_cons = @(
            "设计可能不现实——可能未考虑结构限制",
            "仅限视觉建议——不包含建筑变更",
            "家具建议可能在您所在地区不可用"
        )
        best_for = "Homeowners planning renovations, interior designers seeking inspiration, and real estate agents staging properties."
        zh_best_for = "计划装修的房主、寻求灵感的室内设计师，以及进行房屋布置的房地产经纪人。"
        compare_headers = @("Feature","DecorWhisk","Remodeled.ai","RoomGPT")
        compare_rows = @(
            @("AI room redesign","✅","✅","✅"),
            @("Furniture suggestions","✅","✅","❌"),
            @("Budget estimation","✅","❌","❌"),
            @("Multiple styles","✅","✅","✅"),
            @("Price (Pro)","$19/mo","$29/mo","$9/mo")
        )
        verdict = "Rating: 4.0/5`n`nDecorWhisk is a fun and practical tool for visualizing room changes. Great for brainstorming before committing to expensive renovations."
        zh_verdict = "评分：4.0/5`n`nDecorWhisk是一个有趣且实用的工具，用于可视化房间变化。在投入昂贵装修之前进行头脑风暴非常棒。"
        zh_compare_headers = @("功能","DecorWhisk","Remodeled.ai","RoomGPT")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - v0
    @{
        slug = "v0"
        title = "v0 — Best AI UI Code Generator"
        desc = "Complete review of v0 by Vercel — AI-powered UI code generator that creates production-ready React components from text prompts and screenshots."
        zh_title = "v0 — 最佳AI UI代码生成器"
        zh_desc = "v0 by Vercel完整评测——AI驱动的UI代码生成器，从文本提示和截图创建生产级React组件。"
        categories = @("coding")
        tags = @("v0","Vercel","React","UI","coding")
        type_val = "tool"
        url = "https://v0.dev"
        developer = "Vercel"
        founded = "2023"
        pricing = "Free (10 gen/mo); Premium $20/mo"
        category = @("coding")
        logo = "https://logo.clearbit.com/vercel.com"
        intro = "**v0** by Vercel is an AI-powered UI code generator that creates production-ready React/Next.js components from text descriptions and uploaded screenshots. It uses AI models to understand design intent and output clean, responsive code."
        zh_intro = "**v0** 由Vercel开发，是一款AI驱动的UI代码生成器，从文本描述和上传的截图创建生产级React/Next.js组件。它使用AI模型理解设计意图并输出整洁的响应式代码。"
        features = @(
            "**Text-to-UI** — Generate components from natural language descriptions",
            "**Screenshot-to-Code** — Upload a design screenshot and get matching code",
            "**Production-Ready** — Outputs clean React + Tailwind CSS code",
            "**Iterative Refinement** — Chat with AI to refine generated components",
            "**Component Library** — Access generated components in a personal library",
            **One-Click Deploy** — Deploy to Vercel instantly"
        )
        zh_features = @(
            "**文本转UI** — 从自然语言描述生成组件",
            "**截图转代码** — 上传设计截图获取匹配代码",
            "**生产就绪** — 输出整洁的React + Tailwind CSS代码",
            "**迭代优化** — 与AI对话完善生成的组件",
            "**组件库** — 在个人库中访问生成的组件",
            "**一键部署** — 即刻部署到Vercel"
        )
        pricing_table = @(
            @("Free","$0","10 generations/mo, basic components"),
            @("Premium","$20/mo","Unlimited generations, priority access")
        )
        zh_pricing_table = @(
            @("免费版","$0","每月10次生成，基础组件"),
            @("高级版","$20/月","无限生成，优先访问")
        )
        pros = @(
            "Incredibly fast UI prototyping",
            "Code quality is surprisingly high",
            "Perfect for React/Next.js developers",
            "Screenshot-to-code feature is magical"
        )
        zh_pros = @(
            "极其快速的UI原型设计",
            "代码质量出人意料地高",
            "非常适合React/Next.js开发者",
            "截图转代码功能非常神奇"
        )
        cons = @(
            "Limited to React/Next.js ecosystem",
            "Complex layouts may need manual refinement",
            "Free tier runs out quickly for active use"
        )
        zh_cons = @(
            "仅限于React/Next.js生态系统",
            "复杂布局可能需要手动调整",
            "活跃使用的免费额度很快用完"
        )
        best_for = "React developers, front-end engineers, and designers who want to rapidly prototype and build UI components."
        zh_best_for = "希望快速原型设计和构建UI组件的React开发者、前端工程师和设计师。"
        compare_headers = @("Feature","v0","Cursor","Bolt")
        compare_rows = @(
            @("UI specialization","✅","❌","✅"),
            @("Screenshot-to-code","✅","❌","❌"),
            @("React/Tailwind","✅","✅","✅"),
            @("Full app generation","❌","✅","✅"),
            @("Price","$0-$20/mo","$20/mo","$0-$20/mo")
        )
        verdict = "Rating: 4.5/5`n`nv0 is the best AI tool for generating UI components. If you work with React, it's an absolute must-have."
        zh_verdict = "评分：4.5/5`n`nv0是生成UI组件的最佳AI工具。如果您使用React，它是绝对必备的。"
        zh_compare_headers = @("功能","v0","Cursor","Bolt")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - bolt
    @{
        slug = "bolt"
        title = "Bolt — Best AI Full-Stack Developer"
        desc = "Complete review of Bolt by StackBlitz — AI full-stack development tool that generates, runs, and deploys complete web applications from natural language prompts."
        zh_title = "Bolt — 最佳AI全栈开发工具"
        zh_desc = "Bolt by StackBlitz完整评测——AI全栈开发工具，从自然语言提示生成、运行和部署完整的Web应用。"
        categories = @("coding")
        tags = @("Bolt","StackBlitz","full-stack","coding","AI")
        type_val = "tool"
        url = "https://bolt.new"
        developer = "StackBlitz"
        founded = "2024"
        pricing = "Free; Pro $20/mo"
        category = @("coding")
        logo = "https://logo.clearbit.com/stackblitz.com"
        intro = "**Bolt** by StackBlitz is an AI full-stack development tool that lets you prompt, run, edit, and deploy full-stack web applications entirely in your browser. It generates complete projects with frontend, backend, and database code."
        zh_intro = "**Bolt** 由StackBlitz开发，是一款AI全栈开发工具，让您完全在浏览器中通过提示、运行、编辑和部署全栈Web应用。它生成包含前端、后端和数据库代码的完整项目。"
        features = @(
            "**Full-Stack Generation** — Creates complete web apps with frontend + backend",
            **In-Browser Runtime** — Run Node.js projects directly in the browser",
            "**AI Code Editor** — Chat with AI to modify generated code",
            "**Instant Preview** — See changes in real-time as you iterate",
            "**NPM Ecosystem** — Access to thousands of npm packages",
            "**One-Click Deploy** — Deploy to production with a single click"
        )
        zh_features = @(
            "**全栈生成** — 创建包含前端+后端的完整Web应用",
            "**浏览器运行时** — 直接在浏览器中运行Node.js项目",
            "**AI代码编辑器** — 与AI对话修改生成的代码",
            "**即时预览** — 迭代时实时查看更改",
            "**NPM生态系统** — 访问数千个npm包",
            "**一键部署** — 一键部署到生产环境"
        )
        pricing_table = @(
            @("Free","$0","Limited generations, shared resources"),
            @("Pro","$20/mo","Unlimited generations, faster performance")
        )
        zh_pricing_table = @(
            @("免费版","$0","有限的生成次数，共享资源"),
            @("专业版","$20/月","无限生成，更快性能")
        )
        pros = @(
            "Go from idea to deployed app in minutes",
            "No local development environment needed",
            "Supports full-stack — not just frontend",
            "Great for rapid prototyping and MVPs"
        )
        zh_pros = @(
            "几分钟内从想法到部署应用",
            "不需要本地开发环境",
            "支持全栈——不仅仅是前端",
            "非常适合快速原型设计和MVP"
        )
        cons = @(
            "Generated code can be messy for complex projects",
            "Debugging AI-generated code can be frustrating",
            "Browser-based limits for very large projects"
        )
        zh_cons = @(
            "复杂项目的生成代码可能较乱",
            "调试AI生成的代码可能很令人沮丧",
            "浏览器方式对大型项目有局限"
        )
        best_for = "Developers prototyping ideas quickly, non-technical founders building MVPs, and anyone who wants to create web apps without complex setup."
        zh_best_for = "快速原型设计的开发者、构建MVP的非技术创始人，以及任何想无需复杂设置就创建Web应用的人。"
        compare_headers = @("Feature","Bolt","v0","Replit")
        compare_rows = @(
            @("Full-stack","✅","❌","✅"),
            @("In-browser","✅","✅","❌"),
            @("Instant deploy","✅","✅","✅"),
            @("AI chat editing","✅","✅","✅"),
            @("Price","$0-$20/mo","$0-$20/mo","$0-$25/mo")
        )
        verdict = "Rating: 4.3/5`n`nBolt is the fastest way to go from idea to working web app. It's perfect for prototyping, though complex projects still need manual refinement."
        zh_verdict = "评分：4.3/5`n`nBolt是从想法到可用Web应用最快的方式。非常适合原型设计，但复杂项目仍需手动调整。"
        zh_compare_headers = @("功能","Bolt","v0","Replit")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - devin
    @{
        slug = "devin"
        title = "Devin — First AI Software Engineer"
        desc = "Complete review of Devin by Cognition — the world's first autonomous AI software engineer that can plan, code, debug, and deploy on its own."
        zh_title = "Devin — 首个AI软件工程师"
        zh_desc = "Devin by Cognition完整评测——世界首个自主AI软件工程师，能独立规划、编码、调试和部署。"
        categories = @("coding")
        tags = @("Devin","Cognition","AI-engineer","coding")
        type_val = "tool"
        url = "https://devin.ai"
        developer = "Cognition Labs"
        founded = "2023"
        pricing = "Custom (contact sales)"
        category = @("coding")
        logo = "https://logo.clearbit.com/cognition.ai"
        intro = "**Devin** by Cognition Labs is the world's first autonomous AI software engineer. It can independently plan, write, debug, and deploy code — handling entire development tasks from start to finish."
        zh_intro = "**Devin** 由Cognition Labs开发，是世界首个自主AI软件工程师。它能独立规划、编写、调试和部署代码——从头到尾处理完整的开发任务。"
        features = @(
            "**Autonomous Coding** — Plans and executes coding tasks independently",
            "**Full Development Environment** — Has its own shell, browser, and editor",
            "**Bug Fixing** — Reads error logs, diagnoses issues, and implements fixes",
            **Multi-Step Reasoning** — Breaks complex tasks into sub-tasks",
            "**GitHub Integration** — Can create PRs, review code, and manage repos",
            "**Real-time Progress** — Watch Devin work step by step in real-time"
        )
        zh_features = @(
            "**自主编码** — 独立规划和执行编码任务",
            "**完整开发环境** — 拥有自己的shell、浏览器和编辑器",
            "**Bug修复** — 读取错误日志、诊断问题并实施修复",
            "**多步推理** — 将复杂任务分解为子任务",
            "**GitHub集成** — 可创建PR、审查代码和管理仓库",
            "**实时进度** — 实时观看Devin逐步工作"
        )
        pricing_table = @(
            @("Limited Access","Custom","Early access, limited capacity"),
            @("Enterprise","Custom","Full access, priority support")
        )
        zh_pricing_table = @(
            @("有限访问","联系定价","早期访问，有限容量"),
            @("企业版","联系定价","完整访问，优先支持")
        )
        pros = @(
            "Truly autonomous — handles entire tasks independently",
            "Can work on real codebases with real tools",
            "Fascinating to watch it work step by step",
            "Potential to dramatically increase developer productivity"
        )
        zh_pros = @(
            "真正的自主——独立处理整个任务",
            "能使用真实工具在真实代码库上工作",
            "观看它逐步工作令人着迷",
            "有可能大幅提高开发者生产力"
        )
        cons = @(
            "Very expensive — enterprise pricing only",
            "Can struggle with ambiguous or poorly scoped tasks",
            "Still early stage — reliability varies",
            "Not a replacement for senior engineers"
        )
        zh_cons = @(
            "价格昂贵——仅限企业定价",
            "在模糊或范围不清的任务上可能困难",
            "仍处于早期阶段——可靠性不稳定",
            "不能替代资深工程师"
        )
        best_for = "Enterprise engineering teams looking to automate routine development tasks and increase productivity."
        zh_best_for = "希望自动化常规开发任务并提高生产力的企业工程团队。"
        compare_headers = @("Feature","Devin","Cursor","GitHub Copilot")
        compare_rows = @(
            @("Autonomous","✅","❌","❌"),
            @("Full dev environment","✅","✅","✅"),
            @("Multi-task","✅","✅","Single task"),
            @("Price","Enterprise","$20/mo","$10-$39/mo"),
            @("Maturity","Early","Mature","Mature")
        )
        verdict = "Rating: 3.8/5`n`nDevin is groundbreaking as the first autonomous AI engineer, but it's still early and expensive. Worth watching closely."
        zh_verdict = "评分：3.8/5`n`nDevin作为首个自主AI工程师具有开创性意义，但仍处于早期且价格昂贵。值得密切关注。"
        zh_compare_headers = @("功能","Devin","Cursor","GitHub Copilot")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - augment-code
    @{
        slug = "augment-code"
        title = "Augment Code — Best AI Coding Assistant"
        desc = "Complete review of Augment Code — AI-powered coding assistant that understands your entire codebase for intelligent code suggestions and explanations."
        zh_title = "Augment Code — 最佳AI编程助手"
        zh_desc = "Augment Code完整评测——AI驱动的编程助手，理解您的整个代码库以提供智能代码建议和解释。"
        categories = @("coding")
        tags = @("Augment Code","coding","AI","assistant")
        type_val = "tool"
        url = "https://www.augmentcode.com"
        developer = "Augment Code"
        founded = "2023"
        pricing = "Free; Pro $25/mo"
        category = @("coding")
        logo = "https://logo.clearbit.com/augmentcode.com"
        intro = "**Augment Code** is an AI coding assistant that goes beyond simple autocomplete. It understands your entire codebase, team patterns, and coding standards to provide intelligent, context-aware suggestions."
        zh_intro = "**Augment Code** 是一款超越简单自动补全的AI编程助手。它理解您的整个代码库、团队模式和编码标准，提供智能的上下文感知建议。"
        features = @(
            "**Codebase Understanding** — Indexes your entire project for contextual suggestions",
            "**Intelligent Autocomplete** — Context-aware code completion",
            **Code Explanations** — Explains complex code in natural language",
            "**Bug Detection** — Identifies potential bugs and suggests fixes",
            "**Multi-file Editing** — Can make changes across multiple files at once",
            "**Team Learning** — Adapts to your team's coding patterns over time"
        )
        zh_features = @(
            "**代码库理解** — 索引整个项目以提供上下文建议",
            "**智能自动补全** — 上下文感知的代码补全",
            "**代码解释** — 用自然语言解释复杂代码",
            "**Bug检测** — 识别潜在bug并建议修复",
            "**多文件编辑** — 可以一次在多个文件中做更改",
            "**团队学习** — 随时间适应您团队的编码模式"
        )
        pricing_table = @(
            @("Free","$0","Basic autocomplete, limited queries"),
            @("Pro","$25/mo","Full codebase understanding, advanced features")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础自动补全，有限查询"),
            @("专业版","$25/月","完整代码库理解，高级功能")
        )
        pros = @(
            "Deep codebase understanding sets it apart",
            "Learns team coding patterns over time",
            "Multi-file editing is powerful",
            "Excellent for large, complex codebases"
        )
        zh_pros = @(
            "深度的代码库理解使其与众不同",
            "随时间学习团队编码模式",
            "多文件编辑功能强大",
            "非常适合大型复杂代码库"
        )
        cons = @(
            "Relatively new to the market",
            "Pro plan is pricier than some competitors",
            "IDE support still expanding"
        )
        zh_cons = @(
            "市场相对较新",
            "Pro版比一些竞品更贵",
            "IDE支持仍在扩展中"
        )
        best_for = "Developers working on large codebases who need AI that understands their entire project context."
        zh_best_for = "在大型代码库上工作、需要理解整个项目上下文的AI的开发者。"
        compare_headers = @("Feature","Augment Code","Cursor","GitHub Copilot")
        compare_rows = @(
            @("Codebase awareness","Full","Full","Partial"),
            @("Multi-file edits","✅","✅","❌"),
            @("IDE support","VS Code, JetBrains","VS Code only","Multiple IDEs"),
            @("Price","$0-$25/mo","$20/mo","$10-$39/mo"),
            @("Team learning","✅","❌","❌")
        )
        verdict = "Rating: 4.2/5`n`nAugment Code excels at understanding large codebases. It's a strong choice for teams working on complex projects."
        zh_verdict = "评分：4.2/5`n`nAugment Code在理解大型代码库方面表现出色。是在复杂项目上工作的团队的强有力选择。"
        zh_compare_headers = @("功能","Augment Code","Cursor","GitHub Copilot")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - coderabbit
    @{
        slug = "coderabbit"
        title = "CodeRabbit — Best AI Code Review"
        desc = "Complete review of CodeRabbit — AI code review tool that provides instant, detailed PR reviews with actionable feedback for development teams."
        zh_title = "CodeRabbit — 最佳AI代码审查工具"
        zh_desc = "CodeRabbit完整评测——AI代码审查工具，为开发团队提供即时详细的PR审查和可操作的反馈。"
        categories = @("coding")
        tags = @("CodeRabbit","code-review","AI","PR")
        type_val = "tool"
        url = "https://coderabbit.ai"
        developer = "CodeRabbit"
        founded = "2023"
        pricing = "Free; Pro $12/mo; Team $24/user/mo"
        category = @("coding")
        logo = "https://logo.clearbit.com/coderabbit.ai"
        intro = "**CodeRabbit** is an AI-powered code review tool that automatically reviews pull requests and provides detailed, actionable feedback. It integrates with GitHub, GitLab, and Bitbucket to catch issues before they reach production."
        zh_intro = "**CodeRabbit** 是一款AI驱动的代码审查工具，自动审查Pull Request并提供详细可操作的反馈。它与GitHub、GitLab和Bitbucket集成，在问题到达生产环境之前捕获它们。"
        features = @(
            "**Auto PR Reviews** — Reviews every PR with detailed line-by-line feedback",
            "**Security Scanning** — Detects security vulnerabilities and suggests fixes",
            "**Performance Insights** — Identifies performance bottlenecks",
            "**PR Summaries** — Auto-generates PR descriptions and changelogs",
            **Multi-language** — Supports 30+ programming languages",
            "**Chat** — Ask questions about code directly in PR comments"
        )
        zh_features = @(
            "**自动PR审查** — 对每个PR进行详细的逐行反馈审查",
            "**安全扫描** — 检测安全漏洞并建议修复",
            "**性能洞察** — 识别性能瓶颈",
            "**PR摘要** — 自动生成PR描述和变更日志",
            "**多语言** — 支持30多种编程语言",
            "**聊天** — 直接在PR评论中询问代码问题"
        )
        pricing_table = @(
            @("Free","$0","Open source, limited reviews"),
            @("Pro","$12/mo","Unlimited reviews, full features"),
            @("Team","$24/user/mo","Team analytics, admin controls")
        )
        zh_pricing_table = @(
            @("免费版","$0","开源项目，有限审查"),
            @("专业版","$12/月","无限审查，完整功能"),
            @("团队版","$24/用户/月","团队分析，管理控制")
        )
        pros = @(
            "Catches bugs and security issues human reviewers miss",
            "Extremely fast — reviews in seconds",
            "Detailed, actionable feedback",
            "Excellent GitHub/GitLab integration"
        )
        zh_pros = @(
            "捕获人工审查遗漏的bug和安全问题",
            "极快——几秒内完成审查",
            "详细可操作的反馈",
            "出色的GitHub/GitLab集成"
        )
        cons = @(
            "Can have false positives — needs human oversight",
            "Less useful for very domain-specific code",
            "Team plan pricing adds up"
        )
        zh_cons = @(
            "可能有误报——需要人工监督",
            "对特定领域的代码不太有用",
            "团队版定价较高"
        )
        best_for = "Development teams wanting faster, more thorough code reviews — especially those with limited senior reviewers."
        zh_best_for = "希望获得更快更彻底代码审查的开发团队——特别是资深审查人员有限的团队。"
        compare_headers = @("Feature","CodeRabbit","GitHub Copilot","Bito")
        compare_rows = @(
            @("Auto PR review","✅","❌","✅"),
            @("Security scanning","✅","✅","❌"),
            @("PR summaries","✅","❌","✅"),
            @("Line-by-line feedback","✅","✅","✅"),
            @("Price (Pro)","$12/mo","$10/mo","$10/mo")
        )
        verdict = "Rating: 4.4/5`n`nCodeRabbit is the best AI code review tool available. It catches real issues and saves senior developers significant review time."
        zh_verdict = "评分：4.4/5`n`nCodeRabbit是目前最好的AI代码审查工具。它能发现真实问题，为资深开发者节省大量审查时间。"
        zh_compare_headers = @("功能","CodeRabbit","GitHub Copilot","Bito")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Coding - sweep
    @{
        slug = "sweep"
        title = "Sweep — Best AI Code Assistant"
        desc = "Complete review of Sweep — AI junior developer that creates PRs for bug fixes, features, and refactors directly from GitHub issues."
        zh_title = "Sweep — 最佳AI代码助手"
        zh_desc = "Sweep完整评测——AI初级开发者，直接从GitHub Issues创建Bug修复、功能和重构的PR。"
        categories = @("coding")
        tags = @("Sweep","AI","coding","GitHub")
        type_val = "tool"
        url = "https://sweep.dev"
        developer = "Sweep AI"
        founded = "2023"
        pricing = "Free; Pro $20/mo"
        category = @("coding")
        logo = "https://logo.clearbit.com/sweep.dev"
        intro = "**Sweep** is an AI junior developer that turns GitHub issues into pull requests. Give it a task, and it plans, writes, tests, and creates a PR — essentially acting as an automated junior developer."
        zh_intro = "**Sweep** 是一款AI初级开发者，将GitHub Issues转换为Pull Requests。给它一个任务，它会规划、编写、测试并创建PR——本质上充当一个自动化的初级开发者。"
        features = @(
            "**Issue-to-PR** — Creates PRs directly from GitHub issues",
            "**Multi-file Changes** — Makes coherent changes across many files",
            "**Test Generation** — Writes unit tests for changes",
            **Plan & Execute** — Breaks tasks into steps, executes methodically",
            "**Context Awareness** — Reads relevant files and docs before coding",
            "**GitHub Integration** — Works natively with GitHub repos"
        )
        zh_features = @(
            "**Issue转PR** — 直接从GitHub Issues创建PR",
            "**多文件更改** — 在多个文件中做连贯的更改",
            "**测试生成** — 为更改编写单元测试",
            "**规划与执行** — 将任务分解为步骤，有条理地执行",
            "**上下文感知** — 编码前读取相关文件和文档",
            "**GitHub集成** — 原生支持GitHub仓库"
        )
        pricing_table = @(
            @("Free","$0","Open source, 1 repo"),
            @("Pro","$20/mo","Unlimited repos, priority processing")
        )
        zh_pricing_table = @(
            @("免费版","$0","开源项目，1个仓库"),
            @("专业版","$20/月","无限仓库，优先处理")
        )
        pros = @(
            "Automates routine coding tasks effectively",
            "Understands codebase context",
            "Great for boilerplate and simple features",
            "Saves time on repetitive tasks"
        )
        zh_pros = @(
            "有效自动化常规编码任务",
            "理解代码库上下文",
            "非常适合样板代码和简单功能",
            "在重复性任务上节省时间"
        )
        cons = @(
            "Quality varies — needs human review on generated PRs",
            "Struggles with complex architectural changes",
            "GitHub only — no GitLab or Bitbucket"
        )
        zh_cons = @(
            "质量不稳定——生成的PR需要人工审查",
            "在复杂的架构变更上表现不佳",
            "仅支持GitHub——不支持GitLab或Bitbucket"
        )
        best_for = "Developers who want to automate routine coding tasks and quickly turn GitHub issues into working pull requests."
        zh_best_for = "希望自动化常规编码任务并快速将GitHub Issues转化为可工作的Pull Requests的开发者。"
        compare_headers = @("Feature","Sweep","Devin","Cursor")
        compare_rows = @(
            @("Issue-to-PR","✅","❌","❌"),
            @("Autonomous","Semi","Fully","Assisted"),
            @("GitHub native","✅","✅","✅"),
            @("Price","$0-$20/mo","Enterprise","$20/mo"),
            @("Best for","Routine tasks","Complex projects","Interactive coding")
        )
        verdict = "Rating: 3.9/5`n`nSweep is handy for automating routine coding tasks. It's not as capable as Devin but much more accessible for individual developers."
        zh_verdict = "评分：3.9/5`n`nSweep对于自动化常规编码任务很实用。它不如Devin强大，但对个人开发者来说更容易获取。"
        zh_compare_headers = @("功能","Sweep","Devin","Cursor")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Image - designify
    @{
        slug = "designify"
        title = "Designify — Best AI Product Design"
        desc = "Complete review of Designify — AI product photo editor that creates professional product images, mockups, and lifestyle shots automatically."
        zh_title = "Designify — 最佳AI产品设计工具"
        zh_desc = "Designify完整评测——AI产品照片编辑器，自动创建专业产品图片、模型图和生活方式照片。"
        categories = @("image")
        tags = @("Designify","product-photo","AI","e-commerce")
        type_val = "tool"
        url = "https://www.designify.com"
        developer = "Designify"
        founded = "2021"
        pricing = "Free trial; Pro $29/mo; Pay-as-you-go"
        category = @("image")
        logo = "https://logo.clearbit.com/designify.com"
        intro = "**Designify** is an AI-powered product photo editor that transforms ordinary product photos into professional-grade images. It removes backgrounds, creates mockups, and generates lifestyle scenes automatically."
        zh_intro = "**Designify** 是一款AI驱动的产品照片编辑器，将普通产品照片转化为专业级图像。它自动去除背景、创建模型图和生成生活方式场景。"
        features = @(
            "**Background Removal** — AI-powered automatic background removal",
            "**Mockup Generation** — Places products in realistic scene mockups",
            **Shadow & Reflection** — Adds realistic shadows and reflections",
            "**Batch Processing** — Edit hundreds of images at once",
            **Color Correction** — AI-enhanced color and lighting adjustment",
            "**Template Library** — Thousands of pre-built mockup templates"
        )
        zh_features = @(
            "**背景去除** — AI自动背景去除",
            "**模型生成** — 将产品放置在真实的场景模型中",
            "**阴影和反射** — 添加逼真的阴影和反射",
            "**批量处理** — 一次编辑数百张图片",
            "**色彩校正** — AI增强的色彩和光照调整",
            "**模板库** — 数千个预建模型模板"
        )
        pricing_table = @(
            @("Free Trial","$0","3 free designs"),
            @("Pro","$29/mo","Unlimited designs, priority rendering"),
            @("Pay-as-you-go","$1.90/design","No subscription needed")
        )
        zh_pricing_table = @(
            @("免费试用","$0","3个免费设计"),
            @("专业版","$29/月","无限设计，优先渲染"),
            @("按需付费","$1.90/设计","无需订阅")
        )
        pros = @(
            "Stunning product photos in seconds",
            "Huge mockup template library",
            "Batch processing saves massive time",
            "Pay-as-you-go option is flexible"
        )
        zh_pros = @(
            "几秒内获得惊艳的产品照片",
            "巨大的模型模板库",
            "批量处理节省大量时间",
            "按需付费选项很灵活"
        )
        cons = @(
            "Pro plan is expensive for occasional users",
            "Some mockups look obviously AI-generated",
            "Limited customization for advanced users"
        )
        zh_cons = @(
            "Pro版对偶尔使用的用户来说较贵",
            "一些模型看起来明显是AI生成的",
            "对高级用户的自定义功能有限"
        )
        best_for = "E-commerce sellers, marketers, and small businesses that need professional product photos without expensive photo shoots."
        zh_best_for = "需要专业产品照片但不想花钱拍摄照的电商卖家、营销人员和小企业。"
        compare_headers = @("Feature","Designify","Photoroom","Canva")
        compare_rows = @(
            @("Product mockups","✅","✅","Partial"),
            @("Batch processing","✅","✅","❌"),
            @("Background removal","✅","✅","✅"),
            @("Lifestyle scenes","✅","✅","❌"),
            @("Price","$1.90+/design","$13/mo","$13/mo")
        )
        verdict = "Rating: 4.1/5`n`nDesignify is the best tool for creating professional product mockups. Pay-as-you-go pricing makes it great for occasional use."
        zh_verdict = "评分：4.1/5`n`nDesignify是创建专业产品模型的最佳工具。按需付费使其非常适合偶尔使用。"
        zh_compare_headers = @("功能","Designify","Photoroom","Canva")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Image - uizard
    @{
        slug = "uizard"
        title = "Uizard — Best AI UI Design"
        desc = "Complete review of Uizard — AI UI design tool that transforms hand-drawn sketches, screenshots, and text prompts into professional UI designs and prototypes."
        zh_title = "Uizard — 最佳AI UI设计工具"
        zh_desc = "Uizard完整评测——AI UI设计工具，将手绘草图、截图和文本提示转换为专业的UI设计和原型。"
        categories = @("image")
        tags = @("Uizard","UI-design","prototype","AI")
        type_val = "tool"
        url = "https://uizard.io"
        developer = "Uizard"
        founded = "2018"
        pricing = "Free; Pro $19/mo; Business $39/mo"
        category = @("image")
        logo = "https://logo.clearbit.com/uizard.io"
        intro = "**Uizard** is an AI-powered UI design tool that lets you create professional app and website designs from hand-drawn sketches, screenshots, or text prompts. No design skills required."
        zh_intro = "**Uizard** 是一款AI驱动的UI设计工具，让您从手绘草图、截图或文本提示创建专业的应用和网站设计。无需设计技能。"
        features = @(
            "**Sketch-to-UI** — Convert hand-drawn wireframes into digital designs",
            "**Screenshot-to-Design** — Transform screenshots into editable UI designs",
            "**AI Theme Generation** — Generate complete design themes from text",
            **Prototyping** — Add interactivity and create clickable prototypes",
            "**Component Library** — Thousands of pre-built UI components",
            "**Collaboration** — Real-time team collaboration and commenting"
        )
        zh_features = @(
            "**草图转UI** — 将手绘线框转换为数字设计",
            "**截图转设计** — 将截图转换为可编辑的UI设计",
            "**AI主题生成** — 从文本生成完整的设计主题",
            "**原型设计** — 添加交互性并创建可点击的原型",
            "**组件库** — 数千个预建UI组件",
            "**协作** — 实时团队协作和评论"
        )
        pricing_table = @(
            @("Free","$0","3 projects, basic features"),
            @("Pro","$19/mo","Unlimited projects, full library"),
            @("Business","$39/mo","Team features, custom branding")
        )
        zh_pricing_table = @(
            @("免费版","$0","3个项目，基础功能"),
            @("专业版","$19/月","无限项目，完整组件库"),
            @("企业版","$39/月","团队功能，自定义品牌")
        )
        pros = @(
            "No design skills needed",
            "Sketch-to-UI feature is incredibly useful",
            "Rapid prototyping saves weeks of work",
            "Affordable compared to Figma/Sketch"
        )
        zh_pros = @(
            "无需设计技能",
            "草图转UI功能非常有用",
            "快速原型设计节省数周工作",
            "相比Figma/Sketch更实惠"
        )
        cons = @(
            "Designs can look generic without customization",
            "Not as powerful as Figma for complex designs",
            "Free tier is very limited"
        )
        zh_cons = @(
            "未经自定义的设计可能看起来很普通",
            "复杂设计不如Figma强大",
            "免费版非常有限"
        )
        best_for = "Founders, product managers, and non-designers who need to create professional UI mockups and prototypes quickly."
        zh_best_for = "需要快速创建专业UI模型和原型的创始人、产品经理和非设计人员。"
        compare_headers = @("Feature","Uizard","v0","Figma")
        compare_rows = @(
            @("Sketch-to-UI","✅","❌","❌"),
            @("Screenshot-to-code","✅","✅","❌"),
            @("Prototyping","✅","❌","✅"),
            @("No code required","✅","✅","❌"),
            @("Price","$0-$39/mo","$0-$20/mo","Free-$15/mo")
        )
        verdict = "Rating: 4.2/5`n`nUizard democratizes UI design. It's the best choice for non-designers who need professional-looking interfaces quickly."
        zh_verdict = "评分：4.2/5`n`nUizard让UI设计民主化。它是需要快速获得专业界面外观的非设计人员的最佳选择。"
        zh_compare_headers = @("功能","Uizard","v0","Figma")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Image - looka
    @{
        slug = "looka"
        title = "Looka — Best AI Logo & Brand Design"
        desc = "Complete review of Looka — AI logo and brand identity generator that creates professional logos, brand kits, and business cards in minutes."
        zh_title = "Looka — 最佳AI标志与品牌设计"
        zh_desc = "Looka完整评测——AI标志和品牌标识生成器，几分钟内创建专业标志、品牌套件和名片。"
        categories = @("image")
        tags = @("Looka","logo","brand","AI")
        type_val = "tool"
        url = "https://looka.com"
        developer = "Looka"
        founded = "2016"
        pricing = "One-time $20+ for logo; Brand Kit $96"
        category = @("image")
        logo = "https://logo.clearbit.com/looka.com"
        intro = "**Looka** is an AI-powered logo and brand identity designer. It uses machine learning to generate professional logos, complete brand kits, and marketing materials in minutes."
        zh_intro = "**Looka** 是一款AI驱动的标志和品牌标识设计工具。它使用机器学习在几分钟内生成专业标志、完整品牌套件和营销材料。"
        features = @(
            "**AI Logo Generation** — Generates dozens of logo options from your preferences",
            **Brand Kit** — Complete brand package with colors, fonts, and guidelines",
            "**Business Cards** — Design matching business cards automatically",
            "**Social Media Kits** — Profile images and cover photos",
            "** hundreds of Templates** — Flyers, posters, email signatures",
            "**Customization** — Fine-tune colors, fonts, layout after generation"
        )
        zh_features = @(
            "**AI标志生成** — 根据您的偏好生成数十个标志选项",
            "**品牌套件** — 包含颜色、字体和指南的完整品牌包",
            "**名片** — 自动设计匹配的名片",
            "**社交媒体套件** — 头像和封面照片",
            "**数百个模板** — 传单、海报、电子邮件签名",
            "**自定义** — 生成后精细调整颜色、字体、布局"
        )
        pricing_table = @(
            @("Logo Only","$20 one-time","1 logo file, basic formats"),
            @("Logo + Brand Kit","$96 one-time","Full brand package"),
            @("Enterprise","Custom","Multiple concepts, full rights")
        )
        zh_pricing_table = @(
            @("仅标志","$20一次性","1个标志文件，基础格式"),
            @("标志+品牌套件","$96一次性","完整品牌包"),
            @("企业版","定制","多个方案，完整版权")
        )
        pros = @(
            "Professional results in minutes",
            "No design skills needed",
            "One-time payment — no subscription",
            "Complete brand kit in one purchase"
        )
        zh_pros = @(
            "几分钟内获得专业结果",
            "无需设计技能",
            "一次性付费——无需订阅",
            "一次购买获得完整品牌套件"
        )
        cons = @(
            "Logos can look similar to others in the same industry",
            "Limited to logo and branding — not a full design tool",
            "No vector source files on basic plan"
        )
        zh_cons = @(
            "标志可能与同行业的其他标志相似",
            "仅限于标志和品牌——不是完整的设计工具",
            "基础计划不提供矢量源文件"
        )
        best_for = "Startups, small businesses, and entrepreneurs who need professional branding quickly and affordably."
        zh_best_for = "需要快速且实惠获得专业品牌的初创公司、小企业和企业家。"
        compare_headers = @("Feature","Looka","Canva","Hatchful")
        compare_rows = @(
            @("AI generation","✅","❌","✅"),
            @("Brand kit","✅","❌","❌"),
            @("Customization","✅","✅","Limited"),
            @("Price","$20+","$13/mo","Free"),
            @("Quality","High","High","Low")
        )
        verdict = "Rating: 4.1/5`n`nLooka is the fastest way to get a professional logo and brand kit. One-time pricing makes it great for startups."
        zh_verdict = "评分：4.1/5`n`nLooka是获得专业标志和品牌套件最快的方式。一次性定价对初创公司来说很棒。"
        zh_compare_headers = @("功能","Looka","Canva","Hatchful")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Image - khroma
    @{
        slug = "khroma"
        title = "Khroma — Best AI Color Palette Generator"
        desc = "Complete review of Khroma — AI color palette generator that learns your preferences to create beautiful, personalized color combinations for design projects."
        zh_title = "Khroma — 最佳AI配色工具"
        zh_desc = "Khroma完整评测——AI配色方案生成器，学习您的偏好以创建适合设计项目的美丽个性化色彩组合。"
        categories = @("image")
        tags = @("Khroma","color","palette","design")
        type_val = "tool"
        url = "https://www.khroma.co"
        developer = "George Hastings"
        founded = "2018"
        pricing = "Free"
        category = @("image")
        logo = "https://logo.clearbit.com/khroma.co"
        intro = "**Khroma** is an AI color palette generator that uses machine learning to understand your color preferences and generate personalized palettes, gradients, and typography combinations you'll actually love."
        zh_intro = "**Khroma** 是一款AI配色方案生成器，使用机器学习理解您的颜色偏好，生成您真正喜欢的个性化调色板、渐变和字体组合。"
        features = @(
            "**Personalized Palettes** — Trains on your preferences to suggest colors you'll like",
            "**Infinite Combinations** — Generate endless color combinations",
            "**Multiple Formats** — View colors as palettes, gradients, and typography",
            "**Accessibility Check** — Shows contrast ratios for accessibility",
            "**Color Codes** — Copy HEX, RGB, HSL, and CSS values instantly",
            "**Favorites** — Save and organize your favorite combinations"
        )
        zh_features = @(
            "**个性化调色板** — 基于您的偏好训练，推荐您会喜欢的颜色",
            "**无限组合** — 生成无尽的色彩组合",
            "**多种格式** — 以调色板、渐变和排版方式查看颜色",
            "**无障碍检查** — 显示无障碍对比度比率",
            "**颜色代码** — 即时复制HEX、RGB、HSL和CSS值",
            "**收藏夹** — 保存和组织您最爱的组合"
        )
        pricing_table = @(
            @("Free","$0","Unlimited palette generation")
        )
        zh_pricing_table = @(
            @("免费","$0","无限调色板生成")
        )
        pros = @(
            "Genuinely learns your taste over time",
            "Completely free to use",
            "Beautiful, well-curated combinations",
            "Accessibility-aware"
        )
        zh_pros = @(
            "真正随时间学习您的品味",
            "完全免费使用",
            "美丽精选的组合",
            "关注无障碍性"
        )
        cons = @(
            "Requires initial training (select 50 colors)",
            "Web-only — no mobile app",
            "Limited to color — no full design features"
        )
        zh_cons = @(
            "需要初始训练（选择50种颜色）",
            "仅限网页——没有移动应用",
            "仅限于颜色——没有完整设计功能"
        )
        best_for = "Designers, developers, and anyone who struggles with choosing the right colors for their projects."
        zh_best_for = "在项目配色上遇到困难的设计师、开发者和任何人。"
        compare_headers = @("Feature","Khroma","Coolors","Adobe Color")
        compare_rows = @(
            @("AI personalization","✅","❌","❌"),
            @("Accessibility check","✅","✅","✅"),
            @("Price","Free","Free","Free"),
            @("Gradient support","✅","✅","✅"),
            @("Typography combos","✅","❌","❌")
        )
        verdict = "Rating: 4.5/5`n`nKhroma is the best AI color tool because it actually learns what you like. Free and endlessly useful for any design project."
        zh_verdict = "评分：4.5/5`n`nKhroma是最佳AI配色工具，因为它真正学习您喜欢什么。免费且对任何设计项目都无限有用。"
        zh_compare_headers = @("功能","Khroma","Coolors","Adobe Color")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Video - pixverse
    @{
        slug = "pixverse"
        title = "PixVerse — Best AI Video Generator"
        desc = "Complete review of PixVerse — AI video generation platform that creates high-quality videos from text prompts and images with multiple artistic styles."
        zh_title = "PixVerse — 最佳AI视频生成器"
        zh_desc = "PixVerse完整评测——AI视频生成平台，从文本提示和图像创建高质量视频，支持多种艺术风格。"
        categories = @("video")
        tags = @("PixVerse","video-generation","AI","creative")
        type_val = "tool"
        url = "https://pixverse.ai"
        developer = "PixVerse AI"
        founded = "2023"
        pricing = "Free; Pro $9.99/mo"
        category = @("video")
        logo = "https://logo.clearbit.com/pixverse.ai"
        intro = "**PixVerse** is an AI video generation platform that creates high-quality videos from text prompts and images. It offers multiple artistic styles and produces impressively smooth, cinematic results."
        zh_intro = "**PixVerse** 是一款AI视频生成平台，从文本提示和图像创建高质量视频。它提供多种艺术风格，产生令人印象深刻的流畅电影级效果。"
        features = @(
            "**Text-to-Video** — Generate videos from detailed text descriptions",
            "**Image-to-Video** — Animate still images into video",
            "**Multiple Styles** — Cinematic, anime, 3D, realistic, and more",
            "**HD Output** — Generate videos up to 1080p resolution",
            "**Character Consistency** — Maintain character appearance across scenes",
            "**Fast Generation** — Create videos in seconds"
        )
        zh_features = @(
            "**文本转视频** — 从详细文本描述生成视频",
            "**图像转视频** — 将静态图像动画化为视频",
            "**多种风格** — 电影、动漫、3D、写实等",
            "**高清输出** — 生成最高1080p分辨率的视频",
            "**角色一致性** — 在场景中保持角色外观一致",
            "**快速生成** — 几秒内创建视频"
        )
        pricing_table = @(
            @("Free","$0","~10 videos/day, standard quality"),
            @("Pro","$9.99/mo","Unlimited, HD quality, priority")
        )
        zh_pricing_table = @(
            @("免费版","$0","每天约10个视频，标准质量"),
            @("专业版","$9.99/月","无限生成，高清质量，优先处理")
        )
        pros = @(
            "Impressive video quality for the price",
            "Multiple artistic styles available",
            "Fast generation speed",
            "Very affordable Pro plan"
        )
        zh_pros = @(
            "视频质量令人印象深刻",
            "多种艺术风格可选",
            "生成速度快",
            "Pro版价格非常实惠"
        )
        cons = @(
            "Video length limited (typically 4-8 seconds)",
            "Character consistency can be inconsistent",
            "Less control than Runway or Pika"
        )
        zh_cons = @(
            "视频长度有限（通常4-8秒）",
            "角色一致性可能不稳定",
            "控制能力不如Runway或Pika"
        )
        best_for = "Content creators, marketers, and social media managers who need quick, eye-catching video content."
        zh_best_for = "需要快速、引人注目的视频内容的内容创作者、营销人员和社交媒体经理。"
        compare_headers = @("Feature","PixVerse","Runway","Pika")
        compare_rows = @(
            @("Text-to-video","✅","✅","✅"),
            @("Image-to-video","✅","✅","✅"),
            @("Price (Pro)","$9.99/mo","$15/mo","$8/mo"),
            @("Max resolution","1080p","4K","1080p"),
            @("Video length","4-8s","4-16s","4s")
        )
        verdict = "Rating: 4.0/5`n`nPixVerse offers great value for AI video generation. At $9.99/mo, it's one of the most affordable quality options available."
        zh_verdict = "评分：4.0/5`n`nPixVerse在AI视频生成方面性价比出色。每月$9.99是最实惠的质量选择之一。"
        zh_compare_headers = @("功能","PixVerse","Runway","Pika")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Video - captions
    @{
        slug = "captions"
        title = "Captions — Best AI Video Editor & Subtitles"
        desc = "Complete review of Captions — AI-powered video editor with automatic captions, eye contact correction, and AI-powered editing tools for content creators."
        zh_title = "Captions — 最佳AI视频编辑与字幕工具"
        zh_desc = "Captions完整评测——AI驱动的视频编辑器，具备自动字幕、眼神接触修正和AI编辑工具，专为内容创作者设计。"
        categories = @("video")
        tags = @("Captions","video-editor","subtitles","AI")
        type_val = "tool"
        url = "https://captions.ai"
        developer = "Captions AI"
        founded = "2021"
        pricing = "Free; Pro $9.99/mo; Business $24.99/mo"
        category = @("video")
        logo = "https://logo.clearbit.com/captions.ai"
        intro = "**Captions** is an AI-powered video editor designed for content creators. It features automatic caption generation, AI eye contact correction, teleprompter, and a suite of creative tools for social media content."
        zh_intro = "**Captions** 是一款专为内容创作者设计的AI视频编辑器。它具有自动字幕生成、AI眼神接触修正、提词器和一系列社交媒体内容创作工具。"
        features = @(
            "**Auto Captions** — Generate accurate captions in 50+ languages",
            "**Eye Contact AI** — Corrects eye contact to simulate looking at camera",
            "**AI Teleprompter** — Smart teleprompter that adjusts to your pace",
            "**AI Editor** — Automatically cuts silences and filler words",
            "**Background Effects** — Blur, replace, or enhance video backgrounds",
            "**Social Media Formats** — Export optimized for TikTok, Reels, Shorts"
        )
        zh_features = @(
            "**自动字幕** — 生成50多种语言的准确字幕",
            "**AI眼神接触** — 修正眼神接触以模拟看向镜头",
            "**AI提词器** — 智能提词器，根据您的节奏调整",
            "**AI编辑器** — 自动剪辑静音和填充词",
            "**背景效果** — 模糊、替换或增强视频背景",
            "**社交媒体格式** — 为TikTok、Reels、Shorts优化导出"
        )
        pricing_table = @(
            @("Free","$0","Basic captions, watermark"),
            @("Pro","$9.99/mo","No watermark, AI features"),
            @("Business","$24.99/mo","Team features, API access")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础字幕，有水印"),
            @("专业版","$9.99/月","无水印，AI功能"),
            @("商业版","$24.99/月","团队功能，API访问")
        )
        pros = @(
            "Eye contact AI is genuinely impressive",
            "Extremely easy to use",
            "Captions are highly accurate",
            "Perfect for social media creators"
        )
        zh_pros = @(
            "AI眼神接触功能确实令人印象深刻",
            "极其易于使用",
            "字幕非常准确",
            "非常适合社交媒体创作者"
        )
        cons = @(
            "Mobile-first — desktop features are limited",
            "Free version includes watermark",
            "Advanced editing less powerful than Premiere Pro"
        )
        zh_cons = @(
            "移动端优先——桌面功能有限",
            "免费版包含水印",
            "高级编辑不如Premiere Pro强大"
        )
        best_for = "Social media creators, YouTubers, TikTokers, and podcasters who need quick, professional-looking video content."
        zh_best_for = "需要快速制作专业外观视频内容的社交媒体创作者、YouTuber、TikToker和播客主持人。"
        compare_headers = @("Feature","Captions","Descript","CapCut")
        compare_rows = @(
            @("Auto captions","✅","✅","✅"),
            @("Eye contact AI","✅","❌","❌"),
            @("Teleprompter","✅","✅","❌"),
            @("Price (Pro)","$9.99/mo","$24/mo","Free-$8/mo"),
            @("Best for","Social media","Podcasts","Quick edits")
        )
        verdict = "Rating: 4.4/5`n`nCaptions is the best tool for social media video creation. The eye contact AI and auto captions make it a must-have for creators."
        zh_verdict = "评分：4.4/5`n`nCaptions是社交媒体视频创作的最佳工具。AI眼神接触和自动字幕使其成为创作者的必备工具。"
        zh_compare_headers = @("功能","Captions","Descript","CapCut")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Video - opus-clip
    @{
        slug = "opus-clip"
        title = "Opus Clip — Best AI Clip Maker"
        desc = "Complete review of Opus Clip — AI tool that converts long videos into viral short clips with AI scoring, captions, and social media optimization."
        zh_title = "Opus Clip — 最佳AI短视频剪辑工具"
        zh_desc = "Opus Clip完整评测——AI工具，将长视频转换为病毒式短视频，具备AI评分、字幕和社交媒体优化功能。"
        categories = @("video")
        tags = @("Opus Clip","short-form","viral","social")
        type_val = "tool"
        url = "https://www.opus.pro"
        developer = "Opus Clip"
        founded = "2023"
        pricing = "Free (1 video); Starter $9.99/mo; Pro $19.99/mo"
        category = @("video")
        logo = "https://logo.clearbit.com/opus.pro"
        intro = "**Opus Clip** uses AI to automatically find the most engaging moments in long videos and turn them into viral short clips optimized for TikTok, Reels, and Shorts."
        zh_intro = "**Opus Clip** 使用AI自动找到长视频中最有吸引力的时刻，并将其转换为针对TikTok、Reels和Shorts优化的病毒式短视频片段。"
        features = @(
            "**AI Virality Score** — Scores clips on their viral potential",
            "**Auto Clip Selection** — AI identifies the most engaging moments",
            "**Auto Captions** — Generates accurate captions with emojis",
            "**Aspect Ratio** — Auto-crops to 9:16 for vertical platforms",
            "**B-Roll** — Adds relevant B-roll footage to enhance clips",
            "**Speaker Detection** — Identifies and tracks speakers"
        )
        zh_features = @(
            "**AI病毒性评分** — 对片段的病毒传播潜力进行评分",
            "**自动片段选择** — AI识别最引人入胜的时刻",
            "**自动字幕** — 生成带有表情符号的准确字幕",
            "**宽高比** — 自动裁剪为9:16竖屏格式",
            "**B-Roll** — 添加相关B-Roll素材增强片段",
            "**发言人检测** — 识别和追踪发言人"
        )
        pricing_table = @(
            @("Free","$0","1 video, basic clips"),
            @("Starter","$9.99/mo","200 minutes/mo processing"),
            @("Pro","$19.99/mo","Unlimited processing, B-Roll")
        )
        zh_pricing_table = @(
            @("免费版","$0","1个视频，基础片段"),
            @("入门版","$9.99/月","每月200分钟处理"),
            @("专业版","$19.99/月","无限处理，B-Roll")
        )
        pros = @(
            "Saves hours of manual clipping",
            "Virality score helps prioritize content",
            "Captions and emojis look professional",
            "Great for repurposing podcast and interview content"
        )
        zh_pros = @(
            "节省数小时的手动剪辑时间",
            "病毒性评分帮助确定内容优先级",
            "字幕和表情符号看起来很专业",
            "非常适合重新利用播客和访谈内容"
        )
        cons = @(
            "Free tier is extremely limited (1 video only)",
            "AI sometimes picks less interesting moments",
            "Clip quality varies with source video quality"
        )
        zh_cons = @(
            "免费版极其有限（仅1个视频）",
            "AI有时会挑选不太有趣的时刻",
            "片段质量随源视频质量变化"
        )
        best_for = "Podcasters, live streamers, educators, and content creators who want to repurpose long-form content into viral short clips."
        zh_best_for = "希望将长视频重新制作为病毒式短视频的播客主持人、直播主、教育工作者和内容创作者。"
        compare_headers = @("Feature","Opus Clip","Captions","Veed")
        compare_rows = @(
            @("Auto clipping","✅","❌","❌"),
            @("Virality score","✅","❌","❌"),
            @("Auto captions","✅","✅","✅"),
            @("B-Roll","✅","❌","❌"),
            @("Price (Pro)","$19.99/mo","$9.99/mo","$18/mo")
        )
        verdict = "Rating: 4.3/5`n`nOpus Clip is the best tool for repurposing long videos into shorts. The virality scoring feature is unique and valuable."
        zh_verdict = "评分：4.3/5`n`nOpus Clip是将长视频重新制作为短视频的最佳工具。病毒性评分功能独特且有价值。"
        zh_compare_headers = @("功能","Opus Clip","Captions","Veed")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Audio - splash-pro
    @{
        slug = "splash-pro"
        title = "Splash Pro — Best AI Music Creation"
        desc = "Complete review of Splash Pro — AI music generation platform that creates original songs, beats, and full compositions from text prompts."
        zh_title = "Splash Pro — 最佳AI音乐创作工具"
        zh_desc = "Splash Pro完整评测——AI音乐生成平台，从文本提示创建原创歌曲、节拍和完整作品。"
        categories = @("audio")
        tags = @("Splash Pro","music","AI","creation")
        type_val = "tool"
        url = "https://splashmusic.com"
        developer = "Splash Music"
        founded = "2017"
        pricing = "Free; Pro $10/mo"
        category = @("audio")
        logo = "https://logo.clearbit.com/splashmusic.com"
        intro = "**Splash Pro** is an AI music generation platform that creates original songs and beats from text descriptions. It uses advanced AI models to produce high-quality music across multiple genres."
        zh_intro = "**Splash Pro** 是一款AI音乐生成平台，从文本描述创建原创歌曲和节拍。它使用先进的AI模型跨多种流派制作高质量音乐。"
        features = @(
            "**Text-to-Music** — Describe a song and AI generates it",
            "**Genre Selection** — Create music in any genre (pop, rock, electronic, etc.)",
            "**Vocal Synthesis** — Generate AI vocals with customizable style",
            "**Beat Making** — Create custom beats and loops",
            **Full Songs** — Generate complete songs with intro, verse, chorus",
            "**Download & Share** — Export as MP3/WAV for commercial use"
        )
        zh_features = @(
            "**文本转音乐** — 描述一首歌曲，AI为您生成",
            "**流派选择** — 创建任何流派的音乐（流行、摇滚、电子等）",
            "**人声合成** — 生成可定制风格的AI人声",
            "**节拍制作** — 创建自定义节拍和循环",
            "**完整歌曲** — 生成包含前奏、主歌、副歌的完整歌曲",
            "**下载和分享** — 导出为MP3/WAV用于商业用途"
        )
        pricing_table = @(
            @("Free","$0","10 generations/mo, non-commercial"),
            @("Pro","$10/mo","Unlimited, commercial rights")
        )
        zh_pricing_table = @(
            @("免费版","$0","每月10次生成，非商业用途"),
            @("专业版","$10/月","无限生成，商业权利")
        )
        pros = @(
            "High-quality AI music generation",
            "Supports vocals — not just instrumentals",
            "Affordable Pro plan",
            "Commercial usage rights included"
        )
        zh_pros = @(
            "高质量的AI音乐生成",
            "支持人声——不仅仅是器乐",
            "实惠的Pro计划",
            "包含商业使用权"
        )
        cons = @(
            "AI vocals can sound robotic at times",
            "Less genre variety than Suno/Udio",
            "Free tier is non-commercial only"
        )
        zh_cons = @(
            "AI人声有时听起来很机械",
            "流派多样性不如Suno/Udio",
            "免费版仅限非商业用途"
        )
        best_for = "Content creators needing original music for videos, podcasts, and social media without copyright concerns."
        zh_best_for = "需要为视频、播客和社交媒体获取原创音乐而无需担心版权问题的内容创作者。"
        compare_headers = @("Feature","Splash Pro","Suno","Udio")
        compare_rows = @(
            @("AI vocals","✅","✅","✅"),
            @("Commercial rights","✅ (Pro)","✅ (Pro)","✅ (Pro)"),
            @("Price (Pro)","$10/mo","$10/mo","$10/mo"),
            @("Genre variety","Good","Excellent","Excellent"),
            @("Music quality","Good","Excellent","Excellent")
        )
        verdict = "Rating: 3.8/5`n`nSplash Pro is a solid AI music tool but faces tough competition from Suno and Udio. Good for quick, simple music needs."
        zh_verdict = "评分：3.8/5`n`nSplash Pro是一个可靠的AI音乐工具，但面临Suno和Udio的激烈竞争。适合快速简单的音乐需求。"
        zh_compare_headers = @("功能","Splash Pro","Suno","Udio")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Audio - voicemaker
    @{
        slug = "voicemaker"
        title = "Voicemaker — Best AI Voice Generator"
        desc = "Complete review of Voicemaker — AI text-to-speech and voice cloning platform with 1000+ voices in 130+ languages for professional voiceovers."
        zh_title = "Voicemaker — 最佳AI语音生成器"
        zh_desc = "Voicemaker完整评测——AI文本转语音和声音克隆平台，提供130多种语言的1000多种声音，用于专业配音。"
        categories = @("audio")
        tags = @("Voicemaker","TTS","voice","AI")
        type_val = "tool"
        url = "https://voicemaker.in"
        developer = "Voicemaker"
        founded = "2020"
        pricing = "Free; Basic $9.99/mo; Premium $19.99/mo"
        category = @("audio")
        logo = "https://logo.clearbit.com/voicemaker.in"
        intro = "**Voicemaker** is an AI text-to-speech platform with over 1,000 voices across 130+ languages. It offers natural-sounding voice generation for videos, audiobooks, and commercial use."
        zh_intro = "**Voicemaker** 是一款AI文本转语音平台，拥有130多种语言的1,000多种声音。它提供自然流畅的语音生成，用于视频、有声读物和商业用途。"
        features = @(
            "**1000+ AI Voices** — Wide variety of male, female, and child voices",
            "**130+ Languages** — Support for most world languages",
            **Voice Customization** — Adjust speed, pitch, volume, and pauses",
            "**SSML Support** — Fine-grained control over pronunciation",
            **Commercial License** — Use generated audio commercially",
            "**API Access** — Integrate TTS into your applications"
        )
        zh_features = @(
            "**1000+种AI声音** — 丰富的男声、女声和童声",
            "**130+种语言** — 支持大多数世界语言",
            "**声音自定义** — 调整语速、音调、音量和停顿",
            "**SSML支持** — 对发音进行精细控制",
            "**商业许可** — 可将生成的音频用于商业用途",
            "**API访问** — 将TTS集成到您的应用程序中"
        )
        pricing_table = @(
            @("Free","$0","Limited characters, basic voices"),
            @("Basic","$9.99/mo","25,000 chars/mo, premium voices"),
            @("Premium","$19.99/mo","100,000 chars/mo, all features")
        )
        zh_pricing_table = @(
            @("免费版","$0","有限字符数，基础声音"),
            @("基础版","$9.99/月","每月25,000字符，高级声音"),
            @("高级版","$19.99/月","每月100,000字符，全部功能")
        )
        pros = @(
            "Massive voice library across many languages",
            "Natural-sounding output",
            "Commercial use allowed",
            "Affordable pricing tiers"
        )
        zh_pros = @(
            "跨多种语言的庞大声音库",
            "自然的语音输出",
            "允许商业使用",
            "实惠的价格档次"
        )
        cons = @(
            "Some voices sound less natural than ElevenLabs",
            "Character limits on paid plans can be restrictive",
            "No real-time voice cloning"
        )
        zh_cons = @(
            "一些声音不如ElevenLabs自然",
            "付费计划的字符限制可能较严格",
            "没有实时声音克隆"
        )
        best_for = "Content creators, educators, and businesses needing multilingual voiceovers at an affordable price."
        zh_best_for = "需要以实惠价格获得多语言配音的内容创作者、教育工作者和企业。"
        compare_headers = @("Feature","Voicemaker","ElevenLabs","PlayHT")
        compare_rows = @(
            @("Voice count","1000+","50+","800+"),
            @("Languages","130+","29","130+"),
            @("Voice cloning","❌","✅","✅"),
            @("Price (Basic)","$9.99/mo","$5/mo","$31/mo"),
            @("Naturalness","Good","Excellent","Good")
        )
        verdict = "Rating: 3.9/5`n`nVoicemaker offers the widest variety of voices but ElevenLabs sounds more natural. Best when you need specific languages."
        zh_verdict = "评分：3.9/5`n`nVoicemaker提供最广泛的声音种类，但ElevenLabs听起来更自然。在需要特定语言时最佳。"
        zh_compare_headers = @("功能","Voicemaker","ElevenLabs","PlayHT")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Audio - elevenreader
    @{
        slug = "elevenreader"
        title = "ElevenReader — Best AI Audiobook Reader"
        desc = "Complete review of ElevenReader — AI-powered text-to-speech reader app that turns any text, article, or document into natural-sounding audio."
        zh_title = "ElevenReader — 最佳AI有声读物阅读器"
        zh_desc = "ElevenReader完整评测——AI驱动的文本转语音阅读应用，将任何文本、文章或文档转换为自然流畅的音频。"
        categories = @("audio")
        tags = @("ElevenReader","audiobook","TTS","reading")
        type_val = "tool"
        url = "https://elevenlabs.io/elevenreader"
        developer = "ElevenLabs"
        founded = "2024"
        pricing = "Free; $5/mo (Starter)"
        category = @("audio")
        logo = "https://logo.clearbit.com/elevenlabs.io"
        intro = "**ElevenReader** by ElevenLabs is an AI-powered reading app that converts any text into natural-sounding audio. It can read articles, PDFs, emails, and documents with the same high-quality voice technology that made ElevenLabs famous."
        zh_intro = "**ElevenReader** 由ElevenLabs开发，是一款AI驱动的阅读应用，将任何文本转换为自然流畅的音频。它可以阅读文章、PDF、电子邮件和文档，使用与ElevenLabs闻名于世的相同高质量语音技术。"
        features = @(
            "**Article Reading** — Paste any URL and listen to articles as audio",
            "**PDF Support** — Upload and listen to PDF documents",
            **Multiple Voices** — Choose from ElevenLabs' premium voice library",
            "**Speed Control** — Adjust playback speed from 0.5x to 3x",
            "**Mobile App** — Listen on the go with iOS and Android apps",
            **Clipboard Reading** — Read copied text with one tap"
        )
        zh_features = @(
            "**文章阅读** — 粘贴任何URL并以音频形式收听文章",
            "**PDF支持** — 上传并收听PDF文档",
            "**多种声音** — 从ElevenLabs的高级声音库中选择",
            "**速度控制** — 将播放速度从0.5倍调整到3倍",
            "**移动应用** — 通过iOS和Android应用随时随地收听",
            "**剪贴板阅读** — 一键阅读复制的文本"
        )
        pricing_table = @(
            @("Free","$0","Basic voices, limited usage"),
            @("Starter","$5/mo","Premium voices, unlimited reading")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础声音，有限使用"),
            @("入门版","$5/月","高级声音，无限阅读")
        )
        pros = @(
            "Industry-leading voice quality",
            "Great for consuming content while multitasking",
            "Supports multiple input formats",
            "Very affordable at $5/mo"
        )
        zh_pros = @(
            "业界领先的语音质量",
            "非常适合多任务处理时消费内容",
            "支持多种输入格式",
            "每月$5非常实惠"
        )
        cons = @(
            "Requires ElevenLabs account",
            "Some documents may need formatting fixes",
            "Reading long books can be expensive in credits"
        )
        zh_cons = @(
            "需要ElevenLabs账户",
            "某些文档可能需要格式修复",
            "阅读长篇书籍可能会消耗较多积分"
        )
        best_for = "Busy professionals, students, and anyone who wants to consume written content as audio on the go."
        zh_best_for = "忙碌的专业人士、学生，以及任何想在旅途中以音频形式消费书面内容的人。"
        compare_headers = @("Feature","ElevenReader","Speechify","NaturalReader")
        compare_rows = @(
            @("Voice quality","Excellent","Good","Good"),
            @("Price","$0-$5/mo","$29/mo","$10/mo"),
            @("URL reading","✅","✅","❌"),
            @("PDF support","✅","✅","✅"),
            @("Mobile app","✅","✅","✅")
        )
        verdict = "Rating: 4.4/5`n`nElevenReader is the best AI reading app thanks to ElevenLabs' superior voice quality. At $5/mo, it's the best value for text-to-speech reading."
        zh_verdict = "评分：4.4/5`n`nElevenReader凭借ElevenLabs卓越的语音质量成为最佳AI阅读应用。每月$5是文本转语音阅读的最佳性价比。"
        zh_compare_headers = @("功能","ElevenReader","Speechify","NaturalReader")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Search - you
    @{
        slug = "you"
        title = "You.com — Best AI Search Engine"
        desc = "Complete review of You.com — AI-powered search engine that provides summarized answers with citations, AI chat, and no ads."
        zh_title = "You.com — 最佳AI搜索引擎"
        zh_desc = "You.com完整评测——AI驱动的搜索引擎，提供带引用的摘要答案、AI聊天和无广告体验。"
        categories = @("search")
        tags = @("You.com","search","AI","chat")
        type_val = "tool"
        url = "https://you.com"
        developer = "You.com"
        founded = "2021"
        pricing = "Free; You Pro $20/mo"
        category = @("search")
        logo = "https://logo.clearbit.com/you.com"
        intro = "**You.com** is an AI-powered search engine that provides direct, cited answers instead of just links. It combines web search with AI chat, coding assistance, and creative writing tools."
        zh_intro = "**You.com** 是一款AI驱动的搜索引擎，提供直接的、带引用的答案而不仅仅是链接。它将网页搜索与AI聊天、编程辅助和创意写作工具相结合。"
        features = @(
            "**AI Search** — Get summarized answers with source citations",
            "**YouChat** — Chat with AI for follow-up questions",
            **Mode Selection** — Choose from Research, Genius, Create, and more",
            **Code Generation** — Built-in AI coding assistant",
            **No Ads** — Clean, ad-free search experience",
            **Privacy Controls** — Customizable privacy settings"
        )
        zh_features = @(
            "**AI搜索** — 获取带来源引用的摘要答案",
            "**YouChat** — 与AI聊天以追问更多问题",
            "**模式选择** — 从研究、天才、创作等多种模式中选择",
            "**代码生成** — 内置AI编程助手",
            "**无广告** — 干净无广告的搜索体验",
            "**隐私控制** — 可定制的隐私设置"
        )
        pricing_table = @(
            @("Free","$0","Basic AI search, limited queries"),
            @("You Pro","$20/mo","Unlimited AI, premium models, priority")
        )
        zh_pricing_table = @(
            @("免费版","$0","基础AI搜索，有限查询"),
            @("Pro版","$20/月","无限AI，高级模型，优先访问")
        )
        pros = @(
            "Cited answers build trust in results",
            "Ad-free experience is refreshing",
            "Multiple AI modes for different needs",
            "Good for research with sources"
        )
        zh_pros = @(
            "带引用的答案增强对结果的信任",
            "无广告体验令人耳目一新",
            "多种AI模式满足不同需求",
            "适合需要来源的研究"
        )
        cons = @(
            "AI summaries can sometimes be inaccurate",
            "Not as comprehensive as Google for some searches",
            "Pro plan is same price as Perplexity Pro"
        )
        zh_cons = @(
            "AI摘要有时可能不准确",
            "某些搜索不如Google全面",
            "Pro版价格与Perplexity Pro相同"
        )
        best_for = "Researchers, students, and professionals who want AI-powered search with cited sources."
        zh_best_for = "需要带来源引用的AI搜索的研究人员、学生和专业人士。"
        compare_headers = @("Feature","You.com","Perplexity","Google")
        compare_rows = @(
            @("AI summaries","✅","✅","✅ (SGE)"),
            @("Source citations","✅","✅","❌"),
            @("AI chat","✅","✅","❌"),
            @("Ad-free","✅","✅","❌"),
            @("Price (Pro)","$20/mo","$20/mo","Free")
        )
        verdict = "Rating: 4.2/5`n`nYou.com is a strong AI search engine that competes well with Perplexity. Its multiple modes and ad-free experience make it worth trying."
        zh_verdict = "评分：4.2/5`n`nYou.com是与Perplexity有力竞争的AI搜索引擎。其多种模式和无广告体验值得一试。"
        zh_compare_headers = @("功能","You.com","Perplexity","Google")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Search - phind
    @{
        slug = "phind"
        title = "Phind — Best AI Search for Developers"
        desc = "Complete review of Phind — AI-powered search engine built specifically for developers, with code-aware search, technical explanations, and pair programming."
        zh_title = "Phind — 最佳开发者AI搜索引擎"
        zh_desc = "Phind完整评测——专为开发者构建的AI搜索引擎，具备代码感知搜索、技术解释和结对编程功能。"
        categories = @("search","coding")
        tags = @("Phind","developer","search","coding")
        type_val = "tool"
        url = "https://www.phind.com"
        developer = "Phind"
        founded = "2022"
        pricing = "Free; Pro $10/mo"
        category = @("search")
        logo = "https://logo.clearbit.com/phind.com"
        intro = "**Phind** is an AI search engine purpose-built for developers. It understands code context, searches technical documentation, and provides detailed explanations with code examples — making it the go-to search tool for programmers."
        zh_intro = "**Phind** 是一款专为开发者构建的AI搜索引擎。它理解代码上下文，搜索技术文档，并提供带有代码示例的详细解释——使其成为程序员的搜索首选工具。"
        features = @(
            "**Developer-First Search** — Optimized for technical and coding queries",
            "**Code Generation** — Generates code solutions with explanations",
            **Documentation Search** — Searches across official docs, Stack Overflow, GitHub",
            **Context Awareness** — Understands your codebase and framework context",
            **Pair Programming** — Interactive coding assistance with AI",
            **GPT-4 Powered** — Uses latest AI models for accurate answers"
        )
        zh_features = @(
            "**开发者优先搜索** — 针对技术和编程查询优化",
            "**代码生成** — 生成代码解决方案并附带解释",
            "**文档搜索** — 搜索官方文档、Stack Overflow、GitHub",
            "**上下文感知** — 理解您的代码库和框架上下文",
            "**结对编程** — 与AI交互式编程辅助",
            "**GPT-4驱动** — 使用最新AI模型提供准确答案"
        )
        pricing_table = @(
            @("Free","$0","Limited queries, GPT-3.5"),
            @("Pro","$10/mo","Unlimited, GPT-4, priority access")
        )
        zh_pricing_table = @(
            @("免费版","$0","有限查询，GPT-3.5"),
            @("专业版","$10/月","无限查询，GPT-4，优先访问")
        )
        pros = @(
            "Dramatically faster than searching Stack Overflow",
            "Code-aware search understands developer intent",
            "Excellent for debugging and learning new tech",
            "Affordable Pro plan"
        )
        zh_pros = @(
            "比搜索Stack Overflow快得多",
            "代码感知搜索理解开发者意图",
            "非常适合调试和学习新技术",
            "实惠的Pro计划"
        )
        cons = @(
            "Developer-focused — not useful for general queries",
            "Can hallucinate incorrect code",
            "Less polished UX than Perplexity"
        )
        zh_cons = @(
            "聚焦开发者——对一般查询不实用",
            "可能会产生错误的代码",
            "UX不如Perplexity精致"
        )
        best_for = "Software developers who want fast, code-aware search for debugging, learning, and technical problem-solving."
        zh_best_for = "希望获得快速、代码感知搜索用于调试、学习和解决技术问题的软件开发者。"
        compare_headers = @("Feature","Phind","You.com","Perplexity")
        compare_rows = @(
            @("Code-aware search","✅","Partial","❌"),
            @("Stack Overflow search","✅","❌","❌"),
            @("Code generation","✅","✅","❌"),
            @("Price (Pro)","$10/mo","$20/mo","$20/mo"),
            @("Best for","Developers","General use","Research")
        )
        verdict = "Rating: 4.3/5`n`nPhind is the best AI search engine for developers. It understands code context and provides faster answers than scrolling through Stack Overflow."
        zh_verdict = "评分：4.3/5`n`nPhind是开发者的最佳AI搜索引擎。它理解代码上下文，比翻阅Stack Overflow更快地提供答案。"
        zh_compare_headers = @("功能","Phind","You.com","Perplexity")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Detection - undetectable-ai
    @{
        slug = "undetectable-ai"
        title = "Undetectable AI — Best AI Content Humanizer"
        desc = "Complete review of Undetectable AI — AI content detection and humanization tool that makes AI-generated text pass as human-written."
        zh_title = "Undetectable AI — 最佳AI内容人化工具"
        zh_desc = "Undetectable AI完整评测——AI内容检测和人化工具，使AI生成的文本通过检测仪检测。"
        categories = @("writing")
        tags = @("Undetectable AI","detection","humanizer","writing")
        type_val = "tool"
        url = "https://undetectable.ai"
        developer = "Undetectable AI"
        founded = "2023"
        pricing = "Free trial; Pro $9.99/mo"
        category = @("writing")
        logo = "https://logo.clearbit.com/undetectable.ai"
        intro = "**Undetectable AI** is a tool that both detects AI-generated content and humanizes it to bypass AI detectors. It rewrites AI text to sound more natural and human-written while preserving the original meaning."
        zh_intro = "**Undetectable AI** 是一款既能检测AI生成内容又能人化以绕过AI检测器的工具。它重写AI文本使其听起来更自然、更像人写的，同时保留原始含义。"
        features = @(
            "**AI Detection** — Checks text against multiple AI detectors simultaneously",
            "**Humanization** — Rewrites AI text to sound human-written",
            **Bypass Detectors** — Passes Turnitin, GPTZero, Originality.ai",
            "**Readability Check** — Ensures rewritten text maintains readability",
            **Plagiarism Free** — Guarantees rewritten content is original",
            **Batch Processing** — Process multiple documents at once"
        )
        zh_features = @(
            "**AI检测** — 同时对照多个AI检测器检查文本",
            "**人化处理** — 重写AI文本使其听起来像人写的",
            "**绕过检测器** — 通过Turnitin、GPTZero、Originality.ai",
            "**可读性检查** — 确保重写文本保持可读性",
            "**无抄袭** — 保证重写内容是原创的",
            "**批量处理** — 一次处理多个文档"
        )
        pricing_table = @(
            @("Free Trial","$0","250 words"),
            @("Pro","$9.99/mo","10,000 words/mo"),
            @("Business","$29.99/mo","50,000 words/mo")
        )
        zh_pricing_table = @(
            @("免费试用","$0","250词"),
            @("专业版","$9.99/月","每月10,000词"),
            @("商业版","$29.99/月","每月50,000词")
        )
        pros = @(
            "Effectively bypasses most AI detectors",
            "Combines detection and humanization in one tool",
            "Affordable pricing",
            "Maintains original meaning well"
        )
        zh_pros = @(
            "有效绕过大多数AI检测器",
            "将检测和人化功能集于一体",
            "价格实惠",
            "很好地保持原始含义"
        )
        cons = @(
            "Humanized text can sometimes read awkwardly",
            "Detected text may need multiple passes",
            "Ethical concerns about bypassing AI detection"
        )
        zh_cons = @(
            "人化文本有时读起来不够自然",
            "被检测的文本可能需要多次处理",
            "绕过AI检测存在伦理问题"
        )
        best_for = "Content marketers, SEO professionals, and writers who use AI tools but need their content to pass AI detection checks."
        zh_best_for = "使用AI工具但需要内容通过AI检测检查的内容营销人员、SEO专业人士和写作者。"
        compare_headers = @("Feature","Undetectable AI","StealthGPT","QuillBot")
        compare_rows = @(
            @("AI detection","✅","❌","❌"),
            @("Humanization","✅","✅","❌"),
            @("Bypass rate","High","High","N/A"),
            @("Price (Pro)","$9.99/mo","$14.99/mo","Free-$19.99/mo"),
            @("Ethical use","Questionable","Questionable","Fine")
        )
        verdict = "Rating: 3.5/5`n`nUndetectable AI works as advertised but raises ethical questions. Use responsibly and always disclose AI assistance."
        zh_verdict = "评分：3.5/5`n`nUndetectable AI如其宣传那样工作，但引发伦理问题。请负责任地使用，始终披露AI辅助。"
        zh_compare_headers = @("功能","Undetectable AI","StealthGPT","QuillBot")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI Detection - stealthgpt
    @{
        slug = "stealthgpt"
        title = "StealthGPT — Best AI Detection Bypass"
        desc = "Complete review of StealthGPT — AI writing tool that generates undetectable content designed to bypass AI detectors like Turnitin and GPTZero."
        zh_title = "StealthGPT — 最佳AI检测绕过工具"
        zh_desc = "StealthGPT完整评测——AI写作工具，生成旨在绕过Turnitin和GPTZero等AI检测器的不可检测内容。"
        categories = @("writing")
        tags = @("StealthGPT","undetectable","writing","bypass")
        type_val = "tool"
        url = "https://stealthgpt.ai"
        developer = "StealthGPT"
        founded = "2023"
        pricing = "Free trial; Essential $14.99/mo; Pro $29.99/mo"
        category = @("writing")
        logo = "https://logo.clearbit.com/stealthgpt.ai"
        intro = "**StealthGPT** is an AI writing tool specifically designed to generate content that bypasses AI detection tools. It produces human-sounding text that passes detectors like Turnitin, GPTZero, and Originality.ai."
        zh_intro = "**StealthGPT** 是一款专门设计用于生成绕过AI检测工具内容的AI写作工具。它产生类人的文本，能够通过Turnitin、GPTZero和Originality.ai等检测器。"
        features = @(
            "**Undetectable Writing** — Generates text that passes AI detectors",
            **Multiple Models** — Choose different writing styles and tones",
            **SEO Mode** — Generate SEO-optimized undetectable content",
            **Essay Writer** — Built-in essay and article generation",
            **Bypass Guarantee** — Claims to bypass all major detectors",
            **API Access** — Integrate into your workflow"
        )
        zh_features = @(
            "**不可检测写作** — 生成通过AI检测器的文本",
            "**多种模型** — 选择不同的写作风格和语调",
            "**SEO模式** — 生成SEO优化的不可检测内容",
            "**论文写作器** — 内置论文和文章生成",
            "**绕过保证** — 声称绕过所有主要检测器",
            "**API访问** — 集成到您的工作流中"
        )
        pricing_table = @(
            @("Free Trial","$0","Limited words"),
            @("Essential","$14.99/mo","Basic undetectable generation"),
            @("Pro","$29.99/mo","Unlimited, SEO mode, API")
        )
        zh_pricing_table = @(
            @("免费试用","$0","有限词数"),
            @("基础版","$14.99/月","基础不可检测生成"),
            @("专业版","$29.99/月","无限生成，SEO模式，API")
        )
        pros = @(
            "Content genuinely passes most detectors",
            "Multiple writing styles available",
            "Built-in essay and article tools",
            "SEO mode for content marketers"
        )
        zh_pros = @(
            "内容确实通过大多数检测器",
            "多种写作风格可选",
            "内置论文和文章工具",
            "面向内容营销人员的SEO模式"
        )
        cons = @(
            "Quality can be inconsistent",
            "Significant ethical concerns",
            "More expensive than Undetectable AI",
            "Detectors are constantly improving"
        )
        zh_cons = @(
            "质量可能不稳定",
            "存在重大伦理问题",
            "比Undetectable AI更贵",
            "检测器在不断改进"
        )
        best_for = "Content creators who need AI-assisted writing that passes detection checks. Use ethically and with disclosure."
        zh_best_for = "需要通过检测检查的AI辅助写作的内容创作者。请合乎道德地使用并做出披露。"
        compare_headers = @("Feature","StealthGPT","Undetectable AI","QuillBot")
        compare_rows = @(
            @("AI detection bypass","✅","✅","❌"),
            @("Writing quality","Good","Good","Good"),
            @("SEO mode","✅","❌","❌"),
            @("Price","$14.99+/mo","$9.99+/mo","Free-$19.99/mo"),
            @("Essay generation","✅","❌","❌")
        )
        verdict = "Rating: 3.3/5`n`nStealthGPT works but raises serious ethical concerns. Use responsibly — AI assistance should be disclosed, not hidden."
        zh_verdict = "评分：3.3/5`n`nStealthGPT有效但引发严重的伦理问题。请负责任地使用——AI辅助应当被披露，而非隐藏。"
        zh_compare_headers = @("功能","StealthGPT","Undetectable AI","QuillBot")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI SEO - surfer-seo
    @{
        slug = "surfer-seo"
        title = "SurferSEO — Best AI SEO Optimization"
        desc = "Complete review of SurferSEO — AI-powered SEO tool that provides content optimization, keyword research, and SERP analysis for higher rankings."
        zh_title = "SurferSEO — 最佳AI SEO优化工具"
        zh_desc = "SurferSEO完整评测——AI驱动的SEO工具，提供内容优化、关键词研究和SERP分析以获得更高排名。"
        categories = @("writing")
        tags = @("SurferSEO","SEO","content","optimization")
        type_val = "tool"
        url = "https://surferseo.com"
        developer = "Surfer SEO"
        founded = "2017"
        pricing = "Essential $89/mo; Scale $129/mo; Enterprise $219/mo"
        category = @("writing")
        logo = "https://logo.clearbit.com/surferseo.com"
        intro = "**SurferSEO** is an AI-powered SEO platform that helps you create content optimized for search engines. It provides content scoring, keyword research, SERP analysis, and an AI writing assistant."
        zh_intro = "**SurferSEO** 是一款AI驱动的SEO平台，帮助您创建针对搜索引擎优化的内容。它提供内容评分、关键词研究、SERP分析和AI写作助手。"
        features = @(
            "**Content Score** — Real-time SEO score for your articles",
            "**SERP Analyzer** — Analyze top-ranking pages and their strategies",
            "**Keyword Research** — AI-powered keyword discovery and clustering",
            **AI Writing** — Generate SEO-optimized outlines and paragraphs",
            **Audit** — Audit existing content for SEO issues",
            **Outline Builder** — Generate article outlines from SERP data"
        )
        zh_features = @(
            "**内容评分** — 为您的文章提供实时SEO评分",
            "**SERP分析器** — 分析排名靠前的页面及其策略",
            "**关键词研究** — AI驱动的关键词发现和聚类",
            "**AI写作** — 生成SEO优化的提纲和段落",
            "**审计** — 审计现有内容的SEO问题",
            "**提纲构建器** — 从SERP数据生成文章提纲"
        )
        pricing_table = @(
            @("Essential","$89/mo","Content editor, keyword research"),
            @("Scale","$129/mo","AI writing, audits, API"),
            @("Enterprise","$219/mo","Custom limits, white-label")
        )
        zh_pricing_table = @(
            @("基础版","$89/月","内容编辑器，关键词研究"),
            @("扩展版","$129/月","AI写作，审计，API"),
            @("企业版","$219/月","自定义限制，白标")
        )
        pros = @(
            "Data-driven content optimization",
            "Excellent SERP analysis",
            "AI writing produces SEO-friendly content",
            "Clean, intuitive interface"
        )
        zh_pros = @(
            "数据驱动的内容优化",
            "出色的SERP分析",
            "AI写作产生SEO友好的内容",
            "简洁直观的界面"
        )
        cons = @(
            "Expensive — cheapest plan is $89/mo",
            "No free tier available",
            "AI writing quality not as good as dedicated AI writers"
        )
        zh_cons = @(
            "昂贵——最便宜的计划$89/月",
            "没有免费版",
            "AI写作质量不如专门的AI写作工具"
        )
        best_for = "SEO professionals, content marketers, and agencies that need data-driven content optimization for search rankings."
        zh_best_for = "需要数据驱动内容优化以获得搜索排名的SEO专业人士、内容营销人员和代理商。"
        compare_headers = @("Feature","SurferSEO","Semrush","Clearscope")
        compare_rows = @(
            @("Content scoring","✅","✅","✅"),
            @("AI writing","✅","❌","❌"),
            @("SERP analysis","✅","✅","✅"),
            @("Price (entry)","$89/mo","$130/mo","$170/mo"),
            @("Ease of use","Excellent","Complex","Good")
        )
        verdict = "Rating: 4.2/5`n`nSurferSEO is the best SEO content tool. It combines data-driven optimization with AI writing — ideal for content teams focused on organic growth."
        zh_verdict = "评分：4.2/5`n`nSurferSEO是最佳SEO内容工具。它将数据驱动的优化与AI写作相结合——非常适合专注于自然增长的内容团队。"
        zh_compare_headers = @("功能","SurferSEO","Semrush","Clearscope")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # AI 3D - poly
    @{
        slug = "poly"
        title = "Poly — Best AI 3D Texture Generator"
        desc = "Complete review of Poly — AI-powered 3D texture and material generator that creates PBR materials from text prompts and images for game dev and design."
        zh_title = "Poly — 最佳AI 3D材质生成器"
        zh_desc = "Poly完整评测——AI驱动的3D纹理和材质生成器，从文本提示和图像创建PBR材质，用于游戏开发和设计。"
        categories = @("3d")
        tags = @("Poly","3D","texture","PBR","material")
        type_val = "tool"
        url = "https://poly.cam"
        developer = "Poly"
        founded = "2022"
        pricing = "Free; Pro $30/mo"
        category = @("3d")
        logo = "https://logo.clearbit.com/poly.cam"
        intro = "**Poly** is an AI-powered 3D texture and PBR material generator. It creates photorealistic textures and materials from text descriptions or reference images, ready for use in games, AR/VR, and 3D design."
        zh_intro = "**Poly** 是一款AI驱动的3D纹理和PBR材质生成器。它从文本描述或参考图像创建逼真的纹理和材质，可直接用于游戏、AR/VR和3D设计。"
        features = @(
            "**Text-to-Texture** — Generate PBR textures from text descriptions",
            "**Image-to-Texture** — Create textures from reference photos",
            **PBR Materials** — Generates complete PBR material sets (albedo, normal, roughness)",
            **3D Capture** — Scan real-world objects with your phone",
            **Seamless Textures** — AI creates perfectly seamless tileable textures",
            **Export Formats** — OBJ, GLTF, USDZ, FBX support"
        )
        zh_features = @(
            "**文本转纹理** — 从文本描述生成PBR纹理",
            "**图像转纹理** — 从参考照片创建纹理",
            "**PBR材质** — 生成完整的PBR材质集（反照率、法线、粗糙度）",
            "**3D捕获** — 用手机扫描真实世界物体",
            "**无缝纹理** — AI创建完美无缝的可平铺纹理",
            "**导出格式** — 支持OBJ、GLTF、USDZ、FBX"
        )
        pricing_table = @(
            @("Free","$0","10 textures/mo, basic quality"),
            @("Pro","$30/mo","Unlimited textures, high quality, API")
        )
        zh_pricing_table = @(
            @("免费版","$0","每月10个纹理，基础质量"),
            @("专业版","$30/月","无限纹理，高质量，API")
        )
        pros = @(
            "Incredibly realistic PBR materials",
            "Text-to-texture saves texture artists hours",
            "Phone-based 3D scanning is impressive",
            "Export to all major 3D formats"
        )
        zh_pros = @(
            "极其逼真的PBR材质",
            "文本转纹理为纹理艺术家节省数小时",
            "基于手机的3D扫描令人印象深刻",
            "导出到所有主要3D格式"
        )
        cons = @(
            "Pro plan is expensive",
            "Free tier is very limited",
            "Generated textures sometimes need manual refinement"
        )
        zh_cons = @(
            "Pro版价格较高",
            "免费版非常有限",
            "生成的纹理有时需要手动调整"
        )
        best_for = "3D artists, game developers, and designers who need PBR textures and materials quickly."
        zh_best_for = "需要快速获取PBR纹理和材质的3D艺术家、游戏开发者和设计师。"
        compare_headers = @("Feature","Poly","Meshy","Tripo3D")
        compare_rows = @(
            @("Texture generation","✅","✅","✅"),
            @("3D scanning","✅","❌","❌"),
            @("PBR materials","✅","✅","✅"),
            @("Price (Pro)","$30/mo","$20/mo","$15/mo"),
            @("Best for","Textures/Materials","Full 3D models","Full 3D models")
        )
        verdict = "Rating: 4.1/5`n`nPoly excels at texture and material generation. If you need PBR textures specifically, it's the best tool available."
        zh_verdict = "评分：4.1/5`n`nPoly在纹理和材质生成方面表现出色。如果您特别需要PBR纹理，它是最佳工具。"
        zh_compare_headers = @("功能","Poly","Meshy","Tripo3D")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # Other - presentations-ai
    @{
        slug = "presentations-ai"
        title = "Presentations.ai — Best AI Presentation Maker"
        desc = "Complete review of Presentations.ai — AI presentation maker that creates professional, customizable slide decks from text prompts in seconds."
        zh_title = "Presentations.ai — 最佳AI演示文稿制作工具"
        zh_desc = "Presentations.ai完整评测——AI演示文稿制作工具，几秒内从文本提示创建专业可定制的幻灯片。"
        categories = @("productivity")
        tags = @("Presentations.ai","presentation","slides","AI")
        type_val = "tool"
        url = "https://presentations.ai"
        developer = "Presentations.ai"
        founded = "2023"
        pricing = "Free; Pro $10/mo; Team $20/user/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/presentations.ai"
        intro = "**Presentations.ai** is an AI-powered presentation maker that creates professional slide decks from simple text prompts. It offers beautiful templates, smart layouts, and collaborative editing."
        zh_intro = "**Presentations.ai** 是一款AI驱动的演示文稿制作工具，从简单的文本提示创建专业幻灯片。它提供美观的模板、智能布局和协作编辑。"
        features = @(
            "**AI Slide Generation** — Create full presentations from a topic or outline",
            **Smart Layouts** — AI-designed slide layouts that look professional",
            **Template Library** — Hundreds of professionally designed templates",
            **Collaboration** — Real-time team editing and commenting",
            **Brand Kit** — Apply company branding automatically",
            **Export** — Download as PPTX, PDF, or share via link"
        )
        zh_features = @(
            "**AI幻灯片生成** — 从主题或大纲创建完整演示文稿",
            "**智能布局** — AI设计的专业幻灯片布局",
            "**模板库** — 数百个专业设计的模板",
            "**协作** — 实时团队编辑和评论",
            "**品牌套件** — 自动应用公司品牌",
            "**导出** — 下载为PPTX、PDF或通过链接分享"
        )
        pricing_table = @(
            @("Free","$0","3 presentations, basic features"),
            @("Pro","$10/mo","Unlimited, all templates, brand kit"),
            @("Team","$20/user/mo","Team collaboration, admin controls")
        )
        zh_pricing_table = @(
            @("免费版","$0","3个演示文稿，基础功能"),
            @("专业版","$10/月","无限创建，全部模板，品牌套件"),
            @("团队版","$20/用户/月","团队协作，管理控制")
        )
        pros = @(
            "Creates presentations in seconds",
            "Professional-looking designs out of the box",
            "More affordable than Beautiful.ai",
            "Good template selection"
        )
        zh_pros = @(
            "几秒内创建演示文稿",
            "开箱即用的专业外观设计",
            "比Beautiful.ai更实惠",
            "不错的模板选择"
        )
        cons = @(
            "Limited customization compared to PowerPoint",
            "AI content can be generic",
            "Export quality varies"
        )
        zh_cons = @(
            "与PowerPoint相比自定义功能有限",
            "AI内容可能比较普通",
            "导出质量不稳定"
        )
        best_for = "Professionals, students, and anyone who needs to quickly create professional presentations without design skills."
        zh_best_for = "需要快速创建专业演示文稿但缺乏设计技能的专业人士、学生和任何人。"
        compare_headers = @("Feature","Presentations.ai","Gamma","Beautiful.ai")
        compare_rows = @(
            @("AI generation","✅","✅","✅"),
            @("PPTX export","✅","✅","✅"),
            @("Collaboration","✅","✅","✅"),
            @("Price (Pro)","$10/mo","$10/mo","$13/mo"),
            @("Templates","Hundreds","Good","Good")
        )
        verdict = "Rating: 4.0/5`n`nPresentations.ai is a solid AI presentation tool at a great price. It's the best budget option for quick, professional slides."
        zh_verdict = "评分：4.0/5`n`nPresentations.ai是一款价格出色的AI演示文稿工具。它是快速制作专业幻灯片的最佳预算选择。"
        zh_compare_headers = @("功能","Presentations.ai","Gamma","Beautiful.ai")
        section_names = @("Key Features","Pricing","Pros","Cons","Who It's Best For","How It Compares","Verdict")
        zh_section_names = @("核心功能","定价","优势","劣势","适合人群","对比评测","总结")
    },
    # Other - plus-ai
    @{
        slug = "plus-ai"
        title = "Plus AI — Best Google Slides AI"
        desc = "Complete review of Plus AI — AI-powered Google Slides add-on that creates and enhances presentations directly inside Google Slides."
        zh_title = "Plus AI — 最佳Google Slides AI工具"
        zh_desc = "Plus AI完整评测——AI驱动的Google Slides插件，直接在Google Slides中创建和增强演示文稿。"
        categories = @("productivity")
        tags = @("Plus AI","Google Slides","presentation","AI")
        type_val = "tool"
        url = "https://www.plusdocs.com/plus-ai"
        developer = "Plus AI"
        founded = "2022"
        pricing = "Free trial; Essentials $10/mo; Pro $20/mo"
        category = @("productivity")
        logo = "https://logo.clearbit.com/plusdocs.com"
        intro = "**Plus AI** is an AI-powered Google Slides add-on that creates, edits, and enhances presentations directly inside Google Slides. No new tool to learn — it works where you already work."
        zh_intro = "**Plus AI** 是一款AI驱动的Google Slides插件，直接在Google Slides中创建、编辑和增强演示文稿。无需学习新工具——在您已使用的工具中工作。"
        features = @(
            "**In-Slides AI** — Works directly inside Google Slides",
            **Presentation Generator** — Create full decks from topics or outlines",
            **Slide Editor** — Rewrite, reformat, and enhance individual slides",
            **Theme Matching** — Matches your existing slide theme",
            **Snap to Brand** — Apply company colors and fonts automatically",
            **Charts & Diagrams** — AI-generated data visualizations"
        )
        zh_features = @(
            "**幻灯片内AI** — 直接在Google Slides中工作",
            "**演示文稿生成器** — 从主题或大纲创建完整幻灯片",
            "**幻灯片编辑器** — 重写、重新格式化和增强单个幻灯片",
            "**主题匹配** — 匹配您现有的幻灯片主题",
            "**品牌适配** — 自动应用公司颜色和字体",
            "**图表和图示** —— AI生成的数据可视化"
        )
        pricing_table = @(
            @("Free Trial","$0","3 presentations"),
            @("Essentials","$10/mo","Unlimited creation, basic editing"),
            @("Pro","$20/mo","Full editing, team features")
        )
        zh_pricing_table = @(
            @("免费试用","$0","3个演示文稿"),
            @("基础版","$10/月","无限创建，基础编辑"),
            @("专业版","$20/月","完整编辑，团队功能")
        )
        pros = @(
            "Works natively in Google Slides — zero learning curve",
            "Integrates with existing workflows",
            "Good slide designs and layouts",
            "Affordable pricing"
        )
        zh_pros = @(
            "原生在Google Slides中工作——零学习曲线",
            "与现有工作流集成",
            "出色的幻灯片设计和布局",
            "价格实惠"
        )
        cons = @(
            "Google Slides only — no PowerPoint",
            "Design quality not as high as standalone tools",
            "Limited compared to full AI presentation platforms"
        )
        zh_cons = @(
            "仅支持Google Slides——不支持PowerPoint",
            "设计质量不如独立工具",
            "与完整的AI演示文稿平台相比功能有限"
        )
        best_for = "Google Workspace users who want AI presentation help without leaving Google Slides."
        zh_best_for = "希望在不离开Google Slides的情况下获得AI演示文稿帮助的Google Workspace用户。"
        compare_headers = @("Feature","Plus AI","Presentations.ai","Gamma")
        compare_rows = @(
            @("Google Slides native","�