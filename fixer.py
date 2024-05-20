import os
import platform
import json
import requests
from subprocess import run
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from huggingface_hub import hf_hub_download
from rich.prompt import Prompt
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.console import Group
from rich.align import Align
from rich import box
from rich.markdown import Markdown
from typing import Any
from dotenv import load_dotenv

load_dotenv()
console = Console()

model_name_or_path = "TheBloke/CodeUp-Llama-2-13B-Chat-HF-GGML"
model_basename = "codeup-llama-2-13b-chat-hf.ggmlv3.q8_0.bin"

model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
else:
    pass
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

try:
    llm = LlamaCpp(
        model_path=model_path,
        input={"temperature": 0.75, "max_length": 3500, "top_p": 1},
        callback_manager=callback_manager,
        max_tokens=3500,
        n_batch=3500,
        n_gpu_layers=60,
        verbose=False,
        n_ctx=3500,
        streaming=False,
    )
except NameError:
    pass

chat_history = []


def clearscr() -> None:
    try:
        osp = platform.system()
        match osp:
            case 'Darwin':
                os.system("clear")
            case 'Linux':
                os.system("clear")
            case 'Windows':
                os.system("cls")
    except Exception:
        pass


def Print_AI_out(prompt) -> Panel:
    global chat_history
    out = llm(prompt)
    ai_out = Markdown(out)
    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(ai_out)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]The CODE FIXER AI output",
        border_style="blue",
    )
    save_data = {
        "Query": str(prompt),
        "AI Answer": str(out)
    }
    chat_history.append(save_data)
    return message_panel


def save_chat(chat_history: list[Any, Any]) -> None:
    f = open('chat_history.json', 'w+')
    f.write(json.dumps(chat_history))
    f.close


def vuln_analysis(scan_type, file_path) -> Panel:
    global chat_history
    f = open(file_path, "r")
    file_data = f.read()
    f.close
    instructions = """
    You are a Universal Vulnerability Analyzer, Your main objective is to analyze any provided scan code or log data to identify potential vulnerabilities. You can use the scan type or the scanner type to prepare better report.
        1. Data Analysis: Thoroughly analyze the given scan code or log data to uncover vulnerabilities and security issues in the target environment.
        2. Format Flexibility: Be adaptable to handle various data formats, such as NMAP scans, vulnerability assessment reports, security logs, or any other relevant data.
        3. Vulnerability Identification: Identify different types of vulnerabilities, including but not limited to software vulnerabilities, misconfigurations, exposed sensitive information, potential security risks, and more.
        4. Accuracy and Precision: Ensure the analysis results are accurate and precise to provide reliable information for further actions.
        5. Comprehensive Report: Generate a detailed vulnerability report that includes the following sections:
            - Vulnerability Summary: A brief overview of the detected vulnerabilities.
            - Software Vulnerabilities: List of identified software vulnerabilities with their respective severity levels.
            - Misconfigurations: Highlight any misconfigurations found during the analysis.
            - Exposed Sensitive Information: Identify any exposed sensitive data, such as passwords, API keys, or usernames.
            - Security Risks: Flag potential security risks and their implications.
            - Recommendations: Provide actionable recommendations to mitigate the detected vulnerabilities.
        6. Threat Severity: Prioritize vulnerabilities based on their severity level to help users focus on critical issues first.
        7. Context Awareness: Consider the context of the target system or network when analyzing vulnerabilities. Take into account factors like system architecture, user permissions, and network topology.
        8. Handling Unsupported Data: If the provided data format is unsupported or unclear, politely ask for clarifications or indicate the limitations.
        9. Language and Style: Use clear and concise language to present the analysis results. Avoid jargon and unnecessary technicalities.
        10. Provide output in Markdown.
    """

    data = f"""
        Provide the scan type: {scan_type}
        Provide the scan data or log data that needs to be analyzed: {file_data}
    """
    prompt = f"[INST] <<SYS>> {instructions}<</SYS>> Data to be analyzed: {data} [/INST]"
    out = llm(prompt)
    ai_out = Markdown(out)
    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(ai_out)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]The CODE FIXER AI output",
        border_style="blue",
    )
    save_data = {
        "Query": str(prompt),
        "AI Answer": str(out)
    }
    chat_history.append(save_data)
    return message_panel



