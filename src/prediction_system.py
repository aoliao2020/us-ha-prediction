#!/usr/bin/env python3
import os
import json
import smtplib
import requests
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    print("US→H→A 预测系统启动")

    # 市场数据（实际应从API获取）
    market_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "nasdaq_change": -2.1,
        "vix": 18.45,
        "hsi_close": 26630,
        "sh_close": 4162.88
    }

    # 预测逻辑（简化版）
    predictions = [
        {"sector": "生物医药", "prediction": 2.07, "prob": 55.3},
        {"sector": "周期", "prediction": 1.64, "prob": 56.7},
        {"sector": "金融", "prediction": 1.39, "prob": 57.1},
    ]

    # 生成报告
    generate_html(market_data, predictions)

    # 发送通知
    send_notification(market_data, predictions)

    print("完成!")


def generate_html(data, predictions):
    """生成HTML报告"""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>预测报告 {data['date']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }}
        h1 {{ color: #1e3a8a; }}
        .positive {{ color: green; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ background: #1e3a8a; color: white; padding: 10px; }}
        td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>US→H→A 预测报告 {data['date']}</h1>
        <p>纳斯达克: {data['nasdaq_change']}% | VIX: {data['vix']}</p>
        <table>
            <tr><th>板块</th><th>预测</th><th>概率</th></tr>"""

    for p in predictions:
        html += f"<tr><td>{p['sector']}</td><td class='positive'>+{p['prediction']}%</td><td>{p['prob']}%</td></tr>"

    html += "</table></div></body></html>"

    # 保存文件
    os.makedirs("reports", exist_ok=True)
    date_str = data["date"].replace("-", "")
    with open(f"reports/report_{date_str}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"报告已保存: reports/report_{date_str}.html")


def send_notification(data, predictions):
    """发送邮件"""
    if os.getenv("EMAIL_ENABLED") != "true":
        print("邮件已禁用")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv("SENDER_EMAIL")
        msg['To'] = os.getenv("RECIPIENT_LIST", "")
        msg['Subject'] = f"【周报】US→H→A预测 - {data['date']}"

        body = f"纳斯达克: {data['nasdaq_change']}%\\n最强板块: {predictions[0]['sector']}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(os.getenv("SMTP_SERVER", "smtp.gmail.com"),
                              int(os.getenv("SMTP_PORT", 587)))
        server.starttls()
        server.login(os.getenv("SENDER_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")


if __name__ == "__main__":
    main()