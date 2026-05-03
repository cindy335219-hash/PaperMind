import os
import time
import requests

# ========== 配置 ==========
API_KEY = os.environ.get("ZHIPU_API_KEY")
if not API_KEY:
    raise ValueError("请先设置环境变量：set ZHIPU_API_KEY=你的Key")

API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

def call_agent(agent_name, system_prompt, user_input):
    """通用 Agent 调用函数"""
    print(f"\n{'='*50}")
    print(f"[{agent_name}] 正在分析...")
    print(f"{'='*50}")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "glm-4-flash",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
    response.raise_for_status()

    result = response.json()["choices"][0]["message"]["content"]
    print(result)
    return result


def summary_agent(paper_text):
    """摘要 Agent：提取核心贡献"""
    system_prompt = """你是一个专业的学术论文摘要Agent。
你的任务是从论文中提取以下信息，并以结构化格式输出：
1. 核心研究问题
2. 主要方法创新点（2-3条）
3. 关键实验结果
4. 核心贡献总结（1-2句话）

请保持简洁，每条不超过2句话。"""

    return call_agent("摘要Agent", system_prompt, f"请分析以下论文内容：\n\n{paper_text}")


def critic_agent(paper_text):
    """批判 Agent：识别局限性与缺陷"""
    system_prompt = """你是一个严格的同行评审Agent，专门识别论文的不足之处。
请从以下角度分析论文的局限性：
1. 实验设计缺陷（样本量、对照组、数据集等）
2. 方法论局限（假设条件、适用范围等）
3. 结果可信度问题（是否充分验证）
4. 未解决的问题或未来工作方向

请以批判性视角客观分析，每条给出具体依据。"""

    return call_agent("批判Agent", system_prompt, f"请对以下论文进行批判性分析：\n\n{paper_text}")


def relation_agent(paper_text, existing_papers):
    """关联 Agent：发现与已读论文的关联"""
    system_prompt = """你是一个文献关联分析Agent。
你的任务是分析当前论文与已有文献库的关联关系，输出：
1. 共同研究主题/领域
2. 方法论上的继承或对比关系
3. 可能存在的引用关系（谁引用了谁的思路）
4. 研究脉络梳理（这些工作共同构成了什么研究方向）

请明确指出具体的关联点，避免泛泛而谈。"""

    user_input = f"""当前论文：
{paper_text}

---

已有文献库：
{existing_papers}"""

    return call_agent("关联Agent", system_prompt, user_input)


def integrate_results(summary, critique, relations):
    """整合层：汇总三个 Agent 的输出，生成最终报告"""
    print(f"\n{'='*50}")
    print("[整合层] 正在生成最终报告...")
    print(f"{'='*50}")

    system_prompt = """你是一个学术报告整合Agent。
请将以下三个分析模块的结果整合成一份结构清晰的阅读报告。
报告应包含：执行摘要、核心评估、关联发现、阅读建议。
语言简洁专业，总字数控制在400字以内。"""

    user_input = f"""摘要Agent输出：
{summary}

批判Agent输出：
{critique}

关联Agent输出：
{relations}"""

    return call_agent("整合层", system_prompt, user_input)


def analyze_paper(paper_text, existing_papers="暂无已读文献"):
    """主函数：运行完整的多 Agent 分析流程"""
    print("\n" + "="*50)
    print("  多Agent学术文献分析系统 启动")
    print("="*50)

    summary = summary_agent(paper_text)
    time.sleep(2)

    critique = critic_agent(paper_text)
    time.sleep(2)

    relations = relation_agent(paper_text, existing_papers)
    time.sleep(2)

    final_report = integrate_results(summary, critique, relations)

    print("\n" + "="*50)
    print("  分析完成")
    print("="*50)

    return {
        "summary": summary,
        "critique": critique,
        "relations": relations,
        "final_report": final_report
    }


# ========== 示例运行 ==========
if __name__ == "__main__":

    sample_paper = """
    Title: Attention Is All You Need
    
    Abstract: The dominant sequence transduction models are based on complex recurrent or 
    convolutional neural networks that include an encoder and a decoder. The best performing 
    models also connect the encoder and decoder through an attention mechanism. We propose a 
    new simple network architecture, the Transformer, based solely on attention mechanisms, 
    dispensing with recurrence and convolutions entirely. Experiments on two machine translation 
    tasks show these models to be superior in quality while being more parallelizable and 
    requiring significantly less time to train.
    
    Key Results: Achieved 28.4 BLEU on WMT 2014 English-to-German translation task, 
    outperforming existing best results by over 2 BLEU. Training took 3.5 days on 8 P100 GPUs.
    
    Method: Multi-head self-attention mechanism with positional encoding. The model uses 
    scaled dot-product attention: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V.
    """

    existing_papers = """
    Paper 1: "Neural Machine Translation by Jointly Learning to Align and Translate" (Bahdanau et al., 2015)
    - 提出了注意力机制的早期版本，用于机器翻译中的序列对齐
    
    Paper 2: "Sequence to Sequence Learning with Neural Networks" (Sutskever et al., 2014)  
    - 提出了基于LSTM的Encoder-Decoder框架，是Transformer的前身
    """

    results = analyze_paper(sample_paper, existing_papers)