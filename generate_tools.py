"""Generate 42 new AI tool pages (EN + ZH) for aihandpicked.xyz"""
import os

BASE = r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked"
TOOLS_DIR = os.path.join(BASE, "content", "tools")
ZH_DIR = os.path.join(BASE, "content", "zh", "tools")

def make_tools():
    tools = []
    
    def add(slug, name, zh_name, en_desc, zh_desc, en_cats, en_tags, url, dev, founded, pricing_s, tool_cats, logo,
            en_intro, zh_intro, features, pricing_rows, pros, cons, en_best, zh_best, 
            en_comp_h, en_comp_rows, zh_comp_h, en_verdict, zh_verdict):
        tools.append({
            'slug': slug, 'name': name, 'zh_name': zh_name,
            'en_desc': en_desc, 'zh_desc': zh_desc,
            'en_cats': en_cats, 'en_tags': en_tags,
            'url': url, 'dev': dev, 'founded': founded,
            'pricing_s': pricing_s, 'tool_cats': tool_cats, 'logo': logo,
            'en_intro': en_intro, 'zh_intro': zh_intro,
            'features': features,  # [(en_name, zh_name, en_desc), ...]
            'pricing': pricing_rows,  # [(plan, price, en_feat, zh_feat), ...]
            'pros': pros,  # [(en, zh), ...]
            'cons': cons,  # [(en, zh), ...]
            'en_best': en_best, 'zh_best': zh_best,
            'en_comp_h': en_comp_h, 'en_comp_rows': en_comp_rows,
            'zh_comp_h': zh_comp_h, 'zh_comp_rows': en_comp_rows,  # same rows work for both
            'en_verdict': en_verdict, 'zh_verdict': zh_verdict,
        })
    
    # --- AI Productivity ---
    add("shortwave", "Shortwave", "Shortwave",
        "AI-powered email client built on Gmail with smart sorting, AI replies, and inbox zero automation.",
        "基于Gmail的AI邮件客户端，智能分类、AI回复和收件箱清零自动化。",
        ["writing","productivity"], ["Shortwave","email","productivity","Gmail"],
        "https://shortwave.com", "Shortwave (Ex-Google team)", "2023",
        "Free; Pro $19/mo", ["productivity"], "https://logo.clearbit.com/shortwave.com",
        "**Shortwave** is an AI-powered email client built on top of Gmail. Created by ex-Google engineers, it uses AI to categorize, prioritize, and draft your emails automatically.",
        "**Shortwave** 是一款基于Gmail的AI邮件客户端。由前谷歌工程师团队打造，利用AI自动分类、优先排序甚至自动起草邮件。",
        [("AI Email Sorting", "AI邮件分类", "Automatically categorizes emails by importance and topic"),
         ("AI Draft Replies", "AI起草回复", "Generates context-aware reply suggestions"),
         ("Inbox Zero Automation", "收件箱清零自动化", "AI helps archive and organize to reach inbox zero"),
         ("Gmail Integration", "Gmail集成", "Works directly with your existing Gmail account"),
         ("Daily Summary", "每日摘要", "AI-generated daily email digest"),
         ("Search Enhancement", "搜索增强", "Natural language search across all emails")],
        [("Free","$0","Basic AI sorting, 1 account","基础AI分类，1个账户"),
         ("Pro","$19/mo","AI replies, unlimited accounts","AI回复，无限账户")],
        [("Transforms chaotic Gmail inbox into organized workflow","将混乱的Gmail收件箱转变为有序的工作流程"),
         ("AI replies save significant time on routine emails","AI回复在常规邮件上节省大量时间"),
         ("Beautiful, intuitive interface","美观直观的界面"),
         ("Works with existing Gmail — no migration needed","直接使用现有Gmail，无需迁移")],
        [("Gmail-only — no Outlook or other providers","仅支持Gmail——不支持Outlook等其他提供商"),
         ("Pro plan relatively expensive for email tool","Pro版对于邮件工具来说相对较贵"),
         ("AI replies sometimes need manual editing","AI回复有时需要手动编辑")],
        "Gmail power users, professionals drowning in email, and remote teams wanting AI-assisted inbox management.",
        "Gmail重度用户、被邮件淹没的专业人士，以及需要AI辅助收件箱管理的远程团队。",
        ["Feature","Shortwave","Superhuman","Notion Mail"],
        [["AI email sorting","✅","✅","✅"],["AI draft replies","✅","✅","✅"],["Gmail native","✅","✅","❌"],["Daily AI summary","✅","❌","❌"],["Price (Pro)","$19/mo","$30/mo","$10/mo"]],
        ["功能","Shortwave","Superhuman","Notion Mail"],
        "**Rating: 4.2/5**\n\nShortwave is the best AI email client for Gmail users. The free tier is surprisingly capable, and Pro ($19/mo) is a game-changer for email-heavy professionals.",
        "**评分：4.2/5**\n\nShortwave是Gmail用户最佳的AI邮件客户端。免费版功能出人意料地强大，Pro版是邮件密集型专业人士的革命性工具。")

    add("tldv", "tl;dv", "tl;dv",
        "AI meeting recorder that auto-transcribes, summarizes, and highlights key moments from Zoom, Google Meet, and Teams calls.",
        "AI会议录制工具，自动转录、总结并标记Zoom、Google Meet和Teams通话中的关键时刻。",
        ["productivity"], ["tl;dv","meeting","transcription","productivity"],
        "https://tldv.io", "tl;dv", "2020", "Free; Pro $12/mo; Business $20/mo",
        ["productivity"], "https://logo.clearbit.com/tldv.io",
        "**tl;dv** is an AI-powered meeting recorder that automatically transcribes, summarizes, and creates highlight reels from video calls on Zoom, Google Meet, and Microsoft Teams.",
        "**tl;dv** 是一款AI驱动的会议录制工具，可自动转录、总结并从Zoom、Google Meet和Microsoft Teams视频通话中创建精彩集锦。",
        [("Auto Transcription", "自动转录", "Real-time transcription in 30+ languages"),
         ("AI Summaries", "AI摘要", "Instant meeting summaries with key decisions"),
         ("Highlight Clips", "精彩片段", "Create shareable video clips of key moments"),
         ("Speaker Detection", "发言人识别", "Automatically identifies who said what"),
         ("CRM Integration", "CRM集成", "Push summaries to Salesforce, HubSpot"),
         ("Multi-platform", "多平台支持", "Works with Zoom, Meet, Teams")],
        [("Free","$0","5 meetings/mo, basic transcription","每月5次会议，基础转录"),
         ("Pro","$12/mo","Unlimited meetings, AI summaries","无限会议，AI摘要"),
         ("Business","$20/mo","Team features, CRM integration","团队功能，CRM集成")],
        [("Extremely accurate transcription","极其准确的转录"),
         ("Highlight clips great for sharing","精彩片段非常适合分享"),
         ("Generous free tier for personal use","个人使用的免费版非常慷慨"),
         ("Integrates with major meeting platforms","与主流会议平台集成")],
        [("Free tier limited to 5 meetings/month","免费版每月仅限5次会议"),
         ("Browser-based only — no native desktop app","仅支持浏览器——无原生桌面应用"),
         ("Some languages lower accuracy","部分语言准确度较低")],
        "Remote teams, sales teams, consultants, and anyone who needs to document and share meeting outcomes.",
        "远程团队、销售团队、顾问，以及任何需要记录和分享会议结果的人。",
        ["Feature","tl;dv","Otter.ai","Fireflies.ai"],
        [["AI summaries","✅","✅","✅"],["Video highlight clips","✅","❌","✅"],["Free tier","5 meetings/mo","300 min/mo","800 min storage"],["CRM integration","✅","❌","✅"],["Price (Pro)","$12/mo","$17/mo","$10/mo"]],
        ["功能","tl;dv","Otter.ai","Fireflies.ai"],
        "**Rating: 4.3/5**\n\ntl;dv is the best value meeting recorder. At $12/mo, it offers AI summaries, transcription, and highlight clips.",
        "**评分：4.3/5**\n\ntl;dv是性价比最高的会议录制工具。每月$12即可获得AI摘要、转录和精彩片段。")

    add("attio", "Attio", "Attio",
        "AI-native CRM for modern teams with intelligent automation, relationship intelligence, and seamless workflows.",
        "面向现代团队的AI原生CRM，具备智能自动化、关系智能和无缝工作流。",
        ["productivity"], ["Attio","CRM","productivity","sales"],
        "https://attio.com", "Attio", "2019", "Free; Starter $49/seat/mo; Growth $79/seat/mo",
        ["productivity"], "https://logo.clearbit.com/attio.com",
        "**Attio** is an AI-native CRM designed for modern, fast-moving teams. It combines intelligent automation with relationship intelligence.",
        "**Attio** 是一款专为现代快速团队设计的AI原生CRM。它将智能自动化与关系智能相结合。",
        [("AI-Powered Data Entry", "AI数据录入", "Automatically enriches contact and company data"),
         ("Smart Workflows", "智能工作流", "AI-triggered automation based on deal stages"),
         ("Relationship Mapping", "关系图谱", "Visual maps of connections between contacts"),
         ("Flexible Data Model", "灵活数据模型", "Custom fields and views without rigid schemas"),
         ("Real-time Sync", "实时同步", "Integrates with Gmail, Slack, calendar"),
         ("AI Activity Summaries", "AI活动摘要", "Auto-generates summaries of interactions")],
        [("Free","$0","Basic CRM, 1 user","基础CRM，1个用户"),
         ("Starter","$49/seat/mo","AI automation, integrations","AI自动化，集成"),
         ("Growth","$79/seat/mo","Advanced AI, team features","高级AI，团队功能")],
        [("Beautiful modern interface teams enjoy","美观现代的界面，团队喜欢使用"),
         ("AI automation saves hours on data entry","AI自动化节省大量数据录入时间"),
         ("Flexible enough for any workflow","足够灵活适应任何工作流"),
         ("Strong integrations ecosystem","强大的集成生态系统")],
        [("Relatively new — less established than Salesforce","相对较新——不如Salesforce成熟"),
         ("Per-seat pricing adds up for larger teams","按席位计费，大团队成本较高"),
         ("Limited reporting vs enterprise CRMs","与大型CRM相比报告功能有限")],
        "Startups, SMBs, and modern teams wanting a flexible, AI-powered CRM without legacy system complexity.",
        "希望拥有灵活AI驱动CRM而无需传统系统复杂性的初创公司和中小企业。",
        ["Feature","Attio","HubSpot","Salesforce"],
        [["AI automation","✅","Partial","✅"],["Modern UX","✅","✅","❌"],["Setup time","<30 min","~1 hour","Days"],["Price (entry)","Free","Free","$25/user/mo"],["Custom fields","✅","✅","✅"]],
        ["功能","Attio","HubSpot","Salesforce"],
        "**Rating: 4.4/5**\n\nAttio is the CRM for teams that hate CRMs. Its AI automation and modern design make it ideal for startups and SMBs.",
        "**评分：4.4/5**\n\nAttio是给讨厌CRM的团队使用的CRM。AI自动化和现代设计使其成为初创公司理想选择。")

    add("linear", "Linear", "Linear",
        "AI-enhanced project management tool for software teams with smart issue tracking, automation, and roadmaps.",
        "面向软件团队的AI增强项目管理工具，智能问题跟踪、自动化和路线图规划。",
        ["productivity","coding"], ["Linear","project-management","productivity","agile"],
        "https://linear.app", "Linear", "2019", "Free; Standard $8/seat/mo; Plus $14/seat/mo",
        ["productivity"], "https://logo.clearbit.com/linear.app",
        "**Linear** is an AI-enhanced project management tool built for software teams. It combines beautiful design with intelligent automation to streamline issue tracking and roadmapping.",
        "**Linear** 是一款专为软件团队打造的AI增强项目管理工具。美观设计配合智能自动化，简化问题跟踪和路线图。",
        [("AI Issue Triage", "AI问题分类", "Auto-categorizes and assigns issues based on context"),
         ("Smart Keyboard Shortcuts", "智能快捷键", "Full keyboard-driven workflow"),
         ("Real-time Sync", "实时同步", "Instant updates across the entire team"),
         ("Cycles & Roadmaps", "周期与路线图", "Visual planning with drag-and-drop"),
         ("Git Integration", "Git集成", "Auto-link PRs to issues, status updates on merge"),
         ("AI Drafts", "AI草稿", "Generate issue descriptions from prompts")],
        [("Free","$0","Up to 10 users, basic features","最多10个用户，基础功能"),
         ("Standard","$8/seat/mo","Unlimited, advanced features","无限用户，高级功能"),
         ("Plus","$14/seat/mo","Priority support, admin features","优先支持，管理功能")],
        [("Blazing fast — fastest PM tool available","极快——速度最快的项目管理工具"),
         ("Beautiful, minimal design reduces clutter","美观简约的设计减少杂乱"),
         ("Excellent Git/GitHub/GitLab integration","出色的Git集成"),
         ("AI triage saves PMs significant time","AI分类节省项目经理大量时间")],
        [("Best for software teams — not ideal for non-tech","最适合软件团队——不适合非技术项目"),
         ("Learning curve for teams used to Jira","习惯Jira的团队有学习曲线"),
         ("No built-in time tracking","没有内置时间追踪")],
        "Software engineering teams, product teams, and startups wanting a fast, modern Jira alternative.",
        "希望拥有Jira快速现代替代方案的软件工程团队和初创公司。",
        ["Feature","Linear","Jira","Asana"],
        [["Speed","⚡ Extremely fast","Slow","Medium"],["AI triage","✅","❌","❌"],["Git integration","✅","✅","❌"],["Free tier","✅ (10 users)","✅ (10 users)","✅ (10 users)"],["Price","$8/seat/mo","$8/seat/mo","$11/user/mo"]],
        ["功能","Linear","Jira","Asana"],
        "**Rating: 4.6/5**\n\nLinear is the best project management tool for software teams. Fast, beautiful, and its AI features genuinely save time.",
        "**评分：4.6/5**\n\nLinear是软件团队最佳的项目管理工具。快速、美观，AI功能确实能节省时间。")

    add("ashby", "Ashby", "Ashby",
        "AI-powered recruitment and ATS platform for modern hiring teams with intelligent sourcing and automation.",
        "面向现代招聘团队的AI驱动ATS和招聘平台，具备智能寻源和自动化。",
        ["productivity"], ["Ashby","recruitment","ATS","hiring"],
        "https://ashbyhq.com", "Ashby", "2018", "Custom (contact for pricing)",
        ["productivity"], "https://logo.clearbit.com/ashbyhq.com",
        "**Ashby** is an AI-powered ATS and recruitment platform. It combines intelligent sourcing, automation, and analytics to streamline hiring.",
        "**Ashby** 是一款AI驱动的ATS和招聘平台。结合智能寻源、自动化和分析简化招聘。",
        [("AI Sourcing", "AI寻源", "Finds and ranks candidates from multiple sources"),
         ("Smart Outreach", "智能触达", "AI-generated personalized outreach messages"),
         ("Pipeline Analytics", "流程分析", "Real-time hiring funnel analytics"),
         ("Structured Interviews", "结构化面试", "AI-assisted interview scorecards"),
         ("Calendar Integration", "日历集成", "Seamless scheduling with Google/Outlook"),
         ("Custom Workflows", "自定义工作流", "Fully customizable hiring stages")],
        [("Starter","Custom","Core ATS, basic analytics","核心ATS，基础分析"),
         ("Pro","Custom","AI sourcing, advanced analytics","AI寻源，高级分析"),
         ("Enterprise","Custom","Full suite, dedicated support","完整套件，专属支持")],
        [("Beautiful interface candidates and recruiters love","美观的界面受候选人和招聘者喜爱"),
         ("Powerful AI sourcing reduces time-to-hire","强大的AI寻源缩短招聘周期"),
         ("Excellent analytics and reporting","出色的分析和报告"),
         ("Highly customizable workflows","高度可定制工作流")],
        [("Custom pricing — no self-serve plans","定制定价——没有自助计划"),
         ("Better for mid-market than enterprise","更适合中型市场而非企业级"),
         ("Smaller integration ecosystem","集成生态系统较小")],
        "Growing companies and mid-market teams wanting a modern AI-powered ATS without enterprise complexity.",
        "希望拥有现代化AI驱动ATS而无需企业级复杂性的成长型公司和中等市场团队。",
        ["Feature","Ashby","Greenhouse","Lever"],
        [["AI sourcing","✅","Partial","✅"],["Modern UX","✅","✅","✅"],["Self-serve pricing","❌","❌","❌"],["Interview tools","✅","✅","✅"],["Analytics","✅","✅","✅"]],
        ["功能","Ashby","Greenhouse","Lever"],
        "**Rating: 4.3/5**\n\nAshby is the best-looking ATS on the market. Its AI sourcing and modern UX make it ideal for fast-growing companies.",
        "**评分：4.3/5**\n\nAshby是市场上最好看的ATS。AI寻源和现代UX使其成为快速成长公司的理想选择。")

    add("decorwhisk", "DecorWhisk", "DecorWhisk",
        "AI interior design tool that generates room redesigns, furniture suggestions, and style visualizations from photos.",
        "AI室内设计工具，从照片生成房间重新设计、家具建议和风格可视化。",
        ["productivity","image"], ["DecorWhisk","interior-design","AI","home"],
        "https://decorwhisk.com", "DecorWhisk", "2023", "Free credits; Pro $19/mo",
        ["productivity"], "https://logo.clearbit.com/decorwhisk.com",
        "**DecorWhisk** lets you upload photos of any room and get instant redesign suggestions with furniture, colors, and decor recommendations.",
        "**DecorWhisk** 让您上传任何房间的照片，即可获得即时重新设计建议，包括家具、颜色和装饰推荐。",
        [("Room Redesign", "房间重新设计", "AI-generated room makeovers from photos"),
         ("Style Transfer", "风格转换", "Apply different interior design styles"),
         ("Furniture Suggestions", "家具建议", "AI recommends furniture for your space"),
         ("Color Palette", "配色方案", "Generates complementary color schemes"),
         ("Budget Estimation", "预算估算", "Rough cost estimates for designs"),
         ("Multiple Rooms", "多种房间", "Kitchen, bedroom, living room, bathroom, office")],
        [("Free","$0","Limited generations/month","每月有限的生成次数"),
         ("Pro","$19/mo","Unlimited, HD exports","无限生成，高清导出")],
        [("See room changes before spending money","在花钱之前先看到房间变化"),
         ("Multiple design styles to explore","可探索多种设计风格"),
         ("Easy to use — just upload a photo","简单易用——只需上传照片"),
         ("Helpful for budget planning","有助于预算规划")],
        [("Designs can be unrealistic","设计可能不现实"),
         ("Limited to visual suggestions","仅限视觉建议"),
         ("Furniture may not be available in your region","家具可能在您所在地区不可用")],
        "Homeowners planning renovations, interior designers seeking inspiration, and real estate agents staging properties.",
        "计划装修的房主、寻求灵感的室内设计师，以及进行房屋布置的房地产经纪人。",
        ["Feature","DecorWhisk","Remodeled.ai","RoomGPT"],
        [["AI room redesign","✅","✅","✅"],["Furniture suggestions","✅","✅","❌"],["Budget estimation","✅","❌","❌"],["Multiple styles","✅","✅","✅"],["Price (Pro)","$19/mo","$29/mo","$9/mo"]],
        ["功能","DecorWhisk","Remodeled.ai","RoomGPT"],
        "**Rating: 4.0/5**\n\nDecorWhisk is fun and practical for visualizing room changes. Great for brainstorming before expensive renovations.",
        "**评分：4.0/5**\n\nDecorWhisk是一个有趣且实用的工具，用于可视化房间变化。投入昂贵装修前头脑风暴很棒。")

    # --- AI Coding ---
    add("v0", "v0", "v0",
        "AI-powered UI code generator by Vercel that creates production-ready React components from text prompts and screenshots.",
        "Vercel出品的AI驱动UI代码生成器，从文本提示和截图创建生产级React组件。",
        ["coding"], ["v0","Vercel","React","UI","coding"],
        "https://v0.dev", "Vercel", "2023", "Free (10 gen/mo); Premium $20/mo",
        ["coding"], "https://logo.clearbit.com/vercel.com",
        "**v0** by Vercel creates production-ready React/Next.js components from text descriptions and uploaded screenshots using AI models.",
        "**v0** 由Vercel开发，使用AI模型从文本描述和上传的截图创建生产级React/Next.js组件。",
        [("Text-to-UI", "文本转UI", "Generate components from natural language"),
         ("Screenshot-to-Code", "截图转代码", "Upload screenshot, get matching code"),
         ("Production-Ready", "生产就绪", "Clean React + Tailwind CSS output"),
         ("Iterative Refinement", "迭代优化", "Chat with AI to refine components"),
         ("Component Library", "组件库", "Access generated components in library"),
         ("One-Click Deploy", "一键部署", "Deploy to Vercel instantly")],
        [("Free","$0","10 generations/mo","每月10次生成"),
         ("Premium","$20/mo","Unlimited, priority access","无限生成，优先访问")],
        [("Incredibly fast UI prototyping","极其快速的UI原型设计"),
         ("Code quality surprisingly high","代码质量出人意料地高"),
         ("Perfect for React/Next.js developers","非常适合React/Next.js开发者"),
         ("Screenshot-to-code is magical","截图转代码功能非常神奇")],
        [("Limited to React/Next.js ecosystem","仅限于React/Next.js"),
         ("Complex layouts may need manual refinement","复杂布局可能需手动调整"),
         ("Free tier runs out quickly","免费额度很快用完")],
        "React developers, front-end engineers, and designers wanting to rapidly prototype UI components.",
        "希望快速原型设计UI组件的React开发者、前端工程师和设计师。",
        ["Feature","v0","Cursor","Bolt"],
        [["UI specialization","✅","❌","✅"],["Screenshot-to-code","✅","❌","❌"],["React/Tailwind","✅","✅","✅"],["Full app generation","❌","✅","✅"],["Price","$0-$20/mo","$20/mo","$0-$20/mo"]],
        ["功能","v0","Cursor","Bolt"],
        "**Rating: 4.5/5**\n\nv0 is the best AI tool for generating UI components. If you work with React, it's an absolute must-have.",
        "**评分：4.5/5**\n\nv0是生成UI组件的最佳AI工具。如果您使用React，它是绝对必备的。")

    add("bolt-new", "Bolt", "Bolt",
        "AI full-stack development tool by StackBlitz that generates, runs, and deploys complete web applications from prompts.",
        "StackBlitz出品的AI全栈开发工具，从提示生成、运行和部署完整Web应用。",
        ["coding"], ["Bolt","StackBlitz","full-stack","coding"],
        "https://bolt.new", "StackBlitz", "2024", "Free; Pro $20/mo",
        ["coding"], "https://logo.clearbit.com/stackblitz.com",
        "**Bolt** by StackBlitz lets you prompt, run, edit, and deploy full-stack web applications entirely in your browser.",
        "**Bolt** 由StackBlitz开发，让您完全在浏览器中通过提示、运行、编辑和部署全栈Web应用。",
        [("Full-Stack Generation", "全栈生成", "Complete web apps with frontend + backend"),
         ("In-Browser Runtime", "浏览器运行时", "Run Node.js directly in browser"),
         ("AI Code Editor", "AI代码编辑器", "Chat with AI to modify generated code"),
         ("Instant Preview", "即时预览", "See changes in real-time"),
         ("NPM Ecosystem", "NPM生态", "Access thousands of npm packages"),
         ("One-Click Deploy", "一键部署", "Deploy to production with one click")],
        [("Free","$0","Limited generations","有限的生成次数"),
         ("Pro","$20/mo","Unlimited, faster performance","无限生成，更快性能")],
        [("Go from idea to deployed app in minutes","几分钟内从想法到部署"),
         ("No local dev environment needed","不需要本地开发环境"),
         ("Supports full-stack — not just frontend","支持全栈——不仅是前端"),
         ("Great for rapid prototyping and MVPs","非常适合快速原型和MVP")],
        [("Generated code can be messy","生成代码可能较乱"),
         ("Debugging AI code can be frustrating","调试AI代码可能很沮丧"),
         ("Browser limits for large projects","浏览器方式对大型项目有限制")],
        "Developers prototyping ideas, non-technical founders building MVPs, and anyone creating web apps without complex setup.",
        "快速原型设计的开发者、构建MVP的非技术创始人，以及无需复杂设置创建Web应用的人。",
        ["Feature","Bolt","v0","Replit"],
        [["Full-stack","✅","❌","✅"],["In-browser","✅","✅","❌"],["Instant deploy","✅","✅","✅"],["AI chat editing","✅","✅","✅"],["Price","$0-$20/mo","$0-$20/mo","$0-$25/mo"]],
        ["功能","Bolt","v0","Replit"],
        "**Rating: 4.3/5**\n\nBolt is the fastest way from idea to working web app. Perfect for prototyping.",
        "**评分：4.3/5**\n\nBolt是从想法到可用Web应用最快的方式。非常适合原型设计。")

    add("devin", "Devin", "Devin",
        "World's first autonomous AI software engineer by Cognition that can plan, code, debug, and deploy independently.",
        "Cognition出品的全球首个自主AI软件工程师，能独立规划、编码、调试和部署。",
        ["coding"], ["Devin","Cognition","AI-engineer","coding"],
        "https://devin.ai", "Cognition Labs", "2023", "Custom (contact sales)",
        ["coding"], "https://logo.clearbit.com/cognition.ai",
        "**Devin** by Cognition Labs is the world's first autonomous AI software engineer. It independently plans, writes, debugs, and deploys code.",
        "**Devin** 由Cognition Labs开发，是世界首个自主AI软件工程师。独立规划、编写、调试和部署代码。",
        [("Autonomous Coding", "自主编码", "Plans and executes coding tasks independently"),
         ("Full Dev Environment", "完整开发环境", "Own shell, browser, and editor"),
         ("Bug Fixing", "Bug修复", "Reads logs, diagnoses issues, implements fixes"),
         ("Multi-Step Reasoning", "多步推理", "Breaks complex tasks into sub-tasks"),
         ("GitHub Integration", "GitHub集成", "Creates PRs, reviews code, manages repos"),
         ("Real-time Progress", "实时进度", "Watch Devin work step by step")],
        [("Limited Access","Custom","Early access, limited capacity","早期访问，有限容量"),
         ("Enterprise","Custom","Full access, priority support","完整访问，优先支持")],
        [("Truly autonomous — handles entire tasks","真正的自主——处理整个任务"),
         ("Works on real codebases with real tools","能在真实代码库上工作"),
         ("Fascinating to watch it work","观看它工作令人着迷"),
         ("Dramatic productivity potential","巨大的生产力潜力")],
        [("Very expensive — enterprise only","价格昂贵——仅限企业"),
         ("Struggles with ambiguous tasks","模糊任务可能困难"),
         ("Still early — reliability varies","仍处于早期——可靠性不稳定"),
         ("Not replacement for senior engineers","不能替代资深工程师")],
        "Enterprise engineering teams wanting to automate routine development tasks.",
        "希望自动化常规开发任务的企业工程团队。",
        ["Feature","Devin","Cursor","GitHub Copilot"],
        [["Autonomous","✅","❌","❌"],["Full dev env","✅","✅","✅"],["Multi-task","✅","✅","Single task"],["Price","Enterprise","$20/mo","$10-$39/mo"],["Maturity","Early","Mature","Mature"]],
        ["功能","Devin","Cursor","GitHub Copilot"],
        "**Rating: 3.8/5**\n\nDevin is groundbreaking as first autonomous AI engineer, but still early and expensive. Worth watching.",
        "**评分：3.8/5**\n\nDevin作为首个自主AI工程师具有开创性，但仍在早期且价格昂贵。值得密切关注。")

    add("augment-code", "Augment Code", "Augment Code",
        "AI coding assistant that understands your entire codebase for intelligent code suggestions and explanations.",
        "AI编程助手，理解您的整个代码库以提供智能代码建议和解释。",
        ["coding"], ["Augment Code","coding","AI","assistant"],
        "https://www.augmentcode.com", "Augment Code", "2023", "Free; Pro $25/mo",
        ["coding"], "https://logo.clearbit.com/augmentcode.com",
        "**Augment Code** goes beyond autocomplete. It understands your entire codebase, team patterns, and coding standards.",
        "**Augment Code** 超越简单自动补全。理解您的整个代码库、团队模式和编码标准。",
        [("Codebase Understanding", "代码库理解", "Indexes entire project for context"),
         ("Intelligent Autocomplete", "智能自动补全", "Context-aware code completion"),
         ("Code Explanations", "代码解释", "Explains complex code in natural language"),
         ("Bug Detection", "Bug检测", "Identifies bugs and suggests fixes"),
         ("Multi-file Editing", "多文件编辑", "Changes across multiple files at once"),
         ("Team Learning", "团队学习", "Adapts to team patterns over time")],
        [("Free","$0","Basic autocomplete, limited queries","基础自动补全，有限查询"),
         ("Pro","$25/mo","Full codebase understanding","完整代码库理解")],
        [("Deep codebase understanding sets it apart","深度的代码库理解使其与众不同"),
         ("Learns team coding patterns","随时间学习团队编码模式"),
         ("Multi-file editing is powerful","多文件编辑功能强大"),
         ("Excellent for large codebases","非常适合大型代码库")],
        [("Relatively new to the market","市场相对较新"),
         ("Pro plan pricier than competitors","Pro版比竞品更贵"),
         ("IDE support still expanding","IDE支持仍在扩展")],
        "Developers on large codebases needing AI that understands their entire project context.",
        "在大型代码库上工作、需要理解整个项目上下文的AI的开发者。",
        ["Feature","Augment Code","Cursor","GitHub Copilot"],
        [["Codebase awareness","Full","Full","Partial"],["Multi-file edits","✅","✅","❌"],["IDE support","VS Code, JetBrains","VS Code only","Multiple"],["Price","$0-$25/mo","$20/mo","$10-$39/mo"],["Team learning","✅","❌","❌"]],
        ["功能","Augment Code","Cursor","GitHub Copilot"],
        "**Rating: 4.2/5**\n\nAugment Code excels at understanding large codebases. Strong choice for complex projects.",
        "**评分：4.2/5**\n\nAugment Code在理解大型代码库方面表现出色。是在复杂项目上的有力选择。")

    add("coderabbit", "CodeRabbit", "CodeRabbit",
        "AI code review tool providing instant, detailed PR reviews with actionable feedback for development teams.",
        "AI代码审查工具，为开发团队提供即时详细的PR审查和可操作反馈。",
        ["coding"], ["CodeRabbit","code-review","AI","PR"],
        "https://coderabbit.ai", "CodeRabbit", "2023", "Free; Pro $12/mo; Team $24/user/mo",
        ["coding"], "https://logo.clearbit.com/coderabbit.ai",
        "**CodeRabbit** automatically reviews pull requests with detailed, actionable feedback. Integrates with GitHub, GitLab, and Bitbucket.",
        "**CodeRabbit** 自动审查Pull Request并提供详细可操作反馈。与GitHub、GitLab和Bitbucket集成。",
        [("Auto PR Reviews", "自动PR审查", "Detailed line-by-line feedback on every PR"),
         ("Security Scanning", "安全扫描", "Detects vulnerabilities and suggests fixes"),
         ("Performance Insights", "性能洞察", "Identifies performance bottlenecks"),
         ("PR Summaries", "PR摘要", "Auto-generates PR descriptions and changelogs"),
         ("Multi-language", "多语言", "Supports 30+ programming languages"),
         ("Chat", "聊天", "Ask questions about code in PR comments")],
        [("Free","$0","Open source, limited reviews","开源项目，有限审查"),
         ("Pro","$12/mo","Unlimited reviews, full features","无限审查，完整功能"),
         ("Team","$24/user/mo","Team analytics, admin controls","团队分析，管理控制")],
        [("Catches bugs humans miss","捕获人工遗漏的bug"),
         ("Extremely fast — reviews in seconds","极快——几秒内完成审查"),
         ("Detailed, actionable feedback","详细可操作的反馈"),
         ("Excellent GitHub/GitLab integration","出色的GitHub/GitLab集成")],
        [("Can have false positives","可能有误报"),
         ("Less useful for domain-specific code","特定领域代码不太适用"),
         ("Team plan pricing adds up","团队版定价较高")],
        "Development teams wanting faster, more thorough code reviews — especially with limited senior reviewers.",
        "希望获得更快更彻底代码审查的团队——特别是资深审查人员有限的情况。",
        ["Feature","CodeRabbit","GitHub Copilot","Bito"],
        [["Auto PR review","✅","❌","✅"],["Security scanning","✅","✅","❌"],["PR summaries","✅","❌","✅"],["Line-by-line feedback","✅","✅","✅"],["Price (Pro)","$12/mo","$10/mo","$10/mo"]],
        ["功能","CodeRabbit","GitHub Copilot","Bito"],
        "**Rating: 4.4/5**\n\nCodeRabbit is the best AI code review tool. Catches real issues and saves senior developers significant review time.",
        "**评分：4.4/5**\n\nCodeRabbit是目前最好的AI代码审查工具。能发现真实问题，为资深开发者节省大量时间。")

    add("sweep", "Sweep", "Sweep",
        "AI junior developer that creates PRs for bug fixes, features, and refactors directly from GitHub issues.",
        "AI初级开发者，直接从GitHub Issues创建Bug修复、功能和重构的PR。",
        ["coding"], ["Sweep","AI","coding","GitHub"],
        "https://sweep.dev", "Sweep AI", "2023", "Free; Pro $20/mo",
        ["coding"], "https://logo.clearbit.com/sweep.dev",
        "**Sweep** turns GitHub issues into pull requests. Give it a task — it plans, writes, tests, and creates a PR automatically.",
        "**Sweep** 将GitHub Issues转换为Pull Requests。给它一个任务，它会自动规划、编写、测试并创建PR。",
        [("Issue-to-PR", "Issue转PR", "Creates PRs directly from GitHub issues"),
         ("Multi-file Changes", "多文件更改", "Coherent changes across many files"),
         ("Test Generation", "测试生成", "Writes unit tests for changes"),
         ("Plan & Execute", "规划与执行", "Breaks tasks into steps, executes"),
         ("Context Awareness", "上下文感知", "Reads relevant files before coding"),
         ("GitHub Native", "GitHub原生", "Works natively with GitHub repos")],
        [("Free","$0","Open source, 1 repo","开源项目，1个仓库"),
         ("Pro","$20/mo","Unlimited repos, priority","无限仓库，优先")],
        [("Automates routine coding tasks effectively","有效自动化常规编码任务"),
         ("Understands codebase context","理解代码库上下文"),
         ("Great for boilerplate and simple features","适合样板代码和简单功能"),
         ("Saves time on repetitive tasks","在重复任务上节省时间")],
        [("Quality varies — needs human review","质量不稳定——需人工审查"),
         ("Struggles with architectural changes","复杂架构变更表现不佳"),
         ("GitHub only — no GitLab/Bitbucket","仅支持GitHub")],
        "Developers wanting to automate routine coding tasks and turn GitHub issues into pull requests.",
        "希望自动化常规编码任务并将GitHub Issues转化为PR的开发者。",
        ["Feature","Sweep","Devin","Cursor"],
        [["Issue-to-PR","✅","❌","❌"],["Autonomous","Semi","Fully","Assisted"],["GitHub native","✅","✅","✅"],["Price","$0-$20/mo","Enterprise","$20/mo"],["Best for","Routine","Complex","Interactive"]],
        ["功能","Sweep","Devin","Cursor"],
        "**Rating: 3.9/5**\n\nSweep is handy for automating routine coding tasks. Not as capable as Devin but much more accessible.",
        "**评分：3.9/5**\n\nSweep对于自动化常规编码任务很实用。不如Devin强大，但对个人开发者更容易获取。")

    # --- AI Image/Design ---
    add("designify", "Designify", "Designify",
        "AI product photo editor creating professional product images, mockups, and lifestyle shots automatically.",
        "AI产品照片编辑器，自动创建专业产品图片、模型图和生活方式照片。",
        ["image"], ["Designify","product-photo","AI","e-commerce"],
        "https://www.designify.com", "Designify", "2021", "Free trial; Pro $29/mo; Pay-as-you-go",
        ["image"], "https://logo.clearbit.com/designify.com",
        "**Designify** transforms ordinary product photos into professional-grade images with AI backgrounds, mockups, and lifestyle scenes.",
        "**Designify** 用AI背景、模型图和生活方式场景将普通产品照片转化为专业级图像。",
        [("Background Removal", "背景去除", "AI automatic background removal"),
         ("Mockup Generation", "模型生成", "Products in realistic scene mockups"),
         ("Shadow & Reflection", "阴影和反射", "Adds realistic shadows and reflections"),
         ("Batch Processing", "批量处理", "Edit hundreds of images at once"),
         ("Color Correction", "色彩校正", "AI-enhanced color and lighting"),
         ("Template Library", "模板库", "Thousands of pre-built mockup templates")],
        [("Free Trial","$0","3 free designs","3个免费设计"),
         ("Pro","$29/mo","Unlimited, priority rendering","无限设计，优先渲染"),
         ("Pay-as-you-go","$1.90/design","No subscription","按需付费")],
        [("Stunning product photos in seconds","几秒内获得惊艳产品照片"),
         ("Huge mockup template library","巨大模型模板库"),
         ("Batch processing saves massive time","批量处理节省大量时间"),
         ("Pay-as-you-go is flexible","按需付费很灵活")],
        [("Pro plan expensive for occasional users","偶尔使用Pro版较贵"),
         ("Some mockups look AI-generated","一些模型看起来AI生成"),
         ("Limited customization for advanced users","高级自定义功能有限")],
        "E-commerce sellers and marketers needing professional product photos without expensive shoots.",
        "需要专业产品照片但不想花钱拍摄的电商卖家和营销人员。",
        ["Feature","Designify","Photoroom","Canva"],
        [["Product mockups","✅","✅","Partial"],["Batch processing","✅","✅","❌"],["Background removal","✅","✅","✅"],["Lifestyle scenes","✅","✅","❌"],["Price","$1.90+/design","$13/mo","$13/mo"]],
        ["功能","Designify","Photoroom","Canva"],
        "**Rating: 4.1/5**\n\nDesignify is the best for professional product mockups. Pay-as-you-go pricing great for occasional use.",
        "**评分：4.1/5**\n\nDesignify是创建专业产品模型的最佳工具。按需付费非常适合偶尔使用。")

    add("uizard", "Uizard", "Uizard",
        "AI UI design tool transforming hand-drawn sketches, screenshots, and text into professional UI designs.",
        "AI UI设计工具，将手绘草图、截图和文本转换为专业的UI设计。",
        ["image"], ["Uizard","UI-design","prototype","AI"],
        "https://uizard.io", "Uizard", "2018", "Free; Pro $19/mo; Business $39/mo",
        ["image"], "https://logo.clearbit.com/uizard.io",
        "**Uizard** creates professional app and website designs from hand-drawn sketches, screenshots, or text prompts. No design skills required.",
        "**Uizard** 从手绘草图、截图或文本提示创建专业的应用和网站设计。无需设计技能。",
        [("Sketch-to-UI", "草图转UI", "Convert wireframes into digital designs"),
         ("Screenshot-to-Design", "截图转设计", "Transform screenshots into editable UI"),
         ("AI Theme Generation", "AI主题生成", "Generate complete design themes from text"),
         ("Prototyping", "原型设计", "Clickable prototypes with interactivity"),
         ("Component Library", "组件库", "Thousands of pre-built UI components"),
         ("Collaboration", "协作", "Real-time team editing and commenting")],
        [("Free","$0","3 projects, basic","3个项目，基础"),
         ("Pro","$19/mo","Unlimited, full library","无限项目，完整库"),
         ("Business","$39/mo","Team, custom branding","团队，自定义品牌")],
        [("No design skills needed","无需设计技能"),
         ("Sketch-to-UI incredibly useful","草图转UI非常有用"),
         ("Rapid prototyping saves weeks","快速原型设计节省数周"),
         ("More affordable than Figma","比Figma更实惠")],
        [("Designs can look generic","设计可能看起来普通"),
         ("Not as powerful as Figma","不如Figma强大"),
         ("Free tier very limited","免费版非常有限")],
        "Founders, product managers, and non-designers needing professional UI mockups quickly.",
        "需要快速创建专业UI模型的创始人、产品经理和非设计人员。",
        ["Feature","Uizard","v0","Figma"],
        [["Sketch-to-UI","✅","❌","❌"],["Screenshot-to-design","✅","✅","❌"],["Prototyping","✅","❌","✅"],["No code required","✅","✅","❌"],["Price","$0-$39/mo","$0-$20/mo","Free-$15/mo"]],
        ["功能","Uizard","v0","Figma"],
        "**Rating: 4.2/5**\n\nUizard democratizes UI design. Best choice for non-designers needing professional interfaces quickly.",
        "**评分：4.2/5**\n\nUizard让UI设计民主化。需要快速获得专业界面的非设计人员的最佳选择。")

    add("looka", "Looka", "Looka",
        "AI logo and brand identity generator creating professional logos, brand kits, and business cards in minutes.",
        "AI标志和品牌标识生成器，几分钟内创建专业标志、品牌套件和名片。",
        ["image"], ["Looka","logo","brand","AI"],
        "https://looka.com", "Looka", "2016", "One-time $20+ for logo; Brand Kit $96",
        ["image"], "https://logo.clearbit.com/looka.com",
        "**Looka** generates professional logos, complete brand kits, and marketing materials in minutes using machine learning.",
        "**Looka** 使用机器学习几分钟内生成专业标志、完整品牌套件和营销材料。",
        [("AI Logo Generation", "AI标志生成", "Dozens of logo options from preferences"),
         ("Brand Kit", "品牌套件", "Complete brand package with colors, fonts"),
         ("Business Cards", "名片", "Design matching business cards"),
         ("Social Media Kits", "社交媒体套件", "Profile images and cover photos"),
         ("Templates", "模板", "Flyers, posters, email signatures"),
         ("Customization", "自定义", "Fine-tune colors, fonts, layout")],
        [("Logo Only","$20 一次性","1 logo, basic formats","1个标志，基础格式"),
         ("Logo + Brand Kit","$96 一次性","Full brand package","完整品牌包"),
         ("Enterprise","Custom","Multiple concepts","多个方案")],
        [("Professional results in minutes","几分钟内获得专业结果"),
         ("No design skills needed","无需设计技能"),
         ("One-time payment — no subscription","一次性付费——无需订阅"),
         ("Complete brand kit in one purchase","一次购买获得完整品牌套件")],
        [("Logos can look similar in same industry","同行业标志可能相似"),
         ("Limited to logo/branding","仅限于标志/品牌"),
         ("No vector source files on basic plan","基础计划无矢量源文件")],
        "Startups and small businesses needing professional branding quickly and affordably.",
        "需要快速且实惠获得专业品牌的初创公司和小企业。",
        ["Feature","Looka","Canva","Hatchful"],
        [["AI generation","✅","❌","✅"],["Brand kit","✅","❌","❌"],["Customization","✅","✅","Limited"],["Price","$20+","$13/mo","Free"],["Quality","High","High","Low"]],
        ["功能","Looka","Canva","Hatchful"],
        "**Rating: 4.1/5**\n\nLooka is fastest way to get a professional logo and brand kit. One-time pricing great for startups.",
        "**评分：4.1/5**\n\nLooka是获得专业标志和品牌套件最快的方式。一次性定价对初创公司很棒。")

    add("khroma", "Khroma", "Khroma",
        "AI color palette generator that learns your preferences to create personalized color combinations.",
        "AI配色方案生成器，学习您的偏好创建个性化色彩组合。",
        ["image"], ["Khroma","color","palette","design"],
        "https://www.khroma.co", "George Hastings", "2018", "Free",
        ["image"], "https://logo.clearbit.com/khroma.co",
        "**Khroma** uses machine learning to understand your color preferences and generate palettes, gradients, and typography combinations you'll love.",
        "**Khroma** 使用机器学习理解您的颜色偏好，生成您喜欢的调色板、渐变和字体组合。",
        [("Personalized Palettes", "个性化调色板", "Trains on preferences for colors you'll like"),
         ("Infinite Combinations", "无限组合", "Generate endless color combinations"),
         ("Multiple Formats", "多种格式", "Palettes, gradients, typography views"),
         ("Accessibility Check", "无障碍检查", "Shows contrast ratios for accessibility"),
         ("Color Codes", "颜色代码", "Copy HEX, RGB, HSL, CSS values"),
         ("Favorites", "收藏夹", "Save and organize favorites")],
        [("Free","$0","Unlimited palette generation","无限调色板生成")],
        [("Genuinely learns your taste","真正学习您的品味"),
         ("Completely free to use","完全免费"),
         ("Beautiful, well-curated combinations","美丽精选的组合"),
         ("Accessibility-aware","关注无障碍性")],
        [("Requires initial training (50 colors)","需要初始训练"),
         ("Web-only — no mobile app","仅限网页"),
         ("Limited to color only","仅限于颜色")],
        "Designers, developers, and anyone struggling with choosing the right colors.",
        "在项目配色上遇到困难的设计师和开发者。",
        ["Feature","Khroma","Coolors","Adobe Color"],
        [["AI personalization","✅","❌","❌"],["Accessibility check","✅","✅","✅"],["Price","Free","Free","Free"],["Gradient support","✅","✅","✅"],["Typography combos","✅","❌","❌"]],
        ["功能","Khroma","Coolors","Adobe Color"],
        "**Rating: 4.5/5**\n\nKhroma is the best AI color tool — it learns what you like. Free and endlessly useful.",
        "**评分：4.5/5**\n\nKhroma是最佳AI配色工具——它学习您喜欢什么。免费且无限有用。")

    # --- AI Video ---
    add("pixverse", "PixVerse", "PixVerse",
        "AI video generation platform creating high-quality videos from text prompts and images with multiple styles.",
        "AI视频生成平台，从文本提示和图像创建高质量视频，支持多种艺术风格。",
        ["video"], ["PixVerse","video-generation","AI","creative"],
        "https://pixverse.ai", "PixVerse AI", "2023", "Free; Pro $9.99/mo",
        ["video"], "https://logo.clearbit.com/pixverse.ai",
        "**PixVerse** creates high-quality videos from text prompts and images with multiple artistic styles and cinematic results.",
        "**PixVerse** 从文本提示和图像创建高质量视频，支持多种艺术风格和电影级效果。",
        [("Text-to-Video", "文本转视频", "Generate videos from text descriptions"),
         ("Image-to-Video", "图像转视频", "Animate still images into video"),
         ("Multiple Styles", "多种风格", "Cinematic, anime, 3D, realistic"),
         ("HD Output", "高清输出", "Up to 1080p resolution"),
         ("Character Consistency", "角色一致性", "Maintain appearance across scenes"),
         ("Fast Generation", "快速生成", "Create videos in seconds")],
        [("Free","$0","~10 videos/day, standard","每天约10个视频，标准"),
         ("Pro","$9.99/mo","Unlimited, HD, priority","无限，高清，优先")],
        [("Impressive video quality","视频质量令人印象深刻"),
         ("Multiple artistic styles","多种艺术风格"),
         ("Fast generation speed","生成速度快"),
         ("Very affordable Pro plan","Pro版价格实惠")],
        [("Video length limited (4-8 seconds)","视频长度有限"),
         ("Character consistency can vary","角色一致性可能不稳定"),
         ("Less control than Runway/Pika","控制能力不如Runway/Pika")],
        "Content creators, marketers, and social media managers needing quick video content.",
        "需要快速视频内容的内容创作者、营销人员和社交媒体经理。",
        ["Feature","PixVerse","Runway","Pika"],
        [["Text-to-video","✅","✅","✅"],["Image-to-video","✅","✅","✅"],["Price (Pro)","$9.99/mo","$15/mo","$8/mo"],["Max resolution","1080p","4K","1080p"],["Video length","4-8s","4-16s","4s"]],
        ["功能","PixVerse","Runway","Pika"],
        "**Rating: 4.0/5**\n\nPixVerse offers great value for AI video. At $9.99/mo, one of the most affordable quality options.",
        "**评分：4.0/5**\n\nPixVerse在AI视频方面性价比出色。每月$9.99是最实惠的质量选择之一。")

    add("captions-app", "Captions", "Captions",
        "AI video editor with automatic captions, eye contact correction, and AI editing tools for content creators.",
        "AI视频编辑器，具备自动字幕、眼神接触修正和AI编辑工具。",
        ["video"], ["Captions","video-editor","subtitles","AI"],
        "https://captions.ai", "Captions AI", "2021", "Free; Pro $9.99/mo; Business $24.99/mo",
        ["video"], "https://logo.clearbit.com/captions.ai",
        "**Captions** is an AI video editor for content creators with auto captions, AI eye contact correction, teleprompter, and creative tools.",
        "**Captions** 是面向内容创作者的AI视频编辑器，具有自动字幕、AI眼神修正、提词器和创意工具。",
        [("Auto Captions", "自动字幕", "Accurate captions in 50+ languages"),
         ("Eye Contact AI", "AI眼神接触", "Simulates looking at camera"),
         ("AI Teleprompter", "AI提词器", "Smart teleprompter adjusting to pace"),
         ("AI Editor", "AI编辑器", "Auto-cuts silences and filler words"),
         ("Background Effects", "背景效果", "Blur, replace, enhance backgrounds"),
         ("Social Formats", "社交格式", "Export for TikTok, Reels, Shorts")],
        [("Free","$0","Basic captions, watermark","基础字幕，有水印"),
         ("Pro","$9.99/mo","No watermark, AI features","无水印，AI功能"),
         ("Business","$24.99/mo","Team, API","团队，API")],
        [("Eye contact AI genuinely impressive","AI眼神接触确实令人印象深刻"),
         ("Extremely easy to use","极其易于使用"),
         ("Captions highly accurate","字幕非常准确"),
         ("Perfect for social media creators","非常适合社交媒体创作者")],
        [("Mobile-first — desktop limited","移动端优先——桌面功能有限"),
         ("Free version includes watermark","免费版有水印"),
         ("Less powerful than Premiere Pro","不如Premiere Pro强大")],
        "Social media creators, YouTubers, TikTokers, and podcasters needing quick professional video.",
        "需要快速制作专业视频的社交媒体创作者和播客主持人。",
        ["Feature","Captions","Descript","CapCut"],
        [["Auto captions","✅","✅","✅"],["Eye contact AI","✅","❌","❌"],["Teleprompter","✅","✅","❌"],["Price (Pro)","$9.99/mo","$24/mo","Free-$8/mo"],["Best for","Social media","Podcasts","Quick edits"]],
        ["功能","Captions","Descript","CapCut"],
        "**Rating: 4.4/5**\n\nCaptions is the best for social media video creation. Eye contact AI and auto captions make it a must-have.",
        "**评分：4.4/5**\n\nCaptions是社交媒体视频创作最佳工具。AI眼神接触和自动字幕使其成为必备。")

    add("opus-clip", "Opus Clip", "Opus Clip",
        "AI tool converting long videos into viral short clips with AI scoring, captions, and social media optimization.",
        "AI工具，将长视频转换为病毒式短视频，具备AI评分和字幕功能。",
        ["video"], ["Opus Clip","short-form","viral","social"],
        "https://www.opus.pro", "Opus Clip", "2023", "Free (1 video); Starter $9.99/mo; Pro $19.99/mo",
        ["video"], "https://logo.clearbit.com/opus.pro",
        "**Opus Clip** uses AI to find engaging moments in long videos and turn them into viral short clips for TikTok, Reels, and Shorts.",
        "**Opus Clip** 使用AI找到长视频中最有吸引力的时刻，转换为病毒式短视频。",
        [("AI Virality Score", "AI病毒性评分", "Scores clips on viral potential"),
         ("Auto Clip Selection", "自动片段选择", "AI identifies most engaging moments"),
         ("Auto Captions", "自动字幕", "Captions with emojis"),
         ("Aspect Ratio", "宽高比", "Auto-crops to 9:16 vertical"),
         ("B-Roll", "B-Roll", "Adds relevant B-roll footage"),
         ("Speaker Detection", "发言人检测", "Identifies and tracks speakers")],
        [("Free","$0","1 video, basic","1个视频，基础"),
         ("Starter","$9.99/mo","200 min/mo processing","每月200分钟"),
         ("Pro","$19.99/mo","Unlimited, B-Roll","无限，B-Roll")],
        [("Saves hours of manual clipping","节省数小时手动剪辑"),
         ("Virality score helps prioritize","病毒性评分帮助优先"),
         ("Professional captions and emojis","专业的字幕和表情符号"),
         ("Great for repurposing podcasts","适合重新利用播客")],
        [("Free tier extremely limited","免费版极其有限"),
         ("AI sometimes picks less interesting moments","AI有时选不太有趣的"),
         ("Quality varies with source video","质量随源视频变化")],
        "Podcasters, live streamers, and creators wanting to repurpose long-form content into viral shorts.",
        "希望将长视频重新制作为病毒式短视频的播客主持人和创作者。",
        ["Feature","Opus Clip","Captions","Veed"],
        [["Auto clipping","✅","❌","❌"],["Virality score","✅","❌","❌"],["Auto captions","✅","✅","✅"],["B-Roll","✅","❌","❌"],["Price (Pro)","$19.99/mo","$9.99/mo","$18/mo"]],
        ["功能","Opus Clip","Captions","Veed"],
        "**Rating: 4.3/5**\n\nOpus Clip is best for repurposing long videos into shorts. Virality scoring is unique and valuable.",
        "**评分：4.3/5**\n\nOpus Clip是将长视频重新制作为短视频的最佳工具。病毒性评分独特且有价值。")

    # --- AI Audio ---
    add("splash-pro", "Splash Pro", "Splash Pro",
        "AI music generation platform creating original songs, beats, and full compositions from text prompts.",
        "AI音乐生成平台，从文本提示创建原创歌曲、节拍和完整作品。",
        ["audio"], ["Splash Pro","music","AI","creation"],
        "https://splashmusic.com", "Splash Music", "2017", "Free; Pro $10/mo",
        ["audio"], "https://logo.clearbit.com/splashmusic.com",
        "**Splash Pro** creates original songs and beats from text descriptions across multiple genres with AI.",
        "**Splash Pro** 用AI从文本描述跨多种流派创建原创歌曲和节拍。",
        [("Text-to-Music", "文本转音乐", "Describe a song and AI generates it"),
         ("Genre Selection", "流派选择", "Create music in any genre"),
         ("Vocal Synthesis", "人声合成", "AI vocals with customizable style"),
         ("Beat Making", "节拍制作", "Custom beats and loops"),
         ("Full Songs", "完整歌曲", "Complete songs with structure"),
         ("Download & Share", "下载分享", "MP3/WAV for commercial use")],
        [("Free","$0","10 gen/mo, non-commercial","每月10次，非商业"),
         ("Pro","$10/mo","Unlimited, commercial rights","无限，商业权利")],
        [("High-quality AI music","高质量AI音乐"),
         ("Supports vocals not just instrumentals","支持人声不仅是器乐"),
         ("Affordable Pro plan","实惠Pro计划"),
         ("Commercial usage rights","包含商业使用权")],
        [("AI vocals can sound robotic","AI人声有时听起来机械"),
         ("Less genre variety than Suno/Udio","流派多样性不如Suno/Udio"),
         ("Free tier non-commercial only","免费版仅限非商业")],
        "Content creators needing original music for videos, podcasts, and social media.",
        "需要为视频和播客获取原创音乐的内容创作者。",
        ["Feature","Splash Pro","Suno","Udio"],
        [["AI vocals","✅","✅","✅"],["Commercial rights","✅ (Pro)","✅ (Pro)","✅ (Pro)"],["Price (Pro)","$10/mo","$10/mo","$10/mo"],["Genre variety","Good","Excellent","Excellent"],["Quality","Good","Excellent","Excellent"]],
        ["功能","Splash Pro","Suno","Udio"],
        "**Rating: 3.8/5**\n\nSplash Pro is solid but faces tough competition from Suno and Udio. Good for quick music needs.",
        "**评分：3.8/5**\n\nSplash Pro可靠但面临Suno和Udio竞争。适合快速音乐需求。")

    add("voicemaker", "Voicemaker", "Voicemaker",
        "AI text-to-speech platform with 1000+ voices in 130+ languages for professional voiceovers.",
        "AI文本转语音平台，130多种语言1000多种声音用于专业配音。",
        ["audio"], ["Voicemaker","TTS","voice","AI"],
        "https://voicemaker.in", "Voicemaker", "2020", "Free; Basic $9.99/mo; Premium $19.99/mo",
        ["audio"], "https://logo.clearbit.com/voicemaker.in",
        "**Voicemaker** is an AI TTS platform with 1,000+ voices across 130+ languages for natural-sounding voice generation.",
        "**Voicemaker** 是一款AI TTS平台，拥有130多种语言的1,000多种声音。",
        [("1000+ AI Voices", "1000+种AI声音", "Male, female, child voices"),
         ("130+ Languages", "130+种语言", "Most world languages"),
         ("Voice Customization", "声音自定义", "Adjust speed, pitch, volume"),
         ("SSML Support", "SSML支持", "Fine-grained pronunciation control"),
         ("Commercial License", "商业许可", "Use generated audio commercially"),
         ("API Access", "API访问", "Integrate TTS into applications")],
        [("Free","$0","Limited chars, basic voices","有限字符，基础声音"),
         ("Basic","$9.99/mo","25K chars/mo, premium","每月25K字符，高级"),
         ("Premium","$19.99/mo","100K chars/mo, all features","每月100K字符，全部")],
        [("Massive voice library","庞大声音库"),
         ("Natural-sounding output","自然的语音输出"),
         ("Commercial use allowed","允许商业使用"),
         ("Affordable pricing","实惠价格")],
        [("Some voices less natural than ElevenLabs","一些声音不如ElevenLabs自然"),
         ("Character limits restrictive","字符限制较严"),
         ("No real-time voice cloning","没有实时声音克隆")],
        "Content creators, educators, and businesses needing multilingual voiceovers.",
        "需要多语言配音的内容创作者和企业。",
        ["Feature","Voicemaker","ElevenLabs","PlayHT"],
        [["Voice count","1000+","50+","800+"],["Languages","130+","29","130+"],["Voice cloning","❌","✅","✅"],["Price (Basic)","$9.99/mo","$5/mo","$31/mo"],["Naturalness","Good","Excellent","Good"]],
        ["功能","Voicemaker","ElevenLabs","PlayHT"],
        "**Rating: 3.9/5**\n\nVoicemaker offers widest variety but ElevenLabs sounds more natural. Best for specific languages.",
        "**评分：3.9/5**\n\nVoicemaker提供最广泛的声音种类，但ElevenLabs更自然。需要特定语言时最佳。")

    add("elevenreader", "ElevenReader", "ElevenReader",
        "AI-powered text-to-speech reader by ElevenLabs that turns any text into natural-sounding audio.",
        "ElevenLabs出品的AI文本转语音阅读应用，将任何文本转换为自然流畅的音频。",
        ["audio"], ["ElevenReader","audiobook","TTS","reading"],
        "https://elevenlabs.io/elevenreader", "ElevenLabs", "2024", "Free; Starter $5/mo",
        ["audio"], "https://logo.clearbit.com/elevenlabs.io",
        "**ElevenReader** by ElevenLabs converts any text into natural-sounding audio. Reads articles, PDFs, emails with premium voice technology.",
        "**ElevenReader** 由ElevenLabs开发，将任何文本转换为自然流畅音频。使用高级语音技术阅读文章和PDF。",
        [("Article Reading", "文章阅读", "Paste URL and listen as audio"),
         ("PDF Support", "PDF支持", "Upload and listen to PDFs"),
         ("Multiple Voices", "多种声音", "Premium voice library"),
         ("Speed Control", "速度控制", "0.5x to 3x playback"),
         ("Mobile App", "移动应用", "iOS and Android apps"),
         ("Clipboard Reading", "剪贴板阅读", "Read copied text with one tap")],
        [("Free","$0","Basic voices, limited","基础声音，有限"),
         ("Starter","$5/mo","Premium voices, unlimited","高级声音，无限")],
        [("Industry-leading voice quality","业界领先的语音质量"),
         ("Great for multitasking","非常适合多任务"),
         ("Multiple input formats","多种输入格式"),
         ("Very affordable at $5/mo","每月$5非常实惠")],
        [("Requires ElevenLabs account","需要ElevenLabs账户"),
         ("Some docs need formatting fixes","某些文档需格式修复"),
         ("Long books expensive in credits","长篇书籍积分消耗多")],
        "Busy professionals and students wanting to consume written content as audio on the go.",
        "忙碌的专业人士和学生，想旅途中以音频形式消费书面内容。",
        ["Feature","ElevenReader","Speechify","NaturalReader"],
        [["Voice quality","Excellent","Good","Good"],["Price","$0-$5/mo","$29/mo","$10/mo"],["URL reading","✅","✅","❌"],["PDF support","✅","✅","✅"],["Mobile app","✅","✅","✅"]],
        ["功能","ElevenReader","Speechify","NaturalReader"],
        "**Rating: 4.4/5**\n\nElevenReader is the best AI reading app thanks to superior voice quality. Best value at $5/mo.",
        "**评分：4.4/5**\n\nElevenReader凭借卓越语音质量成为最佳AI阅读应用。每月$5是最佳性价比。")

    # --- AI Search ---
    add("you", "You.com", "You.com",
        "AI search engine with summarized answers, citations, AI chat, and no ads.",
        "AI搜索引擎，提供带引用的摘要答案、AI聊天和无广告体验。",
        ["search"], ["You.com","search","AI","chat"],
        "https://you.com", "You.com", "2021", "Free; You Pro $20/mo",
        ["search"], "https://logo.clearbit.com/you.com",
        "**You.com** provides direct, cited answers instead of just links. Combines web search with AI chat, coding, and creative tools.",
        "**You.com** 提供直接的带引用答案而非仅链接。结合网页搜索与AI聊天和创意工具。",
        [("AI Search", "AI搜索", "Summarized answers with citations"),
         ("YouChat", "YouChat", "Chat with AI for follow-ups"),
         ("Mode Selection", "模式选择", "Research, Genius, Create modes"),
         ("Code Generation", "代码生成", "Built-in AI coding assistant"),
         ("No Ads", "无广告", "Clean, ad-free search"),
         ("Privacy Controls", "隐私控制", "Customizable privacy settings")],
        [("Free","$0","Basic AI search, limited","基础AI搜索，有限"),
         ("You Pro","$20/mo","Unlimited AI, premium models","无限AI，高级模型")],
        [("Cited answers build trust","带引用的答案增强信任"),
         ("Ad-free experience refreshing","无广告体验令人耳目一新"),
         ("Multiple AI modes for different needs","多种AI模式"),
         ("Good for research with sources","适合需要来源的研究")],
        [("AI summaries can be inaccurate","AI摘要有时不准确"),
         ("Not as comprehensive as Google","某些搜索不如Google全面"),
         ("Same price as Perplexity Pro","与Perplexity Pro价格相同")],
        "Researchers, students, and professionals wanting AI-powered search with cited sources.",
        "需要带来源引用的AI搜索的研究人员和专业人士。",
        ["Feature","You.com","Perplexity","Google"],
        [["AI summaries","✅","✅","✅ (SGE)"],["Source citations","✅","✅","❌"],["AI chat","✅","✅","❌"],["Ad-free","✅","✅","❌"],["Price (Pro)","$20/mo","$20/mo","Free"]],
        ["功能","You.com","Perplexity","Google"],
        "**Rating: 4.2/5**\n\nYou.com is a strong AI search engine. Multiple modes and ad-free experience make it worth trying.",
        "**评分：4.2/5**\n\nYou.com是一款有力的AI搜索引擎。多种模式和无广告体验值得一试。")

    add("phind", "Phind", "Phind",
        "AI search engine built for developers with code-aware search and technical explanations.",
        "专为开发者构建的AI搜索引擎，具备代码感知搜索和技术解释。",
        ["search","coding"], ["Phind","developer","search","coding"],
        "https://www.phind.com", "Phind", "2022", "Free; Pro $10/mo",
        ["search"], "https://logo.clearbit.com/phind.com",
        "**Phind** is purpose-built for developers. Understands code context, searches technical docs, and provides code examples.",
        "**Phind** 专为开发者构建。理解代码上下文，搜索技术文档，提供代码示例。",
        [("Developer-First Search", "开发者优先搜索", "Optimized for technical queries"),
         ("Code Generation", "代码生成", "Code solutions with explanations"),
         ("Doc Search", "文档搜索", "Searches docs, Stack Overflow, GitHub"),
         ("Context Awareness", "上下文感知", "Understands codebase and framework"),
         ("Pair Programming", "结对编程", "Interactive coding with AI"),
         ("GPT-4 Powered", "GPT-4驱动", "Latest AI models")],
        [("Free","$0","Limited queries, GPT-3.5","有限查询，GPT-3.5"),
         ("Pro","$10/mo","Unlimited, GPT-4, priority","无限，GPT-4，优先")],
        [("Dramatically faster than Stack Overflow","比搜索Stack Overflow快得多"),
         ("Code-aware understands developer intent","代码感知理解开发者意图"),
         ("Excellent for debugging and learning","非常适合调试和学习"),
         ("Affordable Pro plan","实惠的Pro计划")],
        [("Developer-focused only","仅聚焦开发者"),
         ("Can hallucinate incorrect code","可能产生错误代码"),
         ("Less polished UX than Perplexity","UX不如Perplexity精致")],
        "Software developers wanting fast, code-aware search for debugging and technical problem-solving.",
        "希望获得快速代码感知搜索用于调试和解决技术问题的开发者。",
        ["Feature","Phind","You.com","Perplexity"],
        [["Code-aware search","✅","Partial","❌"],["Stack Overflow","✅","❌","❌"],["Code generation","✅","✅","❌"],["Price (Pro)","$10/mo","$20/mo","$20/mo"],["Best for","Developers","General","Research"]],
        ["功能","Phind","You.com","Perplexity"],
        "**Rating: 4.3/5**\n\nPhind is the best AI search for developers. Code-aware and faster than Stack Overflow.",
        "**评分：4.3/5**\n\nPhind是开发者的最佳AI搜索引擎。代码感知，比Stack Overflow更快。")

    # --- AI Detection ---
    add("undetectable-ai", "Undetectable AI", "Undetectable AI",
        "AI content detection and humanization tool that makes AI text pass as human-written.",
        "AI内容检测和人化工具，使AI生成的文本通过检测。",
        ["writing"], ["Undetectable AI","detection","humanizer","writing"],
        "https://undetectable.ai", "Undetectable AI", "2023", "Free trial; Pro $9.99/mo",
        ["writing"], "https://logo.clearbit.com/undetectable.ai",
        "**Undetectable AI** detects AI-generated content and humanizes it to bypass AI detectors while preserving meaning.",
        "**Undetectable AI** 检测AI生成内容并人化以绕过检测器，保留原始含义。",
        [("AI Detection", "AI检测", "Checks against multiple AI detectors"),
         ("Humanization", "人化处理", "Rewrites AI text to sound human"),
         ("Bypass Detectors", "绕过检测器", "Passes Turnitin, GPTZero, etc"),
         ("Readability Check", "可读性检查", "Ensures rewritten text readable"),
         ("Plagiarism Free", "无抄袭", "Guarantees original content"),
         ("Batch Processing", "批量处理", "Process multiple documents")],
        [("Free Trial","$0","250 words","250词"),
         ("Pro","$9.99/mo","10,000 words/mo","每月10,000词"),
         ("Business","$29.99/mo","50,000 words/mo","每月50,000词")],
        [("Effectively bypasses most detectors","有效绕过大多数检测器"),
         ("Detection + humanization in one tool","检测和人化集于一体"),
         ("Affordable pricing","价格实惠"),
         ("Maintains original meaning","保持原始含义")],
        [("Humanized text can read awkwardly","人化文本有时不够自然"),
         ("May need multiple passes","可能需要多次处理"),
         ("Ethical concerns about bypassing detection","绕过检测有伦理问题")],
        "Content marketers and writers using AI tools needing content to pass AI detection checks.",
        "使用AI工具但需要通过AI检测的内容营销人员和写作者。",
        ["Feature","Undetectable AI","StealthGPT","QuillBot"],
        [["AI detection","✅","❌","❌"],["Humanization","✅","✅","❌"],["Bypass rate","High","High","N/A"],["Price (Pro)","$9.99/mo","$14.99/mo","Free-$20/mo"],["Ethical use","Questionable","Questionable","Fine"]],
        ["功能","Undetectable AI","StealthGPT","QuillBot"],
        "**Rating: 3.5/5**\n\nUndetectable AI works but raises ethical questions. Use responsibly — always disclose AI assistance.",
        "**评分：3.5/5**\n\nUndetectable AI有效但引发伦理问题。请负责任地使用，始终披露AI辅助。")

    add("stealthgpt", "StealthGPT", "StealthGPT",
        "AI writing tool generating undetectable content designed to bypass AI detectors like Turnitin and GPTZero.",
        "AI写作工具，生成旨在绕过Turnitin和GPTZero等AI检测器的不可检测内容。",
        ["writing"], ["StealthGPT","undetectable","writing","bypass"],
        "https://stealthgpt.ai", "StealthGPT", "2023", "Free trial; Essential $14.99/mo; Pro $29.99/mo",
        ["writing"], "https://logo.clearbit.com/stealthgpt.ai",
        "**StealthGPT** generates content designed to bypass AI detection tools. Produces human-sounding text passing major detectors.",
        "**StealthGPT** 生成旨在绕过AI检测的内容。产生能通过主要检测器的类人文本。",
        [("Undetectable Writing", "不可检测写作", "Text that passes AI detectors"),
         ("Multiple Models", "多种模型", "Different writing styles and tones"),
         ("SEO Mode", "SEO模式", "SEO-optimized undetectable content"),
         ("Essay Writer", "论文写作器", "Built-in essay generation"),
         ("Bypass Guarantee", "绕过保证", "Claims to bypass all detectors"),
         ("API Access", "API访问", "Integrate into workflow")],
        [("Free Trial","$0","Limited words","有限词数"),
         ("Essential","$14.99/mo","Basic undetectable gen","基础生成"),
         ("Pro","$29.99/mo","Unlimited, SEO, API","无限，SEO，API")],
        [("Content genuinely passes most detectors","内容确实通过大多数检测器"),
         ("Multiple writing styles","多种写作风格"),
         ("Built-in essay tools","内置论文工具"),
         ("SEO mode for marketers","面向营销人员的SEO模式")],
        [("Quality can be inconsistent","质量可能不稳定"),
         ("Significant ethical concerns","重大伦理问题"),
         ("More expensive than Undetectable AI","比Undetectable AI更贵"),
         ("Detectors constantly improving","检测器不断改进")],
        "Content creators needing AI-assisted writing that passes detection. Use ethically.",
        "需要通过检测的AI辅助写作的内容创作者。请合乎伦理地使用。",
        ["Feature","StealthGPT","Undetectable AI","QuillBot"],
        [["AI detection bypass","✅","✅","❌"],["Writing quality","Good","Good","Good"],["SEO mode","✅","❌","❌"],["Price","$14.99+/mo","$9.99+/mo","Free-$20/mo"],["Essay gen","✅","❌","❌"]],
        ["功能","StealthGPT","Undetectable AI","QuillBot"],
        "**Rating: 3.3/5**\n\nStealthGPT works but raises serious ethical concerns. AI assistance should be disclosed, not hidden.",
        "**评分：3.3/5**\n\nStealthGPT有效但引发严重伦理问题。AI辅助应当被披露，而非隐藏。")

    # --- AI SEO ---
    add("surfer-seo", "SurferSEO", "SurferSEO",
        "AI SEO tool with content optimization, keyword research, SERP analysis, and AI writing assistant.",
        "AI SEO工具，提供内容优化、关键词研究、SERP分析和AI写作助手。",
        ["writing"], ["SurferSEO","SEO","content","optimization"],
        "https://surferseo.com", "Surfer SEO", "2017", "Essential $89/mo; Scale $129/mo; Enterprise $219/mo",
        ["writing"], "https://logo.clearbit.com/surferseo.com",
        "**SurferSEO** is an AI SEO platform for creating search-optimized content with content scoring, keyword research, and AI writing.",
        "**SurferSEO** 是一款AI SEO平台，提供内容评分、关键词研究和AI写作帮助创建搜索优化内容。",
        [("Content Score", "内容评分", "Real-time SEO score for articles"),
         ("SERP Analyzer", "SERP分析器", "Analyze top-ranking pages"),
         ("Keyword Research", "关键词研究", "AI keyword discovery and clustering"),
         ("AI Writing", "AI写作", "SEO-optimized outlines and paragraphs"),
         ("Audit", "审计", "Audit existing content for SEO issues"),
         ("Outline Builder", "提纲构建器", "Generate outlines from SERP data")],
        [("Essential","$89/mo","Content editor, keyword research","内容编辑器，关键词研究"),
         ("Scale","$129/mo","AI writing, audits, API","AI写作，审计，API"),
         ("Enterprise","$219/mo","Custom limits, white-label","自定义限制，白标")],
        [("Data-driven content optimization","数据驱动的内容优化"),
         ("Excellent SERP analysis","出色的SERP分析"),
         ("AI writing produces SEO content","AI写作产生SEO友好内容"),
         ("Clean, intuitive interface","简洁直观的界面")],
        [("Expensive — cheapest $89/mo","昂贵——最便宜$89/月"),
         ("No free tier","没有免费版"),
         ("AI quality not as good as dedicated writers","AI写作不如专门的写作工具")],
        "SEO professionals, content marketers, and agencies needing data-driven content optimization.",
        "需要数据驱动内容优化的SEO专业人士和内容营销人员。",
        ["Feature","SurferSEO","Semrush","Clearscope"],
        [["Content scoring","✅","✅","✅"],["AI writing","✅","❌","❌"],["SERP analysis","✅","✅","✅"],["Price (entry)","$89/mo","$130/mo","$170/mo"],["Ease of use","Excellent","Complex","Good"]],
        ["功能","SurferSEO","Semrush","Clearscope"],
        "**Rating: 4.2/5**\n\nSurferSEO is the best SEO content tool. Data-driven optimization with AI writing — ideal for organic growth.",
        "**评分：4.2/5**\n\nSurferSEO是最佳SEO内容工具。数据驱动优化配合AI写作——适合自然增长。")

    # --- AI 3D ---
    add("poly", "Poly", "Poly",
        "AI 3D texture and PBR material generator creating photorealistic textures from text prompts and images.",
        "AI 3D纹理和PBR材质生成器，从文本和图像创建逼真纹理。",
        ["3d"], ["Poly","3D","texture","PBR","material"],
        "https://poly.cam", "Poly", "2022", "Free; Pro $30/mo",
        ["3d"], "https://logo.clearbit.com/poly.cam",
        "**Poly** creates photorealistic PBR textures from text or images for games, AR/VR, and 3D design.",
        "**Poly** 从文本或图像创建逼真PBR纹理，用于游戏、AR/VR和3D设计。",
        [("Text-to-Texture", "文本转纹理", "Generate PBR textures from text"),
         ("Image-to-Texture", "图像转纹理", "Create textures from reference photos"),
         ("PBR Materials", "PBR材质", "Complete PBR material sets"),
         ("3D Capture", "3D捕获", "Scan real objects with your phone"),
         ("Seamless Textures", "无缝纹理", "Perfectly tileable textures"),
         ("Export Formats", "导出格式", "OBJ, GLTF, USDZ, FBX")],
        [("Free","$0","10 textures/mo, basic","每月10个纹理"),
         ("Pro","$30/mo","Unlimited, high quality, API","无限，高质量，API")],
        [("Incredibly realistic PBR materials","极其逼真的PBR材质"),
         ("Text-to-texture saves hours","文本转纹理节省数小时"),
         ("Phone 3D scanning impressive","手机3D扫描令人印象深刻"),
         ("All major 3D format exports","导出所有主要3D格式")],
        [("Pro plan is expensive","Pro版价格较高"),
         ("Free tier very limited","免费版非常有限"),
         ("Generated textures may need refinement","生成纹理可能需调整")],
        "3D artists, game developers, and designers needing PBR textures and materials quickly.",
        "需要快速获取PBR纹理和材质的3D艺术家和游戏开发者。",
        ["Feature","Poly","Meshy","Tripo3D"],
        [["Texture generation","✅","✅","✅"],["3D scanning","✅","❌","❌"],["PBR materials","✅","✅","✅"],["Price (Pro)","$30/mo","$20/mo","$15/mo"],["Best for","Textures","Full 3D","Full 3D"]],
        ["功能","Poly","Meshy","Tripo3D"],
        "**Rating: 4.1/5**\n\nPoly excels at texture generation. The best tool for PBR textures specifically.",
        "**评分：4.1/5**\n\nPoly在纹理生成方面表现出色。特别需要PBR纹理时的最佳工具。")

    # --- Other Presentations ---
    add("presentations-ai", "Presentations.ai", "Presentations.ai",
        "AI presentation maker creating professional slide decks from text prompts with beautiful templates.",
        "AI演示文稿制作工具，从文本提示创建专业幻灯片。",
        ["productivity"], ["Presentations.ai","presentation","slides","AI"],
        "https://presentations.ai", "Presentations.ai", "2023", "Free; Pro $10/mo; Team $20/user/mo",
        ["productivity"], "https://logo.clearbit.com/presentations.ai",
        "**Presentations.ai** creates professional slide decks from text prompts with beautiful templates, smart layouts, and collaboration.",
        "**Presentations.ai** 从文本提示创建专业幻灯片，提供美观模板、智能布局和协作。",
        [("AI Slide Generation", "AI幻灯片生成", "Full presentations from topics"),
         ("Smart Layouts", "智能布局", "AI-designed professional layouts"),
         ("Template Library", "模板库", "Hundreds of professional templates"),
         ("Collaboration", "协作", "Real-time team editing"),
         ("Brand Kit", "品牌套件", "Apply company branding automatically"),
         ("Export", "导出", "PPTX, PDF, or share via link")],
        [("Free","$0","3 presentations","3个演示文稿"),
         ("Pro","$10/mo","Unlimited, all templates","无限，全部模板"),
         ("Team","$20/user/mo","Team collaboration","团队协作")],
        [("Creates presentations in seconds","几秒内创建演示文稿"),
         ("Professional designs out of the box","开箱即用的专业设计"),
         ("More affordable than Beautiful.ai","比Beautiful.ai更实惠"),
         ("Good template selection","不错的模板选择")],
        [("Limited customization vs PowerPoint","与PowerPoint相比自定义有限"),
         ("AI content can be generic","AI内容可能比较普通"),
         ("Export quality varies","导出质量不稳定")],
        "Professionals, students, and anyone needing quick professional presentations without design skills.",
        "需要快速创建专业演示文稿但缺乏设计技能的人。",
        ["Feature","Presentations.ai","Gamma","Beautiful.ai"],
        [["AI generation","✅","✅","✅"],["PPTX export","✅","✅","✅"],["Collaboration","✅","✅","✅"],["Price (Pro)","$10/mo","$10/mo","$13/mo"],["Templates","Hundreds","Good","Good"]],
        ["功能","Presentations.ai","Gamma","Beautiful.ai"],
        "**Rating: 4.0/5**\n\nPresentations.ai is a solid AI presentation tool at a great price. Best budget option for quick slides.",
        "**评分：4.0/5**\n\nPresentations.ai是价格出色的AI演示文稿工具。快速制作专业幻灯片的最佳预算选择。")

    add("plus-ai", "Plus AI", "Plus AI",
        "AI Google Slides add-on that creates and enhances presentations directly inside Google Slides.",
        "AI Google Slides插件，直接在Google Slides中创建和增强演示文稿。",
        ["productivity"], ["Plus AI","Google Slides","presentation","AI"],
        "https://www.plusdocs.com/plus-ai", "Plus AI", "2022", "Free trial; Essentials $10/mo; Pro $20/mo",
        ["productivity"], "https://logo.clearbit.com/plusdocs.com",
        "**Plus AI** is an AI Google Slides add-on that creates, edits, and enhances presentations directly inside Google Slides.",
        "**Plus AI** 是一款AI Google Slides插件，直接在Google Slides中创建、编辑和增强演示文稿。",
        [("In-Slides AI", "幻灯片内AI", "Works directly inside Google Slides"),
         ("Presentation Generator", "演示文稿生成器", "Full decks from topics or outlines"),
         ("Slide Editor", "幻灯片编辑器", "Rewrite, reformat individual slides"),
         ("Theme Matching", "主题匹配", "Matches existing slide theme"),
         ("Brand Snap", "品牌适配", "Apply company colors and fonts"),
         ("Charts & Diagrams", "图表和图示", "AI-generated data visualizations")],
        [("Free Trial","$0","3 presentations","3个演示文稿"),
         ("Essentials","$10/mo","Unlimited creation","无限创建"),
         ("Pro","$20/mo","Full editing, team","完整编辑，团队")],
        [("Native in Google Slides — zero learning curve","原生在Google Slides中——零学习曲线"),
         ("Integrates with existing workflows","与现有工作流集成"),
         ("Good slide designs","出色的幻灯片设计"),
         ("Affordable pricing","价格实惠")],
        [("Google Slides only — no PowerPoint","仅支持Google Slides"),
         ("Design quality not as high as standalone tools","设计质量不如独立工具"),
         ("Limited vs full AI platforms","与完整AI平台相比功能有限")],
        "Google Workspace users wanting AI presentation help without leaving Google Slides.",
        "希望不离开Google Slides获得AI演示文稿帮助的Google Workspace用户。",
        ["Feature","Plus AI","Presentations.ai","Gamma"],
        [["Google Slides native","✅","❌","❌"],["AI generation","✅","✅","✅"],["PPTX export","❌","✅","✅"],["Price","$10/mo","$10/mo","$10/mo"],["Collaboration","✅","✅","✅"]],
        ["功能","Plus AI","Presentations.ai","Gamma"],
        "**Rating: 4.0/5**\n\nPlus AI is the best choice for Google Slides users. Works where you already work — zero friction.",
        "**评分：4.0/5**\n\nPlus AI是Google Slides用户的最佳选择。在您已使用的工具中工作——零摩擦。")

    return tools

