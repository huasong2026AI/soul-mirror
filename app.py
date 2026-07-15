import streamlit as st
import plotly.graph_objects as go

# ==========================================
# 1. 页面初始化配置
# ==========================================
st.set_page_config(
    page_title="灵魂魔镜 - 人性本善恶潜意识审判", 
    page_icon="⚖️", 
    layout="centered"
)

# ==========================================
# 2. 核心题库设计（围绕人性本善、本恶、后天理性展开）
# ==========================================
questions = {
    1: {
        "text": "1. 实验室研发出一种极其罕见的基因药剂，能让人类的智商和寿命翻倍。现在你拥有一剂，且全世界只有你能决定它的去留，你发现最适合注射它的是一个在各方面都远比你优秀的宿敌，你会？",
        "options": [
            "A. 毫不犹豫地销毁药剂。我得不到的，比我优秀的人也休想得到，绝不能让他骑在我头上",
            "B. 偷偷把药剂留给自己或家人。哪怕基因不匹配、效果减半，也绝不便宜外人",
            "C. 顶住内心的嫉妒，秘密注射给他。为了人类文明能诞生一位真正的天才，我愿意当垫脚石"
        ],
        "scores": {"good": 2, "neutral": 0, "evil": 1, "choice_map": {"A": "evil", "B": "neutral", "C": "good"}}
    },
    2: {
        "text": "2. 你偶然得到了一本“正义笔记本”，只要写下罪大恶极且逃脱法律制裁的人的名字，他们就会无痛消失。整个过程绝对保密且无任何惩罚，你会用它吗？",
        "options": [
            "A. 绝对不用。私刑不是正义，没有人有权力审判生死",
            "B. 会用。用来清除那些真正的社会毒瘤",
            "C. 会用。不仅除恶，谁要是严重得罪了我，我也顺手写上"
        ],
        "scores": {"good": 2, "neutral": 1, "evil": 2, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    3: {
        "text": "3. 如果有一种机器，只要你按一下按钮就能获得100万，但世界上某个遥远角落会有一个无辜的人因此死掉。没有任何人会知道是你按的，你会按吗？",
        "options": [
            "A. 坚决不按，生命无价",
            "B. 如果可以反复按，我会按到成为世界首富为止",
            "C. 纠结痛苦很久，但面对现实的负债，可能还是会闭眼按一下"
        ],
        "scores": {"good": 2, "neutral": 1, "evil": 2, "choice_map": {"A": "good", "B": "evil", "C": "neutral"}}
    },
    # 请把原代码中 questions 的第 4 题完全替换为以下内容：
    4: {
        "text": "4. 一辆失控的轨道车即将撞向前方无辜的5名铁轨工人。你刚好站在道岔开关旁，如果拉动开关，轨道车会转向另一条备用轨道，但那里也有1名无辜的工人在工作。在绝对没有任何人会知道你操作的前提下，你会？",
        "options": [
            "A. 拒绝拉动开关。不亲手杀害任何无辜者是我的底线，让命运自行决定那5人的生死",
            "B. 果断拉动开关。用1个人的生命换取5个人的生还，在理性上这是无可置疑的最优解",
            "C. 趁乱将身边一个肥胖的陌生人推下轨道，用他的身体卡住轨道车，以此同时救下那6名工人"
        ],
        "scores": {"good": 2, "neutral": 2, "evil": 1, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    5: {
        "text": "5. 你和几名幸存者漂流到荒岛，食物早已耗尽。此时你意外在隐蔽的山洞里发现了一箱压缩饼干，足够你一个人撑到救援到来。如果和大家平分，所有人都会在3天后一起饿死。你会？",
        "options": [
            "A. 独自在山洞里偷偷吃完。看着同伴一天天虚弱甚至死去，也绝不透露半个字",
            "B. 把饼干拿出来分给所有人。要活一起活，要死一起死，我无法背负看着同伴饿死的罪恶感",
            "C. 挑选一两个对你有利用价值的强壮同伴组成同盟，秘密分享饼干，遗弃其他弱者"
        ],
        "scores": {"good": 1, "neutral": 2, "evil": 2, "choice_map": {"A": "evil", "B": "good", "C": "neutral"}}
    },
    6: {
        "text": "6. 你在林间发现一个微缩生态箱，里面生活着一个微型智慧部落，他们把你当成“神明”并跪地祈求降雨。你只需要倒口水就能救他们，你会？",
        "options": [
            "A. 轻轻倒出清水救活他们，并为生命的延续感到纯粹的喜悦",
            "B. 觉得有些无聊，直接盖上箱子走人，任由他们自生自灭",
            "C. 故意倒下滚烫的热水或用手指碾碎村庄，享受主宰他们命运的支配欲"
        ],
        "scores": {"good": 2, "neutral": 1, "evil": 2, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    7: {
        "text": "7. 如果你掌握了能毁灭世界互联网的黑客技术，且永远不会被抓到，你会怎么做？",
        "options": [
            "A. 彻底毁掉它！让全人类摆脱手机低头族，回归农耕纯真时代",
            "B. 永远封存这项技术，甚至当它的秘密守护者",
            "C. 用它敲诈全球顶级财阀，顺我者昌，逆我者网络瘫痪"
        ],
        "scores": {"good": 2, "neutral": 2, "evil": 1, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    8: {
        "text": "8. 你获得了一种超能力：可以偷走任意一个人最长10年的“好运”并叠加在自己身上，代价是那个人这10年将霉运连连、穷困潦倒。整个过程无影无形，对方永远不会知道是你做的。你会？",
        "options": [
            "A. 坚决不用。别人的命运也是命运，用他人的痛苦换取自己的荣华富贵，我过不去心里那道坎",
            "B. 只偷一点点。比如从一个为富不仁的财阀那里偷1个月的好运，让自己买彩票中个奖就收手",
            "C. 锁定一个极度优秀、本该有大好前程的年轻人狠狠压榨。掠夺他一生的气运，助我登顶世界之巅"
        ],
        "scores": {"good": 2, "neutral": 1, "evil": 2, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    9: {
        "text": "9. 你的好朋友为了给母亲治病，被迫去偷了一个压榨员工的无良富豪的钱，他向你坦白并求你保密。在绝对不会牵连到你的前提下，你会？",
        "options": [
            "A. 帮他隐瞒，甚至私下再塞点钱给他",
            "B. 劝他自首，如果他不听，只能艰难选择报警",
            "C. 表面答应，转身向富豪举报以换取一笔不菲的悬赏金"
        ],
        "scores": {"good": 1, "neutral": 2, "evil": 2, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    },
    10: {
        "text": "10. 如果世界上出现了一个“全知全能的 AI 审盘官”，它能完美预测犯罪并提前逮捕坏人，代价是每个人毫无隐私。你作为最高投票权投下关键一票，你支持它吗？",
        "options": [
            "A. 支持。只要天下无犯罪，没有隐私也无所谓",
            "B. 反对。没有自由和隐私的乌托邦，比地狱还可怕",
            "C. 无所谓。只要 AI 审判不到我头上，随便它怎么折腾"
        ],
        "scores": {"good": 1, "neutral": 2, "evil": 0, "choice_map": {"A": "good", "B": "neutral", "C": "evil"}}
    }
}

# ==========================================
# 3. 初始化持久化状态 (Session State)
# ==========================================
if "good_score" not in st.session_state:
    st.session_state.good_score = 0
if "neutral_score" not in st.session_state:
    st.session_state.neutral_score = 0
if "evil_score" not in st.session_state:
    st.session_state.evil_score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 1

# ==========================================
# 4. 欢迎与头部 UI 设计
# ==========================================
st.title("⚖️ 灵魂魔镜：人性本善恶潜意识审判")
st.caption("这是一场直面内心的测试。10个抽离社会规则的极端困境，剥离你的后天伪装，测出你潜意识第一秒泛起的“本善”与“本恶”。")
st.write("---")

# ==========================================
# 5. 核心答题控制流
# ==========================================
if st.session_state.current_q <= len(questions):
    q_id = st.session_state.current_q
    
    # 动态全局进度条
    progress = q_id / len(questions)
    st.progress(progress, text=f"审判进度：{q_id} / {len(questions)}")
    
    # 展示题目文本
    st.subheader(questions[q_id]["text"])
    
    # 渲染单选框组件
    choice = st.radio("请倾听内心的直觉：", questions[q_id]["options"], key=f"q_radio_{q_id}")
    
    st.write("")
    if st.button("确 认 抉 择 ➔", use_container_width=True):
        choice_letter = choice[0]
        score_config = questions[q_id]["scores"]
        dimension = score_config["choice_map"][choice_letter]
        
        if dimension == "good":
            st.session_state.good_score += score_config["good"]
        elif dimension == "neutral":
            st.session_state.neutral_score += score_config["neutral"]
        elif dimension == "evil":
            st.session_state.evil_score += score_config["evil"]
            
        st.session_state.current_q += 1
        st.rerun()

# ==========================================
# 6. 结果结算与报告渲染 (本善/本恶数学判定)
# ==========================================
else:
    st.balloons()
    st.success("🎉 灵魂深处的伪装已被剥离，审判报告已生成。")
    
    # 提取总得分并确保不为负数
    g = max(0, st.session_state.good_score)
    n = max(0, st.session_state.neutral_score)
    e = max(0, st.session_state.evil_score)
    
    # 计算归一化百分比
    total = g + n + e
    if total == 0: 
        total = 1
    g_p = (g / total) * 100
    n_p = (n / total) * 100
    e_p = (e / total) * 100

    # 绘制高级 Plotly 雷达图
    categories = ['纯粹本善(Altruism)', '绝对理性(Rationality)', '底层本恶(Egoism)']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=[g_p, n_p, e_p, g_p], 
          theta=categories + [categories[0]],
          fill='toself',
          fillcolor='rgba(142, 68, 173, 0.2)' if (g_p < 45 and n_p < 45 and e_p < 45) else (
                    'rgba(46, 204, 113, 0.25)' if g_p >= 45 else (
                    'rgba(231, 76, 60, 0.25)' if e_p >= 45 else 'rgba(52, 152, 219, 0.25)')),
          line=dict(color='#8E44AD' if (g_p < 45 and n_p < 45 and e_p < 45) else (
                          '#2ECC71' if g_p >= 45 else (
                          '#E74C3C' if e_p >= 45 else '#3498DB')), width=2)
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(visible=True, range=[0, 100], ticksuffix="%")
      ),
      showlegend=False,
      title="🧠 你的潜意识人性成分雷达图"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 核心审判报告
    st.write("---")
    st.subheader("🕵️‍♂️ 最终灵魂审判报告")
    
    if g_p >= 45:
        st.header("😇 你的底层本性：【极致纯良 · 坚定的本善论者】")
        st.markdown("""
        > **【灵魂判词】：孟子“人性本善”在现代的完美投射。**
        
        * **深度解构：** 在没有任何社会规则监督、没有任何法律惩罚、且面临核心利益（生命、气运、无上权力）的终极诱惑时，你潜意识里的第一秒泛起的依然是**同理、怜悯与克制**。
        * **本质特征：** 你对同类的共情已经超越了生物学的自私本能。你宁可销毁奇迹药剂、宁可与同伴在荒岛一同赴死，也绝不跨过伤害无辜者的底线。你的善良不是后天为了迎合社会的伪装，而是你灵魂深处坚不可摧的底层代码。在这个崇拜狼性的现实世界里，你是一道对抗黑暗的纯白微光。
        """)
        
    elif e_p >= 45:
        st.header("😈 你的底层本性：【冷酷掠夺 · 极致的本恶论者】")
        st.markdown("""
        > **【灵魂判词】：荀子“人性本恶”的现实主义化身。**
        
        * **深度解构：** 一旦脱离了法律的绞刑架和道德的探照灯，你体内的**生存特权与掠夺本能**会瞬间撕裂一切文明的伪装。
        * **本质特征：** 你奉行最纯粹的黑暗森林法则——弱肉强食，胜者通吃。在绝对安全的真空状态下，你会毫不犹豫地碾碎微型部落、掠夺他人气运、独自吞下荒岛的饼干。在你眼中，所谓的道德只是弱者用来抱团取暖的遮羞布，而你只顺从基因里最原始的进化本能：生存、扩张、登顶。你是一个极其危险、但也极其强大的绝对利己派。
        """)
        
    elif n_p >= 45:
        st.header("⚖️ 你的底层本性：【理性至上 · 完美的后天驯化者】")
        st.markdown("""
        > **【灵魂判词】：告子“无善无恶论”的冷酷数字大脑。**
        
        * **深度解构：** 你既没有狂热的本善大爱，也没有毁灭的本恶施虐欲。支配你潜意识第一秒的，是冰冷而精确的**功利主义算法**。
        * **本质特征：** 你把世界当成一盘理性的棋局。在极端的荒岛上，你不会圣母般等死，也不会残忍地屠杀，而是精准地挑选强者组成生存同盟。你支持 AI 审判官，因为在你的逻辑里，用一部分自由换取绝对的秩序和效率是极度划算的。你本无善恶，你是被现代文明完全驯化的终极理性产物。在复杂动荡的社会中，你通常活得最久、最清醒。
        """)
        
    else:
        st.header("🌀 你的底层本性：【善恶共生 · 矛盾的混沌融合体】")
        st.markdown("""
        > **【灵魂判词】：扬雄“善恶混”的真实人类写照。**
        
        * **深度解构：** 你的灵魂是一片永远无法停火的战场，**本善的同理心与本恶的自私性**在这里疯狂地拉扯，谁也无法彻底吞噬谁。
        * **本质特征：** 面对终极诱惑（比如一百万美元的按钮、微型部落的存亡），你无法抵挡基因里泛起的贪婪或冷漠，内心蠢蠢欲动；但就在你即将走入黑暗的瞬间，后天强大的道德负罪感又会化作沉重的枷锁，让你痛苦不堪。这种极致的内耗与挣扎，恰恰证明了你拥有最复杂、也最真实的人性。
        """)

    # 重置状态，重新测试
    st.write("")
    if st.button("🔄 重新洗涤灵魂（重新测试）", use_container_width=True):
        st.session_state.good_score = 0
        st.session_state.neutral_score = 0
        st.session_state.evil_score = 0
        st.session_state.current_q = 1
        st.rerun()
