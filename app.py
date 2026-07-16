import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ========== 页面配置 ==========
st.set_page_config(
    page_title="徐朝阳 | Personal Resume - xzy",
    page_icon="🤖",
    layout="wide"
)

# ========== Session State 初始化 ==========
if 'language' not in st.session_state:
    st.session_state.language = 'zh'
if 'loading_shown' not in st.session_state:
    st.session_state.loading_shown = False

# ========== 多语言文本 ==========
T = {
    'zh': {
        'sidebar_title': '徐朝阳',
        'sidebar_subtitle': 'AI应用开发实习生',
        'skills_heading': '⚡ 技能',
        'download_btn': '📄 下载简历 (PDF)',
        'quick_ask': '💬 快捷提问',
        'quick_q1': '💼 介绍项目经历',
        'quick_q2': '🛠️ 核心技能',
        'quick_q3': '🎯 求职意向',
        'tab1': '🏠 关于我',
        'tab2': '💼 项目经历',
        'tab3': '🤖 AI 问答',
        'about_heading': '关于我',
        'about_sub': '从种子到代码的转型之路',
        'about_text': '''
我现在是天津农学院种子科学与工程专业的大二学生。在学习本专业的过程中，
我发现自己对人工智能的热情远远超过了传统农业。于是我开始自学Python和AI开发。

目前已掌握Python编程基础、LangChain框架、RAG系统搭建、Streamlit网页开发等技能。
正在寻找一份AI应用开发方向的实习，希望能将技术落地到实际产品中。

**目标：** 成为能用AI解决实际问题的开发者。
''',
        'projects_heading': '项目经历',
        'project1_title': '🌱 种子知识智能问答系统',
        'project1_tech': 'Python / LangChain / ChromaDB / Streamlit / DeepSeek API',
        'project1_desc': '''
- 使用 LangChain 搭建 RAG（检索增强生成）管线
- 将农作物/种子学专业资料切片存入 ChromaDB 向量数据库
- 基于 DeepSeek 大模型实现自然语言问答
- 使用 Streamlit 构建 Web 交互界面
''',
        'project2_title': '🎨 AI商业PPT工作流搭建',
        'project2_tech': 'Codex / Claude / PowerPoint / HTML',
        'project2_desc': '''
- 利用 Codex + Claude 构建 AI 辅助 PPT 制作流程，实现商业 PPT 快速生产与优化
- 批量生成商业 PPT 页面，将设计图片转换为可编辑 PPT，制作教育课件及比赛汇报 PPT
- AI 生成 HTML 策划方案，人工优化页面排版与视觉效果
- 提高 PPT 制作效率，可独立完成需求分析到最终交付
''',
        'project3_title': '📱 AIGC内容创作与自媒体运营',
        'project3_tech': 'AI Content / 小红书 / 摄影教程',
        'project3_desc': '''
- 独立运营摄影教程类小红书账号，探索 AI 辅助内容生产模式
- AI 辅助选题策划，AI 生成文案与宣传图，HTML 教程页面制作
- 累计阅读量 20,000+，点赞收藏 1,000+，建立完整 AI 内容生产闭环
''',
        'ai_title': '🤖 问问我的简历',
        'ai_caption': 'AI 助手读取了我的简历信息。你可以直接问它关于我的任何问题。',
        'ai_ready': '✅ AI助手已就绪',
        'ai_placeholder': '问任何关于我的问题...',
    },
    'en': {
        'sidebar_title': 'Xu Zhaoyang',
        'sidebar_subtitle': 'AI Developer Intern',
        'skills_heading': '⚡ Skills',
        'download_btn': '📄 Download Resume (PDF)',
        'quick_ask': '💬 Quick Ask',
        'quick_q1': '💼 Projects',
        'quick_q2': '🛠️ Skills',
        'quick_q3': '🎯 Job Target',
        'tab1': '🏠 About Me',
        'tab2': '💼 Projects',
        'tab3': '🤖 AI Q&A',
        'about_heading': 'About Me',
        'about_sub': 'From Seeds to Code',
        'about_text': '''
I am a sophomore majoring in Seed Science and Engineering at Tianjin Agricultural University.
While studying agriculture, I discovered my passion for AI far exceeded my interest in traditional farming,
so I began self-learning Python and AI development.

I have acquired skills in Python programming, LangChain framework, RAG system development,
and Streamlit web development. I am currently seeking an internship in AI application development,
aiming to apply technology to real-world products.

**Goal:** Become a developer who solves real problems with AI.
''',
        'projects_heading': 'Projects',
        'project1_title': '🌱 Seed Knowledge Q&A System',
        'project1_tech': 'Python / LangChain / ChromaDB / Streamlit / DeepSeek API',
        'project1_desc': '''
- Built RAG (Retrieval-Augmented Generation) pipeline with LangChain
- Stored crop/seed science materials in ChromaDB vector database
- Implemented natural language Q&A based on DeepSeek LLM
- Built interactive web interface with Streamlit
''',
        'project2_title': '🎨 AI-Powered PPT Workflow',
        'project2_tech': 'Codex / Claude / PowerPoint / HTML',
        'project2_desc': '''
- Built AI-assisted PPT production workflow using Codex + Claude for rapid business PPT creation
- Batch-generated commercial PPT pages, converted design images to editable PPTs
- AI-generated HTML proposals with manual optimization of layout and visuals
- Delivered end-to-end service from requirements analysis to final delivery
''',
        'project3_title': '📱 AIGC Content Creation & Social Media',
        'project3_tech': 'AI Content / RED / Photography',
        'project3_desc': '''
- Independently operated a photography tutorial account on RED (Xiaohongshu)
- AI-assisted topic planning, copywriting, promotional image generation, HTML tutorials
- Achieved 20,000+ total reads, 1,000+ likes/bookmarks, established complete AI content pipeline
''',
        'ai_title': '🤖 Ask My Resume',
        'ai_caption': 'This AI assistant has read my resume. Ask anything about me.',
        'ai_ready': '✅ AI Assistant Ready',
        'ai_placeholder': 'Ask anything about me...',
    }
}