def gen_en(t):
    slug = t['slug']
    name = t['name']
    en_cats = ", ".join(f'"{c}"' for c in t['en_cats'])
    en_tags = ", ".join(f'"{tag}"' for tag in t['en_tags'])
    tool_cats = ", ".join(f'"{c}"' for c in t['tool_cats'])
    
    md = f'''---
slug: "{slug}"

title: "{name} — Best AI Tool"
description: "{t['en_desc']}"
categories: [{en_cats}]
tags: [{en_tags}]
type: tool
tools:
  name: "{name}"
  url: "{t['url']}"
  developer: "{t['dev']}"
  founded: "{t['founded']}"
  pricing: "{t['pricing_s']}"
  category: [{tool_cats}]
  logo: "{t['logo']}"

---

# {name} Review

{t['en_intro']}

## Key Features

'''
    for f in t['features']:
        md += f"- **{f[0]}** — {f[2]}\n"
    
    md += "\n## Pricing\n\n| Plan | Price | Key Features |\n|------|-------|-------------|\n"
    for p in t['pricing']:
        md += f"| {p[0]} | {p[1]} | {p[2]} |\n"
    
    md += "\n## Pros\n\n"
    for p in t['pros']:
        md += f"✅ {p[0]}\n\n"
    
    md += "## Cons\n\n"
    for c in t['cons']:
        md += f"❌ {c[0]}\n\n"
    
    md += f"\n## Who It's Best For\n\n{t['en_best']}\n\n"
    
    md += "## How It Compares\n\n"
    h = t['en_comp_h']
    md += "| " + " | ".join(h) + " |\n"
    md += "|" + "|".join("---" for _ in h) + "|\n"
    for r in t['en_comp_rows']:
        md += "| " + " | ".join(r) + " |\n"
    
    md += f"\n## Verdict\n\n{t['en_verdict']}\n\n"
    md += f'{{< cta "{slug}" "Try {name} →" >}}\n'
    return md