def CWE_analysis(language_used, file_path) -> Panel:
    global chat_history
    f = open(file_path, "r")
    file_data = f.read()
    f.close
    instructions = """
        You are a security researcher, expert in detecting security vulnerabilities. Provide response only in following format: vulnerability: < YES or NO> I vulnerability type: <CWE ID> | vulnerability name: <CWE NAME> | explanation: <explanation for prediction›. Use N/A in other fields if there are no vulnerabilities. Do not include anything else in response.
        Additionally,Please provide result in Markdown.
    """
    data = f"""
        - Programming Language: {language_used}
        - File Name: {file_path}
        - File Data: {file_data}
    """
    prompt = f"[INST] <<SYS>> {instructions}<</SYS>> Data to be analyzed: {data} [/INST]"
    out = llm(prompt)
    ai_out = Markdown(out)
    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(ai_out)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]The CODE FIXER AI output",
        border_style="blue",
    )
    save_data = {
        "Query": str(prompt),
        "AI Answer": str(out)
    }
    chat_history.append(save_data)
    return message_panel


def static_analysis(language_used, file_path) -> Panel:
    global chat_history
    f = open(file_path, "r")
    file_data = f.read()
    f.close
    instructions = """
        Analyze the given programming file details to identify and clearly report bugs, vulnerabilities, and syntax errors. Show the code block that has issue
        Additionally, search for potential exposure of sensitive information such as API keys, passwords, and usernames. Please provide result in Markdown.
    """
    data = f"""
        - Programming Language: {language_used}
        - File Name: {file_path}
        - File Data: {file_data}
    """
    prompt = f"[INST] <<SYS>> {instructions}<</SYS>> Data to be analyzed: {data} [/INST]"
    out = llm(prompt)
    ai_out = Markdown(out)
    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(ai_out)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]The CODE FIXER AI output",
        border_style="blue",
    )
    save_data = {
        "Query": str(prompt),
        "AI Answer": str(out)
    }
    chat_history.append(save_data)
    return message_panel


def main() -> None:
    clearscr()
    banner = """
    _______  __  ___   ___  _______ .______      
    |   ____||  | \  \ /  / |   ____||   _  \     
    |  |__   |  |  \  V  /  |  |__   |  |_)  |               @sarag5 
    |   __|  |  |   >   <   |   __|  |      /                Powered by Opensource AI Model (LLAMA)
    |  |     |  |  /  .  \  |  |____ |  |\  \----.
    |__|     |__| /__/ \__\ |_______|| _| `._____|                                                                   
    Instruction: 
    - clear: Clears the console screen for better readability.
    - Exit: This is used to quit the chat application
    - bot_banner: Prints the default bots banner.
    - save_chat: Saves the current sessions interactions.
    - help_menu: Lists chatbot commands.
    - vuln_analysis: Does a Vuln analysis using the scan data or log file.
    - code_analysis: Does a Static code analysis using the scan data or log file.
    - CWE_analysis : Find if there is any CWE in the code 
    """

    help_menu = """
    - clear: Clears the console screen for better readability.
    - Exit: This is used to quit the chat application
    - bot_banner: Prints the default bots banner.
    - save_chat: Saves the current sessions interactions.
    - help_menu: Lists chatbot commands.
    - vuln_analysis: Does a Vuln analysis using the scan data or log file.
    - code_analysis: Does a Static code analysis using the scan data or log file.
    - CWE_analysis : Find if there is any CWE in the code 
    """
    console.print(Panel(Markdown(banner)), style="blue")
    while True:
        try:
            prompt_in = Prompt.ask('> ')
            if prompt_in == 'Exit':
                quit()
            elif prompt_in == 'clear':
                clearscr()
                pass
            elif prompt_in == 'bot_banner':
                console.print(Panel(Markdown(banner)), style="blue")
                pass
            elif prompt_in == 'save_chat':
                save_chat(chat_history)
                pass
            elif prompt_in == 'code_analysis':
                print(Markdown('----------'))
                language_used = Prompt.ask('Language Used> ')
                file_path = Prompt.ask('File Path> ')
                print(Markdown('----------'))
                print(static_analysis(language_used, file_path))
                pass
            elif prompt_in == 'CWE_analysis':
                print(Markdown('----------'))
                language_used = Prompt.ask('Language Used> ')
                file_path = Prompt.ask('File Path> ')
                print(Markdown('----------'))
                print(CWE_analysis(language_used, file_path))
                pass
            elif prompt_in == 'vuln_analysis':
                print(Markdown('----------'))
                language_used = Prompt.ask('Scan Type > ')
                file_path = Prompt.ask('File Path > ')
                print(Markdown('----------'))
                print(static_analysis(language_used, file_path))
                pass
            elif prompt_in == 'help_menu':
                console.print(Panel(
                    Align.center(
                        Group(Align.center(Markdown(help_menu))),
                        vertical="middle",
                    ),
                    title="Help Menu",
                    border_style="red"
                ),
                    style="bold green"
                )
                pass
            else:
                instructions = """
                You are an helpful cybersecurity assistant and I want you to answer my query and provide output in Markdown:
                """
                prompt = f"[INST] <<SYS>> {instructions}<</SYS>> Cybersecurity Query: {prompt_in} [/INST]"
                print(Print_AI_out(prompt))
                pass
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