def t(key):
    """快捷翻译函数"""
    return T[st.session_state.language][key]

# ========== 全局 CSS（始终生效）==========
st.markdown("""
<style>
/* ===== 侧边栏渐变背景 ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #09090f 0%, #0f0f1e 35%, #0c0c1a 65%, #090912 100%);
}

/* ===== 侧边栏分割线 ===== */
section[data-testid="stSidebar"] hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.45), rgba(139, 92, 246, 0.25), transparent);
    margin: 1.2rem 0;
}

/* ===== 技能进度条 ===== */
.skill-row {
    margin-bottom: 13px;
}
.skill-name {
    color: rgba(255,255,255,0.65);
    font-size: 12px;
    margin-bottom: 4px;
    display: block;
    letter-spacing: 0.5px;
}
.skill-track {
    height: 3px;
    background: rgba(255,255,255,0.06);
    border-radius: 3px;
    overflow: hidden;
}
.skill-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #a78bfa);
    width: 0%;
    transition: width 1s ease 0.2s;
}
.skill-row:hover .skill-fill {
    filter: brightness(1.3);
}
.skill-row:hover .skill-name {
    color: rgba(255,255,255,0.9);
}

/* ===== 自定义标签栏 ===== */
div[data-testid="column"] button[kind="primary"] {
    border-bottom: 2px solid #6366f1 !important;
    border-radius: 6px 6px 0 0 !important;
}
div[data-testid="column"] button[kind="secondary"] {
    border-bottom: 2px solid transparent !important;
    color: rgba(255,255,255,0.5) !important;
    border-radius: 6px 6px 0 0 !important;
}
div[data-testid="column"] button[kind="secondary"]:hover {
    color: rgba(255,255,255,0.8) !important;
    border-bottom-color: rgba(99, 102, 241, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# ========== 加载动画（仅首次访问）==========
if not st.session_state.loading_shown:
    st.session_state.loading_shown = True
    st.markdown("""
    <style>
    /* ===== 加载动画 ===== */
    .loading-overlay {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: #0a0a0a;
        z-index: 999999;
        display: flex !important;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        animation: overlayFade 1.8s ease-in-out forwards;
    }
    .loading-overlay * { box-sizing: border-box; }
    .loading-name {
        color: rgba(255,255,255,0.4);
        font-size: 12px;
        letter-spacing: 3px;
        margin-bottom: 24px;
        opacity: 0;
        animation: textIn 0.5s ease-out 0.2s forwards;
    }
    .loading-track {
        width: 200px;
        height: 2px;
        background: rgba(255,255,255,0.15);
        border-radius: 2px;
        overflow: hidden;
    }
    .loading-bar {
        height: 100%;
        background: linear-gradient(90deg, #6366f1, #8b5cf6, #a78bfa);
        border-radius: 2px;
        animation: barLoad 1.2s ease-in-out 0.4s forwards;
    }
    .loading-sub {
        color: rgba(255,255,255,0.4);
        font-size: 12px;
        margin-top: 16px;
        letter-spacing: 3px;
        opacity: 0;
        animation: textIn 0.5s ease-out 0.5s forwards;
    }
    @keyframes barLoad {
        0%   { width: 0%; }
        100% { width: 100%; }
    }
    @keyframes textIn {
        0%   { opacity: 0; transform: translateY(8px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes overlayFade {
        0%, 60%  { opacity: 1; }
        100%     { opacity: 0; pointer-events: none; visibility: hidden; }
    }
    .stApp {
        animation: contentReveal 0.01s 1.8s both;
    }
    @keyframes contentReveal {
        from { visibility: hidden; }
        to   { visibility: visible; }
    }
    </style>

    <div class="loading-overlay">
        <div class="loading-name">Initializing_Streamlit_xzy</div>
        <div class="loading-track">
            <div class="loading-bar"></div>
        </div>
        <div class="loading-sub">LOADING</div>
    </div>
    """, unsafe_allow_html=True)

# ========== 侧边栏 ==========
with st.sidebar:
    st.title(t('sidebar_title'))
    st.markdown(
        f"<p style='color: rgba(255,255,255,0.5); font-size: 13px; margin-top: -10px; letter-spacing: 1px;'>{t('sidebar_subtitle')}</p>",
        unsafe_allow_html=True
    )

    # ---- 语言切换 ----
    lang_labels = ["中文", "EN"]
    current_idx = 0 if st.session_state.language == 'zh' else 1
    selected_lang = st.radio(
        "Language", lang_labels,
        horizontal=True,
        index=current_idx,
        label_visibility="collapsed",
        key="lang_switch"
    )
    new_lang = 'zh' if selected_lang == '中文' else 'en'
    if new_lang != st.session_state.language:
        st.session_state.language = new_lang
        st.rerun()

    # ---- 联系方式 ----
    st.markdown(
        f"<p style='color: rgba(255,255,255,0.4); font-size: 12px; margin-top: 4px; line-height: 1.8;'>"
        "📧 1952859208@qq.com<br>"
        "<a href='https://github.com/zhaoyangxu18-pixel' style='color: rgba(255,255,255,0.4); text-decoration: none;'>🔗 zhaoyangxu18-pixel</a>"
        "</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # ---- 技能进度条 ----
    st.markdown(f"<p style='color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 1px; margin-bottom: 16px;'>{t('skills_heading')}</p>", unsafe_allow_html=True)

    skills = [
        ("Python", 75),
        ("AIGC 内容生成", 72),
        ("Prompt Engineering", 70),
        ("LangChain", 60),
        ("Claude / DeepSeek API", 65),
        ("Streamlit", 55),
        ("Photoshop / Lightroom", 60),
    ]

    for name, level in skills:
        st.markdown(f"""
        <div class="skill-row">
            <span class="skill-name">{name}</span>
            <div class="skill-track">
                <div class="skill-fill" style="width: {level}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ---- 简历下载 ----
    resume_pdf = r"D:\我的\学校要求\求职\简历.pdf"
    try:
        with open(resume_pdf, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label=t('download_btn'),
            data=pdf_bytes,
            file_name="徐朝阳_简历.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
    except FileNotFoundError:
        st.caption("简历文件暂未找到")

    st.divider()

    # ---- 快捷提问 ----
    st.markdown(f"<p style='color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 1px; margin-bottom: 12px;'>{t('quick_ask')}</p>", unsafe_allow_html=True)

    quick_qs = [
        (t('quick_q1'), "介绍一下他的项目经历"),
        (t('quick_q2'), "他有哪些核心技能？"),
        (t('quick_q3'), "他的求职意向是什么？"),
    ]

    for i, (label, question) in enumerate(quick_qs):
        if st.button(label, use_container_width=True, key=f"qq_{i}"):
            st.session_state.pending_question = question
            st.session_state.active_tab = 2  # 自动跳转到 AI 问答
            st.rerun()


# ========== 主页面：自定义标签栏 ==========
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0

tab_labels = [t('tab1'), t('tab2'), t('tab3')]
cols = st.columns(len(tab_labels))
for i, (col, label) in enumerate(zip(cols, tab_labels)):
    with col:
        btn_type = "primary" if st.session_state.active_tab == i else "secondary"
        if st.button(label, use_container_width=True, type=btn_type, key=f"tab_btn_{i}"):
            st.session_state.active_tab = i
            st.rerun()

st.divider()

# ---- Tab 0：关于我 ----
if st.session_state.active_tab == 0:
    st.title(t('about_heading'))
    st.caption(t('about_sub'))

    # 基本信息卡片
    lang = st.session_state.language
    info_card_zh = """
    <div style="
        background: linear-gradient(135deg, #12122a 0%, #1a1a35 100%);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 28px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px 32px;
        font-size: 14px;
    ">
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">👤 姓名</span><br><span style="color: #e0e0e0;">徐朝阳</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📍 籍贯</span><br><span style="color: #e0e0e0;">河南 · 南阳</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">🎓 教育背景</span><br><span style="color: #e0e0e0;">天津农学院 · 种子科学与工程 · 2024级</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📧 邮箱</span><br><span style="color: #e0e0e0;">1952859208@qq.com</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📱 电话</span><br><span style="color: #e0e0e0;">15237709204</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">🔗 GitHub</span><br><a href="https://github.com/zhaoyangxu18-pixel" style="color: #8b9cf6; text-decoration: none;">zhaoyangxu18-pixel</a></div>
    </div>
    """
    info_card_en = """
    <div style="
        background: linear-gradient(135deg, #12122a 0%, #1a1a35 100%);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 28px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px 32px;
        font-size: 14px;
    ">
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">👤 Name</span><br><span style="color: #e0e0e0;">Xu Zhaoyang</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📍 Hometown</span><br><span style="color: #e0e0e0;">Nanyang, Henan</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">🎓 Education</span><br><span style="color: #e0e0e0;">Tianjin Agricultural University · Seed Science & Engineering · 2024–2028</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📧 Email</span><br><span style="color: #e0e0e0;">1952859208@qq.com</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">📱 Phone</span><br><span style="color: #e0e0e0;">15237709204</span></div>
        <div><span style="color: rgba(255,255,255,0.4); font-size: 11px; letter-spacing: 1px;">🔗 GitHub</span><br><a href="https://github.com/zhaoyangxu18-pixel" style="color: #8b9cf6; text-decoration: none;">zhaoyangxu18-pixel</a></div>
    </div>
    """
    st.markdown(info_card_zh if lang == 'zh' else info_card_en, unsafe_allow_html=True)

    st.markdown(t('about_text'))

# ---- Tab 1：项目经历 ----
elif st.session_state.active_tab == 1:
    st.title(t('projects_heading'))

    projects = [
        ('project1', t('project1_title'), t('project1_tech'), t('project1_desc')),
        ('project2', t('project2_title'), t('project2_tech'), t('project2_desc')),
        ('project3', t('project3_title'), t('project3_tech'), t('project3_desc')),
    ]

    for i, (key, title, tech, desc) in enumerate(projects):
        st.markdown(f"### {title}")
        st.markdown(f"**技术栈：** `{'` `'.join(tech.split(' / '))}`")
        st.markdown(desc)
        if i < len(projects) - 1:
            st.divider()

# ---- Tab 2：AI 问答 ----
else:
    st.markdown("""
    <style>
    .stChatInput { position: sticky; bottom: 0; z-index: 100; }
    .stChatFloatingInputContainer { bottom: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.title(t('ai_title'))
    st.caption(t('ai_caption'))

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    from langchain_openai import ChatOpenAI

    @st.cache_resource
    def load_llm():
        return ChatOpenAI(
            model="deepseek-chat",
            openai_api_base="https://api.deepseek.com/v1",
            openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=0.3,
            streaming=True
        )

    def load_resume():
        with open("data/resume.txt", "r", encoding="utf-8") as f:
            return f.read()

    def ask_resume_stream(llm, resume_text, question):
        system_prompt = (
            "你是一个简历问答助手。根据下面提供的完整简历信息回答问题。\n"
            "用第三人称他来介绍这个人。如果信息不足，就说根据简历不太确定。\n"
            "保持友好、专业的语气。\n\n"
            f"=== 完整简历 ===\n{resume_text}"
        )
        for chunk in llm.stream([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]):
            if chunk.content:
                yield chunk.content

    try:
        llm = load_llm()
        resume_text = load_resume()
        st.success(t('ai_ready'))
    except Exception as e:
        st.error(f"加载失败：{e}")
        st.stop()

    # ---- 聊天记录 + 快捷提问处理 ----
    chat_container = st.container()
    with chat_container:
        # 显示历史消息
        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # 处理侧边栏快捷提问（在容器内渲染，与普通聊天一致，无闪动）
        if st.session_state.get("pending_question"):
            q = st.session_state.pop("pending_question")
            st.session_state.chat_messages.append({"role": "user", "content": q})
            with st.chat_message("user"):
                st.write(q)
            with st.chat_message("assistant"):
                stream = ask_resume_stream(llm, resume_text, q)
                answer = st.write_stream(stream)
            st.session_state.chat_messages.append({"role": "assistant", "content": answer})

    # ---- 聊天输入框 ----
    if question := st.chat_input(t('ai_placeholder')):
        st.session_state.chat_messages.append({"role": "user", "content": question})
        with chat_container:
            with st.chat_message("user"):
                st.write(question)
            with st.chat_message("assistant"):
                stream = ask_resume_stream(llm, resume_text, question)
                answer = st.write_stream(stream)
        st.session_state.chat_messages.append({"role": "assistant", "content": answer})