def gen_zh(t):
    slug = t['slug']
    name = t['zh_name']
    en_cats = ", ".join(f'"{c}"' for c in t['en_cats'])
    en_tags = ", ".join(f'"{tag}"' for tag in t['en_tags'])
    tool_cats = ", ".join(f'"{c}"' for c in t['tool_cats'])
    
    md = f'''---
slug: "{slug}"

title: "{name} — 最佳AI工具"
description: "{t['zh_desc']}"
categories: [{en_cats}]
tags: [{en_tags}]
type: tool
tools:
  name: "{name}"
  url: "{t['url']}"
  developer: "{t['dev']}"
  founded: "{t['founded']}"
  pricing: "{t['pricing_s']}"
  category: [{tool_cats}]
  logo: "{t['logo']}"

---

# {name} 评测

{t['zh_intro']}

## 核心功能

'''
    for f in t['features']:
        md += f"- **{f[1]}** — {f[0]}\n"
    
    md += "\n## 定价\n\n| 方案 | 价格 | 核心功能 |\n|------|------|----------|\n"
    for p in t['pricing']:
        md += f"| {p[3]} | {p[1]} | {p[2]} |\n"
    
    md += "\n## 优势\n\n"
    for p in t['pros']:
        md += f"✅ {p[1]}\n\n"
    
    md += "## 劣势\n\n"
    for c in t['cons']:
        md += f"❌ {c[1]}\n\n"
    
    md += f"\n## 适合人群\n\n{t['zh_best']}\n\n"
    
    md += "## 对比评测\n\n"
    h = t['zh_comp_h']
    md += "| " + " | ".join(h) + " |\n"
    md += "|" + "|".join("---" for _ in h) + "|\n"
    for r in t['zh_comp_rows']:
        md += "| " + " | ".join(r) + " |\n"
    
    md += f"\n## 总结\n\n{t['zh_verdict']}\n\n"
    md += f'{{< cta "{slug}" "试用 {name} →" >}}\n'
    return md

if __name__ == "__main__":
    tools = make_tools()
    print(f"Total tools: {len(tools)}")
    
    # Check for existing files
    existing = set(os.listdir(TOOLS_DIR)) if os.path.exists(TOOLS_DIR) else set()
    zh_existing = set(os.listdir(ZH_DIR)) if os.path.exists(ZH_DIR) else set()
    
    created = []
    skipped = []
    
    for t in tools:
        en_path = os.path.join(TOOLS_DIR, f"{t['slug']}.md")
        zh_path = os.path.join(ZH_DIR, f"{t['slug']}.md")
        
        if f"{t['slug']}.md" in existing:
            skipped.append(t['slug'])
            continue
        
        en_content = gen_en(t)
        zh_content = gen_zh(t)
        
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write(en_content)
        with open(zh_path, 'w', encoding='utf-8') as f:
            f.write(zh_content)
        
        created.append(t['slug'])
    
    print(f"\nCreated: {len(created)} tools ({len(created)*2} files)")
    for s in created:
        print(f"  ✅ {s}")
    if skipped:
        print(f"\nSkipped (already exist): {len(skipped)}")
        for s in skipped:
            print(f"  ⏭️ {s}")
